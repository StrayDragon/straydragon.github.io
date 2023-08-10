---

title: '少年, 带上coc.nvim, 在 (Neo)Vim 的世界中尽情翱翔吧!'
date: 2019-12-25T22:07:44+08:00
draft: false
tags:
- 'Vim'
- 'NeoVim'
categories:
- '插件与扩展'
comments: true
draft: false
---


标题略显中二, 请自行脑补为这是一篇介绍`coc.nvim`的文章,正如其官网所说,给你以VSCode一般的优秀体验,甚至对于Vimer来讲,这是一款极其优秀,反应很快的值得尝试的插件.
<!-- more -->

# 写在前面:

阅读本篇文章,请至少阅读完Vimtutor,并对插件系统有一定的了解,或多或少的尝试过为你的(Neo)Vim安装过插件,如果你体验过其他老牌的补全插件,并为之苦恼,最终可能直接放弃使用,转投IDEs或Emacs了,至少对于新手而言, Vim实在不是那么友好(想起了这个 问题==SOF:如何退出Vim==)不过这一款出自国人大佬==赵启明==之手的优秀插件足以使你重新拾起(Neo)Vim,在不需要放弃Vim高效的操作模式,享受编程的快感.

## 这里是一些给老手们的参考资料

- 强烈建议浏览一下该项目的Github主页, 以及部分Wiki内容, 因为文档足够优秀,即使你不看这篇文章也可以找到大部分解决办法,这也是必备的技能之一.如果你还是一头雾水,那么可以浏览一下本文,找到你期待的内容,如果没有的话,请联系我,我也希望可以与你共同进步,一起完善这个很优秀的开源项目.
- 这篇文章中不会介绍如何安装, 如何配置(Neo)Vim的`.vimrc/init.vim`,这些内容大佬的README中已经介绍的足够完备,本篇文章作为一个补充以及一些没有直接体现在Wiki中的经验.

> [coc.nvim](https://github.com/neoclide/coc.nvim) 是一个非常 nice 的(Neo)Vim 的插件，提供 [LSP](https://microsoft.github.io/language-server-protocol/specifications/specification-3-14/) 全功能支持，除了 Debug，补全，跳转，重构，文档等都有不同程度的支持(看相应的 language server (如 C++的 ccls ， Java 的 eclipse.jdt.ls )是否提供...)

# 对一些LSP的使用建议
如:
- 学习查看LS的Debug信息,排查问题原因

# 配置管理: 模块化

如何模块化你的配置文件呢,这一主题,你可以在我自己的模块配置[StrayDragon/Mine0Vim](https://github.com/StrayDragon/Mine0Vim) 中找到相关配置或者灵感.

# Q&A: 使用 coc.nvim 遇到的一些问题

看一看 [AwesomeVim](https://vimawesome.com/) 这里面无数的插件们的更新日期, 能积极活跃的老牌插件真的不多,这一节会向你展示我的一些推荐,以及经典插件的coc插件替代品

- 记录使用 `coc.nvim` 的过程中发现的问题与解决办法, 将在之后整理成为入门教程(==待定==)
  > 由于 `coc.nvim` 并不会主动添加快捷键, 跟随官网的配置设置后也并不能涵盖有的需求, 接下来会以我的实际使用经历逐步完善...


## 悬浮窗口显示(也就是`Hover`)滚动文档窗口

> 用于解决有的 doc 太长无法,只能看到部分的问题.
> 注意: 目前该特性是 Neovim Only 的

- 查看相关文档说明:

```
:h coc#util#has_float()
:h coc#util#float_scroll()
```

- 添加快捷映射

```vimscript
"在Hover调出之后使用
"  Ctrl + f 文档翻页, 光标仍在原来文件
nnoremap <expr><C-f> coc#util#has_float() ? coc#util#float_scroll(1) : "\<C-f>"
"在Hover调出之后使用
"  Ctrl + k 光标进入悬浮窗口, 此时hjkl可在文档内移动,在此使用该快捷键跳出
nnoremap <expr><C-k> coc#util#has_float() ? coc#util#float_scroll(0) : "\<C-k>"
```

- 参考:
  > https://github.com/neoclide/coc.nvim/issues/609

## 修改基于使用 `clang-format` 格式化代码的样式

> 用于解决使用 coc.nvim 作为 LSP 框架的找了老半天无法修改默认 Format 样式的问题

- 在代码所在项目根目录中加入 `.clang-format`， 这样如 `clangd`, `ccls`这些 LS 就会使用调用 `clang-format` 载入配置文件进行格式化了.

- 我喜欢的一套代码风格，只不过把缩进改为 2 空格了

```
# .clang-format
---
Language:        Cpp
BasedOnStyle:  Chromium
TabWidth:        2
UseTab:          Never
...

```
