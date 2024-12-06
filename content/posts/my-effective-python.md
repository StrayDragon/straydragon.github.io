---

title: 'My Effective Python'
date: 2019-12-23T20:42:30+08:00
tags:
- python2
- python3
categories:
- '技术积累'
- '阅读笔记'
comments: true
draft: true
---


# 请定义项目根目录, 并克制使用 `../../` 相对路径

- 版本 1
```
$ python spider/run.py
```

- 版本 2
```
$ cd spider/
$ python run.py
```

如果run.py中有上一级目录的依赖(包导入,文件操作等), 第二个版本的调用操作可能会失败,通过定义一个根目录,根据根目录路径走相对或绝对都是确切唯一的,以解决这种不一致的问题
