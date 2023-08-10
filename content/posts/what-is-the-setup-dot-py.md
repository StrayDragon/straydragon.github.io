---

title: '"这个 setup.py 是什么?"'
tags:
- "Python3"
- "Python3::pip"
- "Python3::PyPI"
categories:
- "配置文件"
date: 2019-02-08T11:55:59+08:00
draft: false
---

> 如果你曾经浏览过某些 Python 模块的源码,
> 你会发现一般都会有一个名为**setup.py**的文件,那么这个文件是干啥的呢?

# 写在前面

- 最近,正在构思自己的命令行脚手架工具 **`dragon-cli`** 时遇到了这个问题,在学习使用 [click](https://click.palletsprojects.com/en/7.x/) 模块(一个好用方便的建立命令行工具的框架) 的[教程](https://www.youtube.com/watch?v=kNke39OZ2k0)中有一个配置**setup.py**的过程,我才发现一直对这个玩意熟视无睹,并且不明所以,在探索使用的过程,总结此文,方便以后查阅 O(∩_∩)O~

<!-- more -->

# 初步了解

- 简单来说,这个 **setup.py** 是用来帮助使用者安装 模块(Module)/包(Package) 的构建脚本.就像`pip`, `easy_install`, ... 做的那样 (!它们也是遵循着目标库中的 **setup.py** 而完成的安装).

- 在每个**setup.py**文件中,都可以看到其导入了 setuptools 这个包,并且从入口函数 `setup(...)` 传入配置参数, 看上去像这样:

```python
from setuptools import setup

setup(
    # 包名称
    name='foo',
    # 包版本
    version='1.0',
    # 需要打包的 Python 单文件列表
    py_modules=['foo'],
    # 安装时需要安装的依赖包
    install_requires=[
        'bar',
    ],
    # ...
)
```

- 通常可以在包源码根目录使用以下命令安装 (**注意 Python 的版本,推荐虚拟环境安装**)

```bash
python setup.py install
```

- 这样,对于库的用户来讲,并不太需要关注这个脚本干了些什么,如果没有安装失败,一切就安好.

  - 其实它是把该库安装到目标环境(包括虚拟环境)的 **site-packages/** 目录下.

- 不过,当我们从库用户转变为库作者,或者两者兼有时,那么明白其中的原理就成为解决问题的重要出路了.

# setup 接受参数

> Some values are treated as simple strings, some allow more logic.
>
> Type names used below:
>
> - `str` - simple string
> - `list-comma` - dangling list or string of comma-separated values
> - `list-semi` - dangling list or string of semicolon-separated values
> - `bool` - `True` is 1, yes, true
> - `dict` - list-comma where keys are separated from values by `=`
> - `section` - values are read from a dedicated (sub)section
>
> Special directives:
>
> - `attr:` - Value is read from a module attribute. `attr:` supports callables and iterables; unsupported types are cast using `str()`.
> - `file:` - Value is read from a list of files and then concatenated

- 元信息 (MetaData)

|            说明            |           指定参数            |  指定参数(别名)  |     接收类型      | 最低版本 |
| :------------------------: | :---------------------------: | :--------------: | :---------------: | :------: |
|           包名称           |             name              |                  |        str        |          |
|           包版本           |            version            |                  | attr:, file:, str |  39.2.0  |
|         包官网主页         |              url              |    home-page     |        str        |          |
|                            |         download_url          |   download-url   |        str        |          |
|          项目主页          |         project_urls          |                  |       dict        |  38.3.0  |
|            作者            |            author             |                  |        str        |          |
|       作者的邮箱地址       |         author_email          |   author-email   |        str        |          |
|           维护者           |          maintainer           |                  |        str        |          |
|      维护者的邮箱地址      |       maintainer_email        | maintainer-email |        str        |          |
|        所属分类列表        |          classifiers          |    classifier    | file:, list-comma |          |
|          授权信息          |            license            |                  |        str        |          |
|                            |         license_file          |                  |        str        |          |
|          简单描述          |          description          |     summary      |    file:, str     |          |
|          详细描述          |       long_description        | long-description |    file:, str     |          |
|                            | long_description_content_type |                  |        str        |  38.6.0  |
|         关键字列表         |           keywords            |                  |    list-comma     |          |
|     适用的软件平台列表     |           platforms           |     platform     |    list-comma     |          |
| 指定可以为哪些模块提供依赖 |           provides            |                  |    list-comma     |          |
|      指定依赖的其他包      |           requires            |                  |    list-comma     |          |
|                            |           obsoletes           |                  |    list-comma     |          |

- 选项(Option)

|                           说明                           |        指定参数         |              接收类型              |
| :------------------------------------------------------: | :---------------------: | :--------------------------------: |
|              不压缩包，而是以目录的形式安装              |        zip_safe         |                bool                |
|           指定运行 setup.py 文件本身所依赖的包           |     setup_requires      |             list-semi              |
|                  安装时需要安装的依赖包                  |    install_requires     |             list-semi              |
|          当前包的高级/额外特性需要依赖的分发包           |     extras_require      |              section               |
|                                                          |     python_requires     |                str                 |
|               动态发现服务和插件 ==TODO==                |      entry_points       |           file:, section           |
|                                                          |        use_2to3         |                bool                |
|                                                          |     use_2to3_fixers     |             list-comma             |
|                                                          | use_2to3_exclude_fixers |             list-comma             |
|                                                          |  convert_2to3_doctests  |             list-comma             |
|   指定可执行脚本,安装时脚本会被安装到系统 PATH 路径下    |         scripts         |             list-comma             |
|                                                          |     eager_resources     |             list-comma             |
|                                                          |    dependency_links     |             list-comma             |
|                                                          |      tests_require      |             list-semi              |
|    自动包含包内所有受版本控制(cvs/svn/git)的数据文件     |  include_package_data   |                bool                |
|  需要处理的包目录(通常为包含  `__init__.py`  的文件夹)   |        packages         | find:, find_namespace:, list-comma |
|          指定哪些目录下的文件被映射到哪个源码包          |       package_dir       |                dict                |
|                指定包内需要包含的数据文件                |      package_data       |              section               |
| 当 include_package_data 为 True 时该选项用于排除部分文件 |  exclude_package_data   |              section               |
|                                                          |   namespace_packages    |             list-comma             |
|               需要打包的 Python 单文件列表               |       py_modules        |             list-comma             |
|                                                          |       data_files        |                dict                |

# 常用功能

- 当使用 `python setup.py --help-commands` 时, 可以看到不少指令(在这里列举几个常用的指令)
  - 此外可以使用 `python setup.py <COMMAND> --help` 获取详细帮助

## 针对库用户:

| 命令                      | 命令描述                                                                   |
| ------------------------- | -------------------------------------------------------------------------- |
| `python setup.py build`   | 构建该项目所需文件并将生成物放在 **build/** 中                             |
| `python setup.py install` | 从 **build/** 中将所需文件安装到目标环境(虚拟环境)的 **site-packages/** 中 |
| `python setup.py clean`   | 清理从 build 命令下生成的临时文件                                          |

## 针对库开发者

### 包的上传,发布相关命令

| 命令                       | 命令描述                                                                                           |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| `python setup.py register` | !注册该项目(不推荐:http 未加密):[参考](https://segmentfault.com/a/1190000008663126#articleHeader6) |
| `python setup.py upload`   | 上传二进制文件到 PyPI                                                                              |

> 进阶: [发布你自己的轮子 - PyPI 打包上传实践](https://segmentfault.com/a/1190000008663126)

```python
from setuptools import setup

setup(
    name='dragon',
    version='0.0.1',
    py_modules=['dragon'],
    include_package_data=True,
    install_requires=[
        'click',
        'colorama',
    ],
    license='MIT',
    entry_points='''
        [console_scripts]
        dragon=dragon:cli
    ''',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3.7',
    ],
)

```

# 学习资源

|              | 介绍                                              | 链接                                                                                                                     |
| ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 参考模板     | **`requests`** 库作者,写给人类的 setup.py 指南 ;) | [kennethreitz/setup.py](https://github.com/kennethreitz/setup.py)                                                        |
| 详细教程(En) | 有关打包,分发 Python 包的相关教程                 | [The Hitchhiker's Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html) |

# 参考资料

- https://stackoverflow.com/questions/1471994/what-is-setup-py
- http://blog.konghy.cn/2018/04/29/setup-dot-py/
- https://setuptools.readthedocs.io/en/latest/setuptools.html
