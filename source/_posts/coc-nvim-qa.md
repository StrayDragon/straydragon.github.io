---
title: "Q&A: coc.nvim"
date: 2019-12-05 14:40:44
tags:
  - "Vim"
  - "NeoVim"
categories: 配置文件
comments: true
---

- 记录使用 `coc.nvim` 的过程中发现的问题与解决办法, 将在之后整理成为入门教程(==待定==)
  > [coc.nvim](https://github.com/neoclide/coc.nvim) 是一个非常 nice 的(Neo)Vim 的插件，提供 [LSP](https://microsoft.github.io/language-server-protocol/specifications/specification-3-14/) 全功能支持，除了 Debug，补全，跳转，重构，文档等都有不同程度的支持(看相应的 language server (如 C++的 ccls ， Java 的 eclipse.jdt.ls )是否提供...)
  > 由于 `coc.nvim` 并不会主动添加快捷键, 跟随官网的配置设置后也并不能涵盖有的需求, 接下来会以我的实际使用经历逐步完善...

<!-- more -->

# 悬浮窗口显示(也就是`Hover`)滚动文档窗口

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

# 修改基于使用 `clang-format` 格式化代码的样式

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
