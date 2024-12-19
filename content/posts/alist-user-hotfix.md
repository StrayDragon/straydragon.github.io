---
title: "Alist 维护与疑难杂症解决"
date: 2024-08-20T21:04:02
draft: false
---

这里收集并整理一些遇到的使用问题, 方便读者可以快速定位问题解决方案!

<!--more-->

## alist 网页客户端使用 VLC 视频一键播放/直接点击图标按钮打开

### linux

> 版本: 3.34.0
>
> 环境:
>
> WM: Hyprland (Wayland)
>
> Kernel: Linux 6.10.2-arch1-1

![](8ECAFD58663042ADB5FECF5A411B3751_MD5.webp)

1. 将 `~/.config/mimeapps.list` 中 `[Default Applications]` 条目中 vlc 相关的配置,增加或修改为 `x-scheme-handler/vlc=vlc-url-handler.desktop`

2. 创建或修改 `~/.local/share/applications/vlc-url-handler.desktop` 为

```
[Desktop Entry]
Name=VLC media player - URL Handler
Comment=Read, capture, broadcast your multimedia streams
Exec=/usr/bin/open-alist-vlc %U
Icon=vlc
Terminal=false
Type=Application
Categories=AudioVideo;Player;Recorder;
NoDisplay=true
StartupNotify=true
Categories=Application
```

3. 创建或修改 `/usr/bin/open-alist-vlc` 为

```bash
#!/bin/bash

process_string() {
    local input="$1"

    # 判断 $1 是否以 'vlc:' 开头，如果是则去掉
    if [[ "$input" == vlc:* ]]; then
        input="${input#vlc://}"
    fi

    # 判断剩下的字符串是否以 'http//' 开头，如果是则替换为 'http://'
    if [[ "$input" == http//* ]]; then
        input="${input/http\/\//http://}"
    fi

    # 返回处理后的字符串
    echo "$input"
}

processed=$(process_string "$1")
/usr/bin/vlc "$processed"
```

然后 `{bash} chmod +x /usr/bin/open-alist-vlc`

4. 运行下面命令

```bash
sudo update-desktop-database ~/.local/share/applications
sudo update-desktop-database

```

5. 刷新 alist 视频网页并尝试一键播放

