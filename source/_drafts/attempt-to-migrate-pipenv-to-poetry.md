---
title: '一次迁移Pipenv到Poetry的经历与踩坑总结'
comments: true
date: 2019-12-26 18:55:43
tags:
  - 'Python3'
  - 'Poetry'
  - 'Pipenv'
categories:
  - '未归类'
---

其实从Poetry本身的配置上看, 有两种作用域: 一个是全局配置(config), 一个是本地配置(config ... --local)
这一点也和VSCode,coc.nvim的配置非常类似

```
$ # 全局配置: 使用豆瓣源(或者加 --local 本地工作空间)
$ poetry config repositories.douban https://pypi.doubanio.com/simple/
$ # poetry config repositories.douban https://pypi.doubanio.com/simple/ --local
$
$ # 让 Poetry 在项目根目录中生成虚拟环境文件夹, 默认会生成: .venv/ , 由于我使用coc-python的LSP支持,在相关配置后,也无法正确找到解释器及相关库,如果你用的环境可以找到目标的virtualenv目录,这条配置可以忽略
$ poetry config virtualenvs.in-project true
$ # poetry config virtualenvs.in-project true --config
```
