---

title: "开发日记: 时间管理应用"
date: 2020-01-02 08:12:32
tags: 
  - "Flutter"
categories: 
  - "开发日记"
comments: true

---

> 开新坑咯...
> 
> 我想通过开发日记的形式记录过程中的想(wa)法(keng)与吐(bei)槽(nüè), 由以往的经验来看,要想快速理解一个项目, 除了开发者关心的版本控制记录之外(如:commit logs / issues 等), 及时的文档与从零开始的介绍也是非常重要的,故诞生此文,希望我能坚持下去~
>
> **PS:** 
> - 我不太喜欢把系列文章分成那么多篇,所以暂时都写在这, 以`0x`序号为主顺序.
> - 笔者初次写作, 若有任何不通或小错误, 任何建议与批评都是欢迎的, 祝你阅读愉快~


# 0x00 开篇准备与碎碎念

<!-- more -->

## 动机/契机
由于`Flutter`其非常优秀的原生渲染以及跨平台的能力十分诱人,也充分满足我的平台需求,虽然有不少的坑,也写过一些demo体验过,但还是值得一试的;其次我想构建一个完整的软件, 除了这几个前端还要包含后端的部分的,而[微服务(Microservices)](https://en.wikipedia.org/wiki/Microservices) 一词经常出现在我阅读的技术文章中,因此感到很好奇,在阅读相关解释后发现虽然并不是很适合我准备制作的App的需求(有点太小题大作了,当然,如果可以维护到那个规模,试一试也未尝不可),而其"原型"面向服务架构 ([Service-oriented architecture, SOA](https://en.wikipedia.org/wiki/Service-oriented_architecture)) ,更为适合我想要打造出来的那个系统符合的架构名字,标题也因此而来.

希望这个应用的服务可以体现出组件的高复用性, 并易于重构, 并提供其他多个后端网络服务扩展如: 云备份, 搜索, 记录分析等
> 以下指导原则是开发，维护和使用SOA的基本原则[3]：
> - 可重复使用、粒度、模块性、可组合型、对象化原件、构件化以及具交互操作性
> - 符合开放标准（通用的或行业的）
> - 服务的识别和分类，提供和发布，监控和跟踪。
>
> 摘自: [维基百科 SOA的主要三原则](https://en.wikipedia.org/wiki/Service-oriented_architecture):

以上原则(或者叫特性),加强了这一做法的可行性,正所谓"面向需求编程", 而不是"面向高端大气上档次的技术名词编程"(虽然这个标题还是有点...),
所以我决定尝试在这一过程中更多地验证所学并克服更多技术问题,深入浅出,以项目驱动学习,实践这些应用技能,适当时候也会反模式让其更适应需求.

想开发这个App的想法来自于我体验过的许多应用,如Android上的 `Microsoft Todo`, `番茄Todo` , iOS上的 `时间块`等时间管理类应用,它们很好很成熟,制作精良. 但还是感觉用的不是很顺手,似乎各有优点,但又没有办法可以很好的扩展, 比如:
- `MS Todo` 中的 "我的一天" 会给你根据过去添加记录的建议,以快速完成这个动作,而另一些软件却没有这个很实用的功能;
- `番茄Todo` 可以再添加事项后提供可选的计时,倒计时功能(虽然很繁琐), 而 `MS Todo` 却没有(也许这不是这该应用的产品功能吧,但我真的需要这个功能,甚至发了Feature Request...)
- `时间块` 有非常直观可视的区块添加事件,是对`日历`一类应用的加强,但却无法计时.
- ...
以上这些,如果可以更好的衔接,舒服地UX体验,流畅的UI,那该有多好!

除此之外,学习时间管理等自我管理的方法, 养成高效规划与执行的习惯, 才是我的最终目的,而这个辅助工具的功能开发的会首先考虑自己的需求(这也是一强大动力哈), 但我会将其开源,尽可能提供较少开销的**扩展机制**,放到这里[StrayDragon/Daily](https://github.com/StrayDragon/Daily).

## 功能计划 [待补充]

**注意**: 详细的文档说明,将会更新在Github项目主页上(或许是issues) [StrayDragon/Daily](https://github.com/StrayDragon/Daily)

## 前端

> 这里有一些过去的功能需求文档: [StrayDragon/Daily/doc/ProjectDescription](https://github.com/StrayDragon/Daily/blob/master/doc/ProjectDescription.md)

除此之外:
- 克隆一下以上提到的那些应用的需求
  - 任务/事项的推荐
  - 时间管理模块(如计时...)
  - [扩展] 数据分析模块(如习惯分析...)
  - [扩展] 搜素模块
  - [扩展] 信息持久化模块(如云备份...)
  
- 至少 Linux/Web 与 Android 的UI布局需要有所更改

## 后端
- 针对以上 [扩展] 模块进行API的开发


## 技术选型
如以下表格所示:

| 职责 | 主要语言 | 生态    | (备选)                    | 用于构建                          |
| ---- | -------- | ------- | ------------------------- | --------------------------------- |
| 后端 | Python   | Django  | Flask                     | API Server                        |
| 前端 | Dart     | Flutter | React Native, Vue混合开发 | Linux, Android, Web平台的前端应用 |

简单来说(以编程语言导向):

- Flutter 负责 所有的用户端(大前端): Linux, Android, Web (暂时只针对这三个平台优先开发, 其他平台由于多方原因(Win不常用,iOS没Mac...),视情况而定)
- Python的Web后端生态 负责 API Server的开发 实现前后端分离

- 数据库将会从以下选择中: 使用SQL数据库(SQLite, MySQL/MariaDB, PostgreSQL)与NoSQL数据库(Redis, MongoDB), 挑选适合的数据库完成衔接后端服务模块
- 其他
  - 会有真正"服务器"去启动Web端, 如Nginx, Gunicorn...


## 可能学到什么 [待补充]
- 使用多种应用技术构建整体系统服务的一次项目实践

- Web后端应用的相关知识与数据库应用知识

- 掌握Flutter应用开发的一些小技巧和基本组件,并享受不断学习,重构完善的过程

- Git与Github:
  - 更规范的Git commit messages / log / tag 管理
  - 更熟练地使用Git常用命令
  - 学会掌握Github Flow 的开发流程. 
  - 严格的Review与PR模拟

- 测试与持续集成
  - 更强的更为规范的单元/集成测试,覆盖率检查与代码质量检查以及对APIServer的压力测试
  - 与Circle CI等在线持续集成系统结合,完善测试自动化过程

## 参考资料 [待补充]

#### 前端

- [Flutter 官方文档](https://flutter.dev/docs)
- 《Flutter技术入门与实战》

#### 后端

- [Django 官方文档](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
- [Flask 官方文档](https://flask.palletsprojects.com/)

#### 工具链相关

- 《Pro Git》

- 《Github入门与实践》
#### 测试相关
- 《Google软件测试之道》
- 《C++ 程序设计实践与技巧 测试驱动开发》

