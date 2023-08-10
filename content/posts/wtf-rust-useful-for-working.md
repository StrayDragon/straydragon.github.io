---

title: '哇塞Rust: 关于Cargo.toml的二三事'
tags:
- Rust
categories:
- 阅读笔记
- 学习笔记
date: 2019-12-26T09:02:53+08:00
draft: true
---

> 记录学习Rust过程中那些看起来对于实际工程很有帮助的技巧

# 以更低优化级别用于开发,以更高优化级别编译用于发布

优化级别与编译速度一般关系[^1]如下
- 慢<- 编译速度 ->快
- 高<- 优化级别 ->低
```toml
# ...

[profile.dev]
opt-level = 0 # 默认值 0, 故可以不设置

[profile.release]
opt-level = 3

# ...
```
==TODO:这里以后补充更多关于性能调优的知识==


## 参考:
[^1]: [The Rust Programming Language(Second Edition)]() # Cargo and Crates.io
