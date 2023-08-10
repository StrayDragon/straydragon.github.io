---

title: 'Cling: 一个C++的解释器'
tags:
  - 'C++'
  - 'Jupyter Notebook'
categories: '实用工具'
comments: true
date: 2019-07-28T22:22:32+08:00
draft: true

---

> [Cling](https://github.com/root-project/cling.git) : C++ REPL [^1]

<!-- more -->

# 安装
## 直接运行
- 下载最新包解压对应版本直接运行即可 [下载地址](https://root.cern.ch/download/cling/)

## 编译安装
```bash
wget https://raw.githubusercontent.com/root-project/cling/master/tools/packaging/cpt.py

chmod +x cpt.py
./cpt.py --check-requirements && ./cpt.py --create-dev-env Debug --with-workdir=./cling-build/
```

# 集成到Jupyter内核

Jupyter C++ kernel ([Cling/tools/Jupyter](https://github.com/root-project/cling/tree/master/tools/Jupyter))
```bash
git clone https://github.com/root-project/cling.git

pip3 install tools/Jupyter/kernel/

jupyter kernelspec install kernel/cling-cpp11
jupyter kernelspec install kernel/cling-cpp14
jupyter kernelspec install kernel/cling-cpp17
```

[^1]: Hello [baidu](www.baidu.com)
