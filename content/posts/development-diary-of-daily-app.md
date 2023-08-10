---

title: "开发日记: 时间管理应用"
date: 2020-01-02T08:12:32+08:00
tags:
- "Flutter"
categories:
- "开发日记"
comments: true
draft: false

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

#### 通用工具

#### 前端

##### PC & Mobile
- [Flutter 官方文档](https://flutter.dev/docs)
- 《Flutter技术入门与实战》

###### 数据持久
> https://github.com/tekartik/sqflite | tekartik/sqflite: SQLite flutter plugin
> https://github.com/tekartik | Tekartik
> https://medium.com/flutter/flutters-ios-application-bundle-6f56d4e88cf8 | Flutter’s iOS Application Bundle - Flutter - Medium
> https://github.com/Jaguar-dart/jaguar_orm/issues | Issues · Jaguar-dart/jaguar_orm
> https://juejin.im/post/5c45c72d6fb9a049d81c2b4c | 手把手教你在Flutter项目优雅的使用ORM数据库 - 掘金

##### Web
> [vuetifyjs/vuetify: 🐉 Material Component Framework for Vue](https://github.com/vuetifyjs/vuetify)
> [ElemeFE/element: A Vue.js 2.0 UI Toolkit for Web](https://github.com/ElemeFE/element)
> [vuematerial/vue-material: Material design for Vue.js](https://github.com/vuematerial/vue-material)
> [airyland/vux: Mobile UI Components based on Vue & WeUI](https://github.com/airyland/vux)
> [Semantic-UI-Vue/Semantic-UI-Vue: Semantic UI integration for Vue](https://github.com/Semantic-UI-Vue/Semantic-UI-Vue)



#### 后端
> [tiangolo/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production](https://github.com/tiangolo/fastapi)
> [Django 官方文档](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
> [Flask 官方文档](https://flask.palletsprojects.com/)

##### 数据持久

> [dahlia/awesome-sqlalchemy: A curated list of awesome tools for SQLAlchemy](https://github.com/dahlia/awesome-sqlalchemy)
> [ponyorm/pony: Pony Object Relational Mapper](https://github.com/ponyorm/pony/)


##### 依赖管理

##### 维护工具

###### 部署
> [ansible/ansible: Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. ](https://github.com/ansible/ansible?hmsr=pycourses.com&utm_source=pycourses.com&utm_medium=pycourses.com)
>  - Avoid writing scripts or custom code to deploy and update your applications — automate in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com/ansible/


##### 面向服务体系架构与微服务
> https://www.redhat.com/zh/topics/microservices/what-are-microservices | 什么是微服务？
> https://en.wikipedia.org/wiki/Microservices | Microservices - Wikipedia
> https://zh.wikipedia.org/zh-cn/%E9%9D%A2%E5%90%91%E6%9C%8D%E5%8A%A1%E7%9A%84%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84 | 面向服务的体系结构 - 维基百科，自由的百科全书
> https://www.zhihu.com/question/65502802 | 什么是微服务架构？ - 知乎

######

#### 工具链相关

- 《Pro Git》
- 《Github入门与实践》

#### 测试相关
- 《Google软件测试之道》
- 《C++ 程序设计实践与技巧 测试驱动开发》


# 0x01 目标,需求分析与应用技术生态调研

## 目标
> 从不同的视角思考, 经常会获得更多的收获. 我将目前的所有认知与思考总结分类于此

### 产品目标

### 技术目标
> 这个章节将表达我期望使用的应用技术, 熟练程度.

- RESTful API, GraphQL
- 权限验证: JWT, Auth2
- 应用 `docker` 及相关生态

# 版本目标与需求和功能分析

鉴于需求往往会改变, 而落实完成功能往往会体现在大大小小的版本号上, 所以我将会及时更新目标,功能与需求说明, 最终体现在语义化版本号内容更新中

(注意: 这里确定的版本号与说明文只是文档版本(如 `v0.0.0-Luna`), 请以各个项目中实际版本的变动信息查询)

## 整体定位

包含待办事项, 番茄法计时, 象限分类, 优先级, 计划推荐(关键路径等算法), 自动化, 优势分析 等功能的时间管理应用

## v0.0.0-Luna

基于市面常见`TODO`应用, 完成待办事项基本功能, 实现基本应用框架, 并尝试完成各个平台部署.

**注意**: 此版本需要细心设计, 为未来功能开发作出合适的扩展设计

### 前端

整体描述:

- 减少或弃用 Dart(Flutter) 投入, 转而使用 JS/TS, HTML, Stylus 等大前端相关技术栈
  - 虽然使用 Flutter 开发过两三个 App(两个课设,一个实验项目), 但还是不太喜欢 Dart 在 Flutter 上的表现, 由于被禁了反射, 太多事情需要做的非常繁琐了, 比如它的 JSON 序列化, ORM 等, 虽然有 `codegen` 这个大杀器, 但有时候代码膨胀的厉害, 十分难受, 写起来总感觉有坏味道; 嵌套的多个部件拆分, 多种状态管理还是有点繁琐,当然也有更好的`inspector`工具了, 总而言之就是我太菜, 且不是很喜欢 Dart 提供的语法罢了(当然这不是主要原因)...
  - 反过来看回所谓大前端圈(主要是 TS 或 ES6 以后的 JS)的生态和方案, 学习成本降低了不少, 主要是我的需求可能不是最性能敏感的, 使用前端技术栈足以应对了. (另外确实想学习一下 TS 了 23333, 毕竟受到 `coc.nvim` 这个极其优秀的插件受到了极大的鼓舞, 也想写一些插件玩玩了, p.s.好像不是一个领域的东西 233333)
- 深入学习并应用跨端生成对应代码的技术, 争取最小化代价获得更多的代码复用

#### PC(Linux)

> **变更(主框架)**
>
> **弃用**: `Flutter Desktop` , 原因:
>
> - 不太稳定, 未进入主线支持;
> - 需重度使用的插件不支持(如 [sqflite](https://pub.flutter-io.cn/packages/sqflite) )
>
> **选用**: `Electron`, 原因:
>
> - 生态繁荣, 相关插件支持良好
> - 性能够用
> - 配合已有技术栈方便

由[技术调研](TODO)中得出的表现, 与实际需求对比, 最终还是还是放弃了 `FlutterDesktop`, 代价可能是丢掉了原生级别的高性能的用户体验, 但带来不小的开发效率的提升

##### Databases

如果需要缓存一些数据的话, 关系型貌似长久持久化支持完善的只有 `SQLite`, 短期可以存一存文档数据库, 不过需要进一步调研 ...

#### Web

> **变更简要(主框架):**
>
> **弃用**: `Flutter Web` , 原因:
>
> - 需重度使用的插件不支持, 如 [sqflite](https://pub.flutter-io.cn/packages/sqflite)
> - 包体积太大, 且有性能有点问题, 见 [如何评价 Flutter for Web？ - 闲鱼技术的回答 - 知乎](https://www.zhihu.com/question/323439136/answer/850516697);
> - 一些部件(Widget)有渲染问题
>
> **选用**: `Vuetify`, 原因:
>
> - 生态繁荣, 相关插件支持良好
> - 性能够用
> - `Material Design` 支持完善

#### CLI(\*nix)

> **等待调研**

方便更喜欢**Keyboard Only**的选手使用, 比如俺 QAQ

#### Mobile(Android)

> **暂时停止开发**

不过, 目前仍未找到合适的替代, `Flutter`仍是我看得到的所有技术中除原生外最好的选择(视时间待定)

### 后端

终于选中了合适的框架(`FastAPI`), 看上去非常好, 读了两天文档的直接感受就是作者很贴心和照顾新人, 社区活跃, 底层还算结实. 有完整的鉴权集成(OAuth2/1 with JWT, Basic HTTP Auth...), OpenAPI Schema 与 Swagger 文档生成, 真的吹爆(虽然可能 Swagger 早就出现过了, 可我第一次听说哈哈, 想想实习时和后端扯 API 规范扯来扯去, 当时咋就没遇到这个呢, 有了它就可以, 别 BB,文档 Sever 一直开着, 要啥返回啥自己看, 降低了沟通损耗, 真是赛高~), 与 ASGI 的结合和兼容同步写法的代码, GraphQL 等等一些我还没怎么接触过的东西, 项目驱动学习的感觉不错.

#### API Server

> 变更(主框架)
>
> 弃用: `Flask RESTFul API Server` 相关生态, 原因:
>
> - [基于 Flask 的 Web API 开发指南 - PyCon China 2019 上海 李辉](https://www.bilibili.com/video/av77591259?p=2) 分享的后半部分对相关 RESTFul API 的框架描述, 或见我的[技术调研](TODO)
>
> 选用: `FastAPI`, 原因:
>
> - 开发效率提升(积极的 Type Hint 完美智能补全与自动校验, 提供灵活的方式来依赖注入)
> - 文档写的太好了 QAQ, 太适合学习了
> - ASGI 看上去挺赞, 并且兼容传统写法
> - 内部使用库 `starlette` 组织开发了 `Django RESTFul Framework`, 质量值得信赖
>
> 备用: `Django RESTFul Framework`
>
> - 仍未实际使用过, 暂时搁置

##### 该版本待实现事项：

- [ ] 用户鉴权:
  - [ ] 注册
  - [ ] 登录

#### Databases

暂时没选好, 其实目前也太不需要想, 暂时使用 `SQLite` 开发就好


# 总体参考[论文引用]

[时间管理 方法 - Sci-Hub文献检索](https://s2.sci-hub.org.cn/scholar?start=20&q=%E6%97%B6%E9%97%B4%E7%AE%A1%E7%90%86+%E6%96%B9%E6%B3%95&hl=zh-TW&as_sdt=0,5)

[PsycNET](https://psycnet.apa.org/fulltext/1994-39368-001.html)

[Time management - Wikipedia](https://en.wikipedia.org/wiki/Time_management)

[To-Do Lists Can Take More Time Than Doing, But That Isn't the Point - WSJ](https://www.wsj.com/articles/SB109460145618411891)

[时间管理 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E6%97%B6%E9%97%B4%E7%AE%A1%E7%90%86)

[Time Management | Penn State Learning](https://pennstatelearning.psu.edu/time-management)

[微服务 论文 - 搜索结果 - 知乎](https://www.zhihu.com/search?type=content&q=%E5%BE%AE%E6%9C%8D%E5%8A%A1%20%E8%AE%BA%E6%96%87)

[读思码--ShowDoc](https://www.showdoc.cc/note?page_id=1390467302230065)

[基于微服务架构的系统设计与开发--《南京邮电大学》2017年硕士论文](http://cdmd.cnki.com.cn/Article/CDMD-10293-1017859549.htm)

[大学生学习计划管理系统的开发研究--《第二军医大学》2012年硕士论文](http://cdmd.cnki.com.cn/Article/CDMD-90024-1012404732.htm)

[基于REST架构的web服务技术研究--《武汉理工大学》2013年硕士论文](http://cdmd.cnki.com.cn/Article/CDMD-10497-1013296405.htm)

[学位论文搜索结果_远见搜索](http://yuanjian.cnki.com.cn/cdmd/Search/index)

[研究生课余时间管理研究--《湖南大学》2013年硕士论文](http://cdmd.cnki.com.cn/Article/CDMD-10532-1014233258.htm)

[基于跨平台的移动应用开发框架研究--《北京交通大学》2014年硕士论文](http://cdmd.cnki.com.cn/Article/CDMD-10004-1014178267.htm)

[面向服务的业务流程建模与验证研究--《西安电子科技大学》2012年博士论文](http://cdmd.cnki.com.cn/Article/CDMD-10701-1013114286.htm)