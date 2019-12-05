---
title: coc-nvim-qa
date: 2019-12-05 14:40:44
tags: 
  - "Vim"
  - "NeoVim"
categories: 配置文件
comments: true
---

# 记录使用 `coc.nvim` 的过程中发现的问题与解决办法
- [coc.nvim](https://github.com/neoclide/coc.nvim) 是一个非常nice的(Neo)Vim的插件，提供 [LSP](https://microsoft.github.io/language-server-protocol/specifications/specification-3-14/) 全功能支持，除了Debug，补全，跳转，重构，文档等都有不同程度的支持(看相应的 language server (如 C++的 ccls ， Java 的 eclipse.jdt.ls )是否提供...)

## 如何修改基于使用 `clang-format` 格式化代码的样式 
> 用于解决使用coc.nvim作为LSP框架的找了老半天无法修改默认Format样式的问题

- 在代码所在项目根目录中加入 `.clang-format`， 这样如 `clangd`, `ccls`这些LS就会使用调用 `clang-format` 载入配置文件进行格式化了.

- 我喜欢的一套代码风格，只不过把缩进改为2空格了

```
# .clang-format
---
Language:        Cpp
BasedOnStyle:  Chromium
TabWidth:        2
UseTab:          Never
...

```
