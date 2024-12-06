---
title: deep into git
tags:
- "git"
categories:
- "版本控制"
comments: true
date: 2020-04-04T14:45:55+08:00
draft: true
---

# 1. `仓库 B` Fork 了 `仓库 A`, 如何在`仓库 B` 中同步更新上游代码?

> 查找 "与上游保持同步": https://git-scm.com/book/zh/v2/GitHub-%E5%AF%B9%E9%A1%B9%E7%9B%AE%E5%81%9A%E5%87%BA%E8%B4%A1%E7%8C%AE

```
git remote add <NAME> <GIT_SERVER_URL_OR_GIT>
```

如:

```
git remote add upstream https://github.com/schacon/blink
```

最后使用这个,查询信息

```
git remote -v # 查看远程仓库情况
```

或直接修改 .git/config

# 2. `仓库 B` Fork 了 `仓库 A`, 但想合并 `仓库 A` 中有权限的人未合并的 PR

> 参考: https://d.cosx.org/d/420363-pr/6

首先使用 `# 1` 添加上游的源, 然后:

```
git pull <NAME> refs/pull/<PR的序号>/head:<新本地分支名字或省略>
```

如:

```
git pull origin refs/pull/771/head:patch-2
```

然后若有冲突按照提示进行操作即可
