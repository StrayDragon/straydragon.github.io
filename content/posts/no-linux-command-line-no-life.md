---

title: 'Linux命令行世界: 生存指南'
tags:
- 'Linux'
categories:
- '读书笔记'
- '备忘录'
comments: true
date: 2020-02-10T15:32:28+08:00
draft: false
enableLastMod: true
enableWordCount: true
enableReadingTime: true
---

我的读书笔记: 摘自《Linux命令行与Shell脚本编程大全》中那些有意义的技巧和命令...

<!-- more -->
鉴于Linux发行版太多了, 这里只会记录那些看上去通用的命令和技巧,旨在在大多数环境中正常工作.
另请注意:
- 这些命令运行在 TTY (**T**ele**Ty**peWriter) 或 TE(Terminal Emulator)中,为方便查找将以每个标题中以`--TTY/--TE/--TE/TTY`表示适用性.
- 大多数终端下使用的命令都有man手册或-help/--help/...帮助信息,若想深入了解请输入那些命令查看
- 占位符(placeholder) 一般使用大写字母(如: KEYWORD) 表示需要用户根据自己条件更改相应信息



# 命令 Commands


## `setterm` --TTY
```bash
$ # 重见光明
$ setterm -inversescreen on # 反转屏幕颜色 黑->白
$ # 或者
$ setterm -background white
$ setterm -foreground black
$
$ # 感受色彩 COLOR: black,red,green,yellow,blue,magenta,cyan,white
$ setterm -background COLOR
$ setterm -foreground COLOR
$
$ # 一切归初
$ setterm -reset
```
> P19

## `man` --TE/TTY

### 按关键字查找已有手册
```bash
$ man -k KEYWORD # KEYWORD: 按关键字查找已有手册
```
> P36

### 获取不同章节(section)下的手册
```bash
$ man SECTION_NUMBER TARGET # 获取TARGET的SECTION_NUMBER的手册
SECTION_NUMBER:
       1   Executable programs or shell commands
       2   System calls (functions provided by the kernel)
       3   Library calls (functions within program libraries)
       4   Special files (usually found in /dev)
       5   File formats and conventions, e.g. /etc/passwd
       6   Games
       7   Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7)
       8   System administration commands (usually only for root)
       9   Kernel routines [Non standard]
```
> P37 以及 `$ man man`


## `rm` --TE/TTY

### 推荐替换默认`rm`命令,以防手划
```
$ alias rm='rm -i'
$ rm -i FILE
rm: remove regular file 'FILE'?:y<CR> # 确认删除
# 或者
rm: remove regular file 'FILE'?:n<CR> # 取消
```

# Notes:

## 从哪里知道启动哪个Shell?

```bash
$ cat /etc/passwd | grep USERNAME # USERNAME: 如 root
USERNAME:x:1000:1000:USERNAME:/home/USERNAME:/usr/bin/zsh # <- 这里即默认启动的Shell
```
> P33

## Linux文件目录含义与名称
TODO
> P39

## Linux文件权限见`ls -l` 输出
TODO
> P43,45

## 适用于模式匹配的内置命令
- `?`(1), `*`(0 or N)
- `[CHARACTERS]`(可选列表) `[!CHARACTERS]`(排除列表)

> P45

## 链接文件
- 符号链接/软链接
- 硬链接


# 基本命令清单备忘录
- `CMD`  : 代表这个CMD默认来自外部指令(非内建)
- `CMD`\*: 代表这个CMD默认来自Shell(Bash-like)自身或保留字(内建)
- `CMD`+ : 代表这个CMD有内建和非内建的实现
> 可以用 `type CMD` 来判断内建/非内建指令

## Shell环境管理
### 增
#### `export`\*
#### `<env>="<value>"`
### 删
#### `unset`\*
### 查
#### `printenv`
#### `env`
#### `set`\*
#### `echo`+

## 命令管理
### `type`\*
### `which`\*
### `history`\*
### `alias`\*

## 路径管理
### `cd`\*
### `pwd`\*

## 文件管理
### 增
#### `touch`
#### `ln`
#### `mkdir`
#### `cp`
#### `gzip`,`zip`,... / `gunzip`,`unzip`,... | `tar`
### 删
#### `rm`
### 改
#### `mv`
#### `umask`
#### `chmod`
#### `chown`
#### `chgrp`
#### `sed`
#### `gawk`
### 查
#### `ls`
#### `file`
#### `cat`
#### `more`/`less`
#### `head`/`tail`
#### `du`
#### `sort`
#### `grep`

## 文件系统管理
- `fdisk`
- `mkfs.*`
- `fsck`

## 进程(Process)管理
### 增
#### `sleep`
#### `CMD &`
#### `nohup`
#### `bg`\*
#### `nice`
### 删
#### `kill`
#### `killall`
#### `exit`
### 改
#### `renice`
### 查
#### `ps`\*
#### `jobs`\*
#### `coproc`\*
#### `lsof`

## 磁盘(Disk)管理
### 增
#### `mount`
### 删
#### `unmount`
### 查
#### `df`

## 用户管理
### 增
- `useradd`
### 删
- `userdel`
### 改
- `usermod`
- `passwd` / `chpasswd`
- `chage`
- `chage`
- `chsh`

## 用户组管理
### 增
- `groupadd`
### 改
- `groupmod`
