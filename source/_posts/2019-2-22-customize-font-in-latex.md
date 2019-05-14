---
layout: post
title: 在LaTex中使用自定义字体
date: 2019-02-22 00:00:00 +0800
description: 
categories:
- LaTex
tags: 
- LaTex
- 字体 
---

{% cq %} 挖坑 {% endcq %}

<!-- more -->

刚接触LaTex，不太了解编译运行方式，网上搜了好多种方法都一直报错。这个例子刚测试的时候还编译不了，据猜测原因应该是编译缓存未清理或导入宏包的问题。

## 定义代码段字体

下边是一种自定义字体的方法，来自[LaTeX技巧006：使用不同的英文字体](https://blog.csdn.net/ProgramChangesWorld/article/details/51502730)

``` latex
\documentclass[UTF8]{article}
\usepackage{fontspec}
\setmainfont{Times New Roman}%fontspec下这个命令设置全局默认字体
\begin{document}
Hello World!\\
%这也是一种调用方式，无须fontspec宏包
\font\rm="Calibri" at 14pt \rm This is Calibri\\
\font\rm="Candara" at 14pt \rm This is Candara\\
\font\rm="Mistral" at 14pt \rm This is Mistral\\
\font\rm="Bahnschrift" at 14pt \rm This is Bahnschrift\\
\font\rm="Pristina" at 14pt \rm This is Pristina\\
\font\rm="Microsoft Uighur" at 14pt \rm This is Microsoft Uighur\\
\font\rm="Bradley Hand ITC" at 14pt \rm This is Bradley Hand ITC\\
\font\rm="Nirmala UI" at 14pt \rm This is Nirmala UI\\
\font\rm="CCBackBeat" at 14pt \rm This is CCBackBeat\\
\font\rm="Supercell-Magic" \rm This is Supercell-Magic\\
\font\rm="Supercell-Magic" at 14pt \rm This is Supercell-Magic\\
\font\rm="Supercell-Magic" at 18pt \rm This is Supercell-Magic\\
\end{document}
``` 

显示结果

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-02-22%20-fonts.jpg) 

## 设置全局（自定义）字体

第二天在测试中发现，用如下代码也能实现同样的效果，现在猜测是刚安装的字体VSCode或XeLaTex识别不了的问题。

``` latex
\documentclass[UTF8]{article}
\usepackage{ctex}
\usepackage{fontspec}
\usepackage{metalogo}
\usepackage{amsmath}
\usepackage{newtxtt, newtxmath}

\setmainfont{CCBackBeat} %英文字体
\setCJKmainfont{DengXian} % 中文字体

\title{论文测试}
\author{Teemo}
\date{2019年2月22日}
\begin{document}
\maketitle
\tableofcontents
\section{输出测试}
 Hello \XeLaTeX.
 Body of the article.
 second not sure \\
 fuck LaTex \\
 换行试试？\LaTeX，WithTab Icon,How to add a command \\

 换行
``` 

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-02-23-font-test-143421.jpg)
