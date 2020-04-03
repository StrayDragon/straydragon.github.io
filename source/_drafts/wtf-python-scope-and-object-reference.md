---

title: '哇塞Python: 作用域与对象引用'
date: 2019-12-25 22:49:27
tags:
  - 'Python'
  - 'Python3'
categories:
  - '阅读笔记'
comments: true

---
Python一直以来都因看上去简单易用, 而受到不少人的青睐, 然鹅, 架不住一些历史和设计的原因 存在不少令人抓狂的规则, 让人摸不到头脑.
![wtf](./wtf_title.png)


> 来自: [twitter/laike9m](https://twitter.com/laike9m/status/1236846226462523393?s=19)

今天在瞎写自己的`tweedle`这个CLI工具时, 终于被上图的某个错误理解而导致不断报错, 于是我决定, 重拾基础, 争取通过此文整理好Python中作用域和传递对象引用的相关的坑

<!-- more -->

一般这种时候没有一个非常友好的inspect方法是不行的, 那么我们需要立刻寻找相关命令行工具和模块?

No~No~No~, 就我以前的开发经历来看, 常常会因解决X而递归的解决一系列路上遇到的问题,最后解决了Y...效率实在不太好, 于是掏出神器 [Python Tutor](http://pythontutor.com/) 来基本观察内部结构变化, 之后再上那些屠龙刀(这个作者看上去一点也Hack啊 = =|||), 具体效果如下图所示(可能有网不太好的同学,体验稍差,可以在此Repo https://github.com/pgbovine/OnlinePythonTutor 按README指导自行安装部署本地版本哦):

![example](./python_tutor_example.png)

复制以下代码, 自己感受下吧!

```python
g = None
def foo():
    a = 1
    b = 2
    def bar():
        print(b)
        print(g)
        c = 2
    bar()

foo()
```

- [ ] 学会组织一篇文章, 让读者阅读起来舒服,流畅



# 参考资料:

- Python2.7 文档 相关章节
- Python3.6 文档 相关章节
- Python3.8 文档 相关章节
- Python3学习笔记 雨痕
- Effective Python Brett Slatkin

> ==TODO:这里把看过的相关博客,StackOverFlow的问答,知乎的相关问题答案链接贴上来,方便读者交叉阅读==
