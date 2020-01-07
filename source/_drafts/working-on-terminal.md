---

title: '终端工作的高效方式' 
date: 2019-12-22 19:10:48
tags:
  - 'CLI'
  - 'TUI'
categories: '未归档'
comments: true

---

# Vim基本操作
```
ggVG                # 全选 (V-Line Mode)
ggVG"+y             # 全选并复制到系统剪切版（寄存器）
<C-o> / <C-i>       # 返回上/下一个操作
za                          # 折叠/不折叠操作
zM                              #全部折叠
zR                          # 全部展开
<S-*> / <S-#>           # 高亮当前所在单词并跳到下/上一个出现的位置
```


# 完全终端工作高效方式 TUI Effective way
---

## 文件管理 `Ranger`

## 单终端模拟器窗口管理 `Tmux`

## 多终端模拟器窗口管理  `i3-wm`

## 编辑器 + 一堆插件 `NeoViM / ViM`

# 便携编程 Pocket Programming 

## 场景一 有安卓手机有大屏平板

## `Termux` (*nix shell)
- Android Phone 

## `Shelly` (SSH Client App)
- iPad

# 效率工具

## Terminal Application

### `tmux`: 单终端下分屏分窗口分会话

### `ranger`: TUI 文件管理器

### `autojump` : （不推荐 慢）快速跳转

###  `z.lua` : 快速跳转

### `tldr`: 终端工具简易使用片段

### `icdiff`: 横向diff工具

### `tokei`: 代码计数工具

### `screenfetch`: 设备信息和logo

### `mosh` : 基于UDP的“SSH”替代品
- 有相关的客户/服务器端，适合较差网络，可断网重连，但是没有明显改善我的iPad与Linux/Android通信的摁键延迟问题

### `bat`: `cat`的替代方案

### `exa`: `tree` 和 `ls` 的替代方案

### `micro`: `nano`的替代方案

### `lazygit`: `git` TUI管理工具

### `fzf`: 模糊路径查找工具

### `cppman`: 查看C++文档

## Application

### `gdbgui`: Web版GDB调试工具

### `TermuxArch`: 模拟ArchLinux环境，使用pacman (需要安装TermuxApp)

# 配置与插件

## `(Neo)Vim` 配置
> (暂时以Android上的配置为主配置，其他由github仓库同步配置)，

- 2019/11/28
    - [x] 关闭所有不太会用的插件
    - [x] 优化配置格式
- 2019/11/29
    - [x] 配置自动下载Plug插件，进行自动化安装插件
    - [x] 更新一些自定义快捷键给vim-which-key
    - [x] 尝试折腾一下C++的Debug工具和用法 -> `gdbgui`
- 2019/11/30
    - [x] 优化启动速度 
    - [x]  Debug Tools, (Neo)Vim的集成
- 2019/12/1
    - [x] 重新整理一下 init.vim 由 **按键配置分开** 到 **以功能为界限分割** 的配置内容
- 2019/12/23~
    - [x] 学习方便的查看文档
    - [x] 将常用coc插件写入vimrc (coc-json, coc-rls, coc-snippets...)
    
###插件升级
- 2019/11/28
    - `lightline.vim`: 替换缓慢笨重的 `vim-airline`
- 2019/11/30
    - Debug插件 `neodbg.vim`(bug太多) , `vim-padre`(`Vim` only)
    - 启动时间检查 `startuptime.vim`


