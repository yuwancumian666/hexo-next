---
title: Electron-Vue开发笔记
date: 2019-03-23 02:54:43
category: 
- [Node.js]
- [Electron]
tags: 
- 前端
- Electron-Vue
- 笔记
---

对于Electron的了解，还是开始于[Motrix](https://motrix.app/)，一个颜值极高的多功能下载工具。在GitHub项目页面看到了“Electron”一词，从此开始了废寝忘食的学习过程……

<!-- more -->

从electron到electron-vue，不仅重拾了之前自学的Html、CSS、js，还扩展到了Node.js，还有Vue、Bootstrap等前端框架。虽然现在并不知道他们到底是用来干嘛的（Vue，我说谁呢自己心里去除），但也有个初步的了解了。

# 环境
{% note warning %}
欲练此功，必先自宫。
{% endnote %}

刚准备拿起书看计算机组成原理，就在知乎上看到有人推荐[Motrix](https://motrix.app/)这个东西，惊讶于颜值，了解项目的技术栈后，又感叹于技术。心里默默想着，这书怕是，看不成了。

# 抄代码

很多代码及代码风格都模仿自Motrix（羞羞:no_mouth:）

# 样式与排版

感觉好多种样式不对的情况都是没有刷新（瞎写定位）


# 打开对话框
打开对话框的尝试倒没有踩多少坑，看[electron文档](https://electronjs.org/docs/api/dialog)就可以handle。
## 注意
### 选择文件和文件夹-2019/03/26
在[对话框文档](https://electronjs.org/docs/api/dialog)中有这么一句：
{% note primary %}
在 Windows 和 Linux 上, 打开对话框不能同时是文件选择器和目录选择器,
因此如果在这些平台上将 properties 设置为["openFile"、"openDirectory"],
则将显示为目录选择器。
{% endnote %}
若对选择文件和文件夹都有需要，则应将它们分开处理。

### 文件夹-2019/03/26
在读取文件夹下的文件目录时，可以用`forEach`循环，因为`forEach`是同步的，即使没有`Sync`（详见该[博客](http://www.gimoo.net/t/1502/54e2acd26b263.html)）。在该循环内也建议使用同步函数，否则可能会遇到数据还没来得及传出来就返回的问题。当然，返回为空（或不全）。

# 小结

经过三天没日没夜地折腾，终于看到了一丝曙光。在bootstrap的加持下排版样式有了雏形，有了Vue的高级功能（没见过的都是高级），可以任意添加单个或多个图片了。

## 预览-2019/03/23

现在的界面就是酱紫：
+ 原生卡片（bootstrap中.card-columns的样式，加了自制页眉）
+ 自制卡片

两种样式看起来只差一个图片的margin，看起来大小不太一样。但是设计的时候走了很多弯路。
自制卡片没有使用.card-columns的时候图片的定位有问题：
1. 宽>高的时候图片不能居中
2. 高>宽的时候图片突破容器高度，向下伸出一大截。
使用.card-group和.card-decks的时候一张图片占了整个页面，问题太多了，而且自己写的CSS也一直在变，没有太大的可比性。现在能做成这样子已经巨jb开心了，感觉自己啥都tm会……

{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-23-card-columns-%E5%8E%9F%E7%94%9F%E5%8D%A1%E7%89%87%E6%A0%B7%E5%BC%8F.jpg 原生卡片样式 %}
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-23-card-columns-%E8%87%AA%E5%88%B6%E5%8D%A1%E7%89%87%E6%A0%B7%E5%BC%8F.jpg 自制卡片样式 %}
