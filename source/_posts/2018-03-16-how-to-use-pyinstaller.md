---
layout: post
title: Python pyinstaller的使用
subtitle: 哈哈哈
date: 2018-03-16 00:00:00 +0800
description: 把 python 脚本编译成 exe 文件，让没有安装 python 的同学也能运行你的脚本
categories:
- Python
tags: 
- Python
- pyinstaller
---


{% blockquote 泰戈尔, 飞鸟集 %}
	I think of others ages that floated upon the stream of life and love and death and are forgotten, and I feel the freedom of passing away.
	我想起了浮泛在生与爱与死的川流上的许多别的时代，以及这些时代之被遗忘，我便感觉到离开尘世的自由了。
{% endblockquote %}

<!-- more -->

### 概述

安装: `pip install pyinstaller` <br>
用法: `pyinstaller -options script.py`，等 pyinstaller 编译完成之后，目录里面就多出两个文件夹: build 和 dist，其中 dist 里面就是打包的二进制文件，build 里是编译过程生成的中间件（作用不明）

选项 | 作用
-w，--windowed，--noconsole | 窗体exe文件(Windows Only)
-c，--nowindowed，--console | 控制台exe文件(Windows Only)
-F，--onefile | 把脚本打包成一个独立文件，打包一时爽，打开花五秒
-o DIR，--out=DIR | 设置spec文件输出的目录，默认在PyInstaller同目录
--version-file=file_version_info.txt，-v file | 给程序添加版权信息，需要指定一个版本信息文件
--icon=ico.ico | 添加图标，必须是 ico 文件
--upx-dir | 压缩可执行程序

### 版权信息

在我的GitHub里有现成的版权信息文件: “file_version_info.txt”，修改后即可使用。
<a href="https://github.com/moeext/Python-Demo/tree/master/Fuck%20RedSpider" target="_blank">传送门</a><br>
利用 pyinstaller 内置的 grab_verson.py 或 pyi-grab_version.exe工具也可以自己获取其他 exe 文件的版权信息，修改后使用。

+ grab_version.py: 目录:“Python27\Lib\site-packages\PyInstaller\utils\cliutils”，用法: ```python grab_version.py exe-file``` 
+ pyi-grab_version.exe: 目录: “Python27\Scripts\pyi-grab_version.exe”，用法: ```pyi-grab_version exe-file version-file``` 
+ 举个栗子说明: exe-file（C:\Users\Sarmon\AppData\Local\GitHubDesktop\GitHubDesktop.exe），version-file（version.txt）
+ 版权信息文件中，#号起注释作用，如果生成的 version.txt 没有正确换行，在修改的时候需要注意正确区分注释与版权信息
