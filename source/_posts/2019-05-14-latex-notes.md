---
title: Latex自定义设置
date: 2019-05-14 10:39:29
categories:
- LaTex
tags:
- Latex
- 笔记
mathjax: true
---

$\LaTex$论文写作Tip全记录

<!-- more -->

# Latex格式

## 页面尺寸
``` latex
\usepackage{geometry}
\geometry{a4paper, left=2.4cm, top=2.4cm, right=2.4cm, bottom=2.4cm}  % 页边距
```

## 页眉页脚
L、C、R分别表示左、中、右；E、O表示奇偶页，页眉页脚的设置中可以使用它们的组合，多选项的情况用中括号分开。
现在有几个问题：
1. 页眉需要的样式是：奇数页居中显示章节号，偶数页显示“东北林业大学本科毕业论文”，但是通过[CE]、[CO]设置就不行，而且只设置`\fancyhead[CE]{\song\xiaowu{东北林业大学本科毕业论文}}`也会失败，什么都不显示。
2. 双线页眉的长度一开始是`\headwidth`，右侧没有达到文档宽度的位置。改为`\columnwidth`或`\textwidth`之后，长度虽然改变了，但是文字的位置没有随之向右移动（没有居中）
3. 问题1中的章节号不知道怎么获取……
``` latex
\usepackage{fancyhdr}

%------- 页眉页脚样式 -------%
\pagestyle{fancy}
\fancyhf{}  % 清空设置
\fancyhead[C]{\song\xiaowu{东北林业大学本科毕业论文}}
% \fancyhead[CO]{\thechapter}
\fancyfoot[C]{\xiaowu{-\thepage-}}
\renewcommand{\headrulewidth}{0.4pt}

%------- 双线页眉的设置 -------%
\makeatletter %双线页眉
\def\headrule{{\if@fancyplain\let\headrulewidth\plainheadrulewidth\fi%
\hrule\@height 1.0pt \@width\columnwidth\vskip1pt%上面线为1pt粗
\hrule\@height 0.5pt\@width\columnwidth  %下面0.5pt粗
\vskip-2\headrulewidth\vskip-1pt}      %两条线的距离1pt
  \vspace{6mm}}     %双线与下面正文之间的垂直间距
\makeatother
```

## 并排图片

``` latex
\begin{figure}[htbp]
    \centering %图片全局居中
    \subfigure[原图]{
      \includegraphics[width=0.2\textwidth]{resource/2-原图.jpg}
    }
    \subfigure[互相关]{
      \includegraphics[width=0.2\textwidth]{resource/2-互相关.jpg}
    }
    \subfigure[卷积]{
      \includegraphics[width=0.2\textwidth]{resource/2-卷积.jpg}
    }
    \caption{卷积核的翻转对特征提取的影响}
    \label{Figure.Second.1}
  \end{figure}
```
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-05-14-%E5%A4%9A%E5%9B%BE.jpg 图片并排显示 %}

# Latex样式

## 图片标题的样式
把图片标题默认的“图1:示例”更改为“图2-1 示例”。
其中：
- thesection{} 表示章节号
- 两个命令分别设置表格和插图的格式
- 命令中的“-”可以用“.”等符号代替，以适应不同的要求
``` latex
\renewcommand {\thetable} {\thesection{}-\arabic{table}} 
\renewcommand {\thefigure} {\thesection{}-\arabic{figure}}
\captionsetup{labelformat=default,labelsep=space} %去除冒号
```

## 公式引用输出样式

``` latex
\renewcommand\theequation{\arabic{section}-\arabic{equation}} % 公式引用输出样式

\begin{equation}
    (\ref{Formula.Second.1}) \Leftrightarrow S(i,j)=(K*I)(i,j)=\sum_m \sum_n I(i-m,j-n)K(m,n)\label{Formula.Second.3}
\end{equation}
(\ref{Formula.Second.3})式也被称为I和K的互相关
```
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-05-14-%E5%85%AC%E5%BC%8F%E7%BC%96%E5%8F%B7.jpg 公式的编号与引用 %}
