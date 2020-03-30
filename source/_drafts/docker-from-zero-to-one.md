---

title: '从零到一的Docker旅行'
date: 2020-02-25 16:56
tags: 
	- 'docker'
categories:
	- '笔记'
comments: true

---

> 记录一下从头开始学习使用docker中遇到的问题
> 笔者使用 ArchLinux with i3/KDE, 自这个文章创建时, 才接触ArchLinux半个月...不过有其他发行版至少2年的使用经验
> 让我们开始吧~

<!-- more -->

# 1. 安装
注意: 可能有时效性,请自行确认日期
> 参考: 
> - https://computingforgeeks.com/installing-docker-ce-ubuntu-debian-fedora-arch-centos/
> 对于Debian系/Fedora/CentOS/RHEL来说,tuna有个安装应用的镜像,注意只是应用镜像
> - https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/

# 2. 配置
需要`sudo systemctl start docker`来启动docker.server,不过这样并不会使得docker服务每次开机都自动打开, 因为我只是希望做一些练习, 用时启动对于我来说是不错的,不用的时候不用有开销(大概),如果你希望它默认启动,请启用并建立链接
```bash
sudo systemctl enable docker
sudo systemctl start docker
```
## 运行`docker version`, 遇到 "Got permission denied while trying to connect to the Docker daemon socket..."
- Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/version: dial unix /var/run/docker.sock: connect: permission denied

其实已经给出错误提示, 运行此命令为普通user,所以没权限, 建议不要获取root权限运行,
参考官网处理一下就好,

[Manage Docker as a non-root user](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user#manage-docker-as-a-non-root-user)

## \[配置文件\] 换默认DockerHub镜像源
不作多余解释了...QAQ

> 参考:
> https://juejin.im/post/5cd2cf01f265da0374189441
> https://yeasy.gitbooks.io/docker_practice/install/mirror.html
> https://www.jianshu.com/p/84b6fe281b4d

其实有的时候镜像源有可能没来得及更新导致一些校验错误, 或许你需要以http代理的方式解决下载问题了. 

ArchWiki是个寻找答案的好地方: https://wiki.archlinux.org/index.php/Docker_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)#%E4%BB%A3%E7%90%86%E9%85%8D%E7%BD%AE
