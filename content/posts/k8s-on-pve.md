---
title: "在PVE中搭建K8S学习环境"
date: 2024-12-21T16:12:30
draft: false
tags:
- "k8s"
categories:
- "配置文件"
- '学习笔记'
enableLastMod: true
enableWordCount: true
enableReadingTime: true
---


本文用 kubeadm 搭建环境, 并使用PVE创建和管理虚拟机, 参考以下材料完成, 读者可以直接参考相关官方文档, 调整安装过程以适配自己的环境
- [安装 kubeadm | Kubernetes](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)


<!--more-->


## 验证与准备工作

以下内容不是这篇文章的重点, 按照顺序仅供读者参考, 相关内容将不会具体描述
- 硬件环境: 有一台预先安装配置好 PVE 8.0+,  CPU性能不太差, 大内存(空闲16GB以上)最好的物理机
    - 我的硬件配置为 5825U + 32GB内存
- 初始化debian12虚拟机的过程:
    - 下载并安装 debian12 镜像(建议使用离线完整包, 不要更新时debian security的包容易拉取不下来)到 PVE
    - 配置好虚拟机: **尤其注意需要关闭swap分区**(虽然可以调整配置与swap启用兼容运行, 但是官方不推荐, 这里提前关闭可以减少问题)
- 掌握方便配置Linux虚拟机的运维命令
    - 同时配置hostname和domain, 如 `hostnamectl set-hostname HOST_NAME` 等

## 在装好系统的虚拟机上, 安装 k8s(kubeadm)相关组件

