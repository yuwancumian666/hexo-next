---
layout: post
title: Python 第三方库（持续更新）
subtitle: 哈哈哈
date: 2018-03-08 00:00:00 +0800
description: python 的第三方库以及介绍
categories:
- Python
tags: [Python] 
---

{% blockquote 泰戈尔, 飞鸟集 %}
He who wants to do good knocks at the gate; he who loves finds the gate open.
	那些想做好人的，在门外敲着门，那爱人的，看见们敞着。——《飞鸟集》
{% endblockquote %}

<!-- more -->
	
### 爬虫类 (8)

|        库名        |                                                              作用                                                               |
| :----------------: | :-----------------------------------------------------------------------------------------------------------------------------: |
|   urllib/urllib2   |                                              Python 标准库，提供了大部分 HTTP 功能                                              |
|      requests      |                                                    功能强大的 HTTP 客户端库                                                     |
| bs4：beautifulsoup |                                           HTML 或 XML 文档处理工具，现已整合到 bs4 中                                           |
|        lxml        |                  HTML 和 XML 文档处理工具，速度快，需了解 xpath 语法；可以作为 BeautifulSoup 处理文档时的引擎                   |
|      html5lib      | HTML 和 XML 文档处理工具，几个解析工具的<a href="http://blog.csdn.net/fly_yr/article/details/51553587" target="_blank">比较</a> |
|      selenium      |                        自动化测试工具，适用于动态爬虫，需配合浏览器（例如 phantomjs，无界面浏览器）使用                         |
|       scrapy       |                                                         著名的爬虫框架                                                          |

### 科学计算及图像处理 (6)

|    库名     |                        作用                        |
| :---------: | :------------------------------------------------: |
| matplotlib  |           Python 的 2D绘图库，也支持 3D            |
|    numpy    |       科学计算工具：矩阵、函数、精密运算等；       |
|   pandas    | 基于 numpy，提供了大量的解决数据分析任务所需的工具 |
|    scipy    |         高级的科学计算库，和Numpy联系密切          |
| pillow：PIL |               具有强大的图像处理能力               |
| opencv：CV2 |    一个C++库，用于实时处理计算机视觉方面的问题     |

### 深度学习 (4)

|      库名      |                            作用                            |
| :------------: | :--------------------------------------------------------: |
|   tensorflow   |             膜拜谷歌大佬；有GPU版，需安装 CUDA             |
|  scikit-learn  | 基于NumPy, SciPy, Matplotlib的开源机器学习工具包（没用过） |
| caffee/caffee2 |                  常用于图像分类（没用过）                  |

### 网络编程 (4)

|      库名      |                       作用                       |
| :------------: | :----------------------------------------------: |
|     socket     | 套接字，可以访问底层操作系统Socket接口的全部方法 |
|  socketServer  |   高级别网络服务模块，可以简化网络服务器的开发   |
| smtplib、email |           封装了 SMTP 协议的邮件客户端           |

### WEB 框架 (3，不了解)

|      库名      |              作用               |
| :------------: | :-----------------------------: |
|      web       |         很简单的web框架         |
|     Flask      |           轻量级框架            |
|     Djando     |      全能型框架（没用过）       |
| 最简单的服务器 | python -m SimpleHTTPServer 8080 |

### 其他(28)

|      库名       |                       作用                        |
| :-------------: | :-----------------------------------------------: |
|       pip       |          Python 标准库，第三方库安装工具          |
|       os        |         Python 标准库，文件、目录操作工具         |
|       sys       |          Python 标准库，python 系统工具           |
|       re        |           Python 标准库，正则表达式工具           |
|      wget       |    linux-wget 命令的移植版，功能强大的下载工具    |
|     you-get     |          用于从 web 上下载媒体，支持油管          |
|  itchat、wxpy   |    微信机器人，提供了一系列操作微信聊天的接口     |
|      jieba      |                     中文分词                      |
|    markdown     | 将 markdown 格式的文档转化为结构化的xhtml 或 html |
|    PyQRCode     |                   二维码相关库                    |
|    wordcloud    |                     生成词云                      |
|    traceback    |                  代码debug 工具                   |
| time、datetime  |              Python 标准库，时间处理              |
| python-dateutil |                  时间处理工具包                   |
|     pywin32     |         提供了 python 操作 Windows 的接口         |
|     pyhook      |     基于pywin32；钩子，用来监听鼠标和键盘事件     |
|     PyYAML      |             生成、解析 YAML 配置文件              |
|    pdfminer     |                 pdf工具（没用过）                 |
|   pyinstaller   |        可以将 python 打包成 exe 可执行文件        |
|     zipfile     |                zip 压缩包处理工具                 |
|    optparse     |            主要用来为脚本传递命令参数             |
|     pygame      |                   游戏制作工具                    |
|   collections   |       Python 标准库，提供了许多有用的集合类       |
|     Tkinter     |              GUI （图形界面）开发库               |
|      json       |               编码和解码 JSON 对象                |
|     base64      |                    base64编码                     |