本章主要参考 [准备开始 - 安装 kubeadm | Kubernetes](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#%E5%87%86%E5%A4%87%E5%BC%80%E5%A7%8B)的内容, 并检查已经安装好的debian12虚拟机配置,  我们之后会从这个配置中 clone 出多个虚拟机来组建集群

- [ ] 确保每个节点上 MAC 地址和 product_uuid 的唯一性
    - PVE中clone后虚拟机会生成新的 MAC 地址 和 product_uuid: 具体可以看下: [[SOLVED] - when cloning a kvm VM the mac address is renewed | Proxmox Support Forum](https://forum.proxmox.com/threads/when-cloning-a-kvm-vm-the-mac-address-is-renewed.28153/)
- [ ] 检查所需端口
    - `nc 127.0.0.1 6443 -v` , 如果提示 `nc: connect to 127.0.0.1 port 6443 (tcp) failed: Connection refused` 则 OK
- [ ] 交换分区的配置: 见 [[#验证与准备工作]]
- [ ] 安装容器运行时(负责运行容器的软件)
    - 建议安装 `containerd`, 使用以下命令安装 `sudo apt update && sudo apt install containerd`
- [ ] 安装 kubeadm、kubelet 和 kubectl
    - 按照官方描述 [在 Linux 系统中安装并设置 kubectl | Kubernetes](https://kubernetes.io/zh-cn/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management) 安装即可
    - **NOTE: 一定要固定这三个软件的版本号, 不然会版本冲突**
- [ ] 配置 cgroup 驱动程序
    - 主要是确认是否 containerd 和 kubelet 都使用同一个驱动, 否则会出现问题

我推荐顺手安装下一些方便我们观测系统的程序, 比如

```bash
sudo apt update && sudo apt install btop k9s
```

额外配置(以下配置为官方没有说明的配置)

- [ ] 配置 ip 地址转发 | 否则会在调用 `kubeadm init` 报错
```
# edit /etc/sysctl.conf
net.ipv4.ip_forward=1
```
重启或使用 `sudo sysctl --system`  检阅并永久生效


## 利用 kubeadm 创建集群

确定目标: 组件架构为 [高可用拓扑选项 | Kubernetes](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/ha-topology/#stacked-etcd-topology)
![606](./9650254AB2FD8B322845589BD5246A77_MD5.svg)

因此需要配置以下服务器:
- 负载均衡 >= 1
- 控制平面节点 >= 3
- 工作节点 >= 3

最后在PVE控制台中会部署并运行以下虚拟机(名字对应下面的标题)
![](./83D8F4267BCC4CF83CB4DDEA2B991AD5_MD5.webp)

### 负载均衡  | k8s-lb-1

这里直接新建一个虚拟机, 命名为 `k8s-lb`, 这里仅简单使用 nginx 配置负载均衡,  注意, 生产环境中推荐参考 [为 kube-apiserver 创建负载均衡器 | Kubernetes](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/high-availability/#%E4%B8%BA-kube-apiserver-%E5%88%9B%E5%BB%BA%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%99%A8), 其建议用[keepalived](https://www.keepalived.org) 和 [haproxy](https://www.haproxy.com) 的组合
- nginx配置如下
```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log warn;

include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 1024;  # 每个工作进程的最大连接数
}

stream {
# 日志格式定义
    log_format basic '$remote_addr [$time_local] '
                     '$protocol $status $bytes_sent $bytes_received '
                     '$session_time';

    access_log /var/log/nginx/stream-access.log basic;  # 访问日志路径及格式

    # 上游服务器配置，定义 Kubernetes 控制平面节点
    upstream k8s_control_plane {
        server 192.168.1.203:6443 max_fails=3 fail_timeout=10s;  # 第一个控制平面节点
        server 192.168.1.204:6443 max_fails=3 fail_timeout=10s;  # 第二个控制平面节点
        server 192.168.1.205:6443 max_fails=3 fail_timeout=10s;  # 第三个控制平面节点
    }

    # 服务器配置
    server {
        listen 6443;  # 监听端口
        proxy_pass k8s_control_plane;  # 将请求代理到上游服务器
        proxy_timeout 10m;  # 代理超时时间
        proxy_connect_timeout 1m;  # 连接超时时间
    }
}
```

这台主机的ip为 `192.168.1.191`

### 控制平面节点  | k8s-node-{1,2,3}

#### 对第一个即将成为控制平面节点的服务器  | k8s-node-1

- [ ] 检查要使用的网段
```shell
ip route show # 查找以 "default via" 开头的行
```
比如我这里的输出是
```
default via 192.168.1.1 dev ens18
192.168.1.0/24 dev ens18 proto kernel scope link src 192.168.1.203
```

- [ ] 初始化节点
记下来上一步输出的ip地址(`192.168.1.203`), 结合我们上一章节已经初始化好的负载均衡节点的ip(`192.168.1.191`), 可以通过以下任意一种方式初始化节点

- 通过命令 `kubeadm init --apiserver-advertise-address=192.168.1.203 --control-plane-endpoint=192.168.1.191 --image-repository registry.cn-hangzhou.aliyuncs.com/google_containers --upload-certs`
- 或者通过配置文件(固定命令到配置文件)
    1. 使用 `kubeadm config print init-defaults > kubeadm-config.yaml` 复制一份初始化配置
    2. 参考下面命令选项对应的配置文件字段中修改, 然后使用 `kubeadm init --config kubeadm-config.yaml --upload-certs` 进行初始化
> [!tip]+
>
> - 命令行参数：`--apiserver-advertise-address=192.168.1.203`
> - 配置文件字段：
> ```yaml
> apiVersion: kubeadm.k8s.io/v1beta3
> kind: InitConfiguration
> localAPIEndpoint:
> advertiseAddress: "192.168.1.203" # 指定了 API Server 向集群其他组件通告的 IP 地址
> ```
> - 命令行参数：`--control-plane-endpoint=192.168.1.191`
> - 配置文件字段：
> ```yaml
> apiVersion: kubeadm.k8s.io/v1beta3
> kind: ClusterConfiguration
> controlPlaneEndpoint: "192.168.1.191" # 指定了控制平面的稳定 IP 地址或 DNS 名称，通常用于高可用（HA）集群配置。
> ```
> - 命令行参数：`--image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers`
> - 配置文件字段：
> ```yaml
> apiVersion: kubeadm.k8s.io/v1beta3
> kind: ClusterConfiguration
> imageRepository: "registry.cn-hangzhou.aliyuncs.com/google_containers" # 定了 Kubernetes 组件镜像的仓库地址，通常用于替换默认的 `k8s.gcr.io` 仓库，以解决国内无法访问的问题
> ```

 无论你是使用哪种方法运行, 如果看到以下输出, 说明成功初始化了, 否则参考官方QA和[[#遇到的一些问题]]来排查错误
```bash
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of control-plane nodes by copying certificate authorities
and service account keys on each node and then running the following as root:

  kubeadm join 192.168.1.203:6443 --token abcdef.0123456789abcdef \
        --discovery-token-ca-cert-hash sha256:ed39da573eeda3b1a32e994be85677b0d33917f804770144f8221cf8b0cbadbf \
        --control-plane

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.1.203:6443 --token abcdef.0123456789abcdef \
        --discovery-token-ca-cert-hash sha256:ed39da573eeda3b1a32e994be85677b0d33917f804770144f8221cf8b0cbadbf
```
**NOTE: 请保存这个信息到一个安全的地方, 之后配置工作节点要用到**

4. 安装 Pod 网络附加组件

至此, 平面控制节点(可以理解为管理节点)的配置和初始化就完成了, 官方教程中还有一些内容可以额外设置, 读者可以自行参考学习

如果按照 [k9s](https://github.com/derailed/k9s) 文档完成配置, 你可以使用这个tui工具来查看和管理集群,  它覆盖了大部分 kubectl 常用管理命令, 类似于 lazydocker, lazygit等, 极大降低了学习和使用门槛

#### 对每个其他控制平面节点(非第一个)的服务器 | k8s-node-{2,3}

执行先前由第一个节点上的 kubeadm init 输出提供给你的 join 命令。 它看起来应该像这样：
```
sudo kubeadm join 192.168.0.203:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866 --control-plane --certificate-key f8902e114ef118304e561c3ecd4d0b543adc226b7a07f675f56564185ffe0c07
```
这个 --control-plane 标志通知 kubeadm join 创建一个新的控制平面。
    --certificate-key ... 将导致从集群中的 kubeadm-certs Secret 下载控制平面证书并使用给定的密钥进行解密。


### 工作节点 | k8s-node-{11,12,13}

接下来设置几个工作节点加入到管理节点中形成 k8s集群
0. 使用[[#每个其他控制平面节点(非第一个)的服务器]] 中记录的成功输出中的第二个命令(类似这样的命令), 在每一个即将成为工作节点的装有相关程序的服务器上运行
```sh
sudo kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866
```

最后可以看到类似这样的输出即可, 配置完成!!!

![1532](./8B9DB775D381EA6BDDB09FB488BEF4DD_MD5.webp)



## 遇到的一些问题 Q&A

### 运行 `kubeadm init` 时卡在 `[api-check]`
```bash
...
[kubelet-check] Waiting for a healthy kubelet at http://127.0.0.1:10248/healthz. This can take up to 4m0s
[kubelet-check] The kubelet is healthy after 501.152289ms
[api-check] Waiting for a healthy API server. This can take up to 4m0s
(卡住不动, 然后报错)
```

遇到这样的问题, 我们的思路应该是排查相关组件的日志, 比如先使用 `systemctl status kubelet` 查看一些日志信息

发现显示 `Unable to register node with API server" err="Post \"https://192.168.1.203:6443/api/v1/nodes\": dial tcp 192.168.1.203:6443: conne...`
这说明 api server 未启动成功, 但这个提示信息并不能定位问题

后来关注到运行初始化命令时, 有一条warning
```bash
...
W1222 16:47:43.888204     959 checks.go:846] detected that the sandbox image "registry.k8s.io/pause:3.6" of the container runtime is inconsistent with tha
t used by kubeadm.It is recommended to use "registry.aliyuncs.com/google_containers/pause:3.10" as the CRI sandbox image.
...
```
查询了一些资料, 发现原因是我的containerd配置不完整, 需要根据以下步骤配置好, 注意相关版本可能会随着时间而变动, 需要做调整!

0. 检查 `/etc/containerd/config.toml` 中 如果没有 `sandbox_image` 字段, 那就从步骤 1 继续操作, 否则跳转至步骤 2
1. 重新生成默认`containerd`配置 `containerd config default > /etc/containerd/config.toml`
2. 找到并修改字段  `sandbox_image = "registry.aliyuncs.com/google_containers/pause:3.10"`, 同时参考 [[#在装好系统的虚拟机上, 安装 k8s(kubeadm)相关组件]] 中 "配置 cgroups 驱动程序"内容
3. 重启服务: `systemctl restart containerd`

然后在重新初始化就可以了, 在初始化前可能要恢复出厂设置, 可以调用以下命令, 如果你想全部推倒重来, 可以参考这个文档 [使用 kubeadm 创建集群 | Kubernetes](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#tear-down)
```
kubeadm reset -f
systemctl restart kubelet
```