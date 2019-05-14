---
title: Electron-Vue遇到的诸多问题
date: 2019-03-26 00:42:32
category: 
- [Node.js]
- [Electron]
tags: 
- 问题
- Electron-Vue
---

由于个人水平原因遇到的解决不了或已经解决的问题。

<!--more-->

# Electron & Vue

## ipcRenderer.send()函数不能工作-2019/03/26
Console里的错误描述：
{% note danger %}
[Vue warn]: Error in v-on handler: "TypeError: electron__WEBPACK_IMPORTED_MODULE_3___default.a.send is not a function"
found in
---> <Gallery> at src/renderer/components/Gallery/Gallery.vue
       <MainPage> at src/renderer/components/MainPage.vue
         <ButerApp> at src/renderer/App.vue
           <Root>
TypeError: electron__WEBPACK_IMPORTED_MODULE_3___default.a.send is not a function
    at VueComponent.drop (Gallery.vue?f747:125)
    at drop (Gallery.vue?f24d:127)
    at invokeWithErrorHandling (vue.esm.js?a026:1863)
    at HTMLDivElement.invoker (vue.esm.js?a026:2188)
    at HTMLDivElement.original._wrapper (vue.esm.js?a026:7542)
{% endnote %}

该问题可能的原因是：在引入ipcRenderer的时候写成了`import ipcRenderer from 'electron'`，改成`const {ipcRenderer} = require('electron')`不再显示错误。

## ipcRenderer和ipcMain
ipcRenderer和ipcMain这两个类之间传递的数据是**object**格式，即使你在ipcRenderer里向ipcMain发送的是数组。只这么单向地说是因为在文件对话框里选择的文件经sender发送到ipcRenderer后，其object格式使用forEach不会报错。具体原因待研究。

## ipcRenderer.on重复执行（dialog）
问题描述：点击按钮打开对话框，选择文件并输出在屏幕上。第一次打开对话框选择一个图片，会有一个图片添加到视图上；再打开对话框选择一个或多个图片，会进来双倍相同的图片；接着再打开会有三倍，四倍……
这是个从一开始就令我脑壳痛的问题，来回测试代码就是找不到问题在哪，但是知道是在`ipcRenderer.on()`中反复执行的，之前存储数据的格式简单：数组可以去重，简单对象可以用图片的src做键，直接去掉重复的图片链接。而把数据存储到Vuex的store中之后，加上编辑页面的需要，数据结构变得复杂，变成了对象列表，这就不得不解决这个问题。后来还是在Stack Overflow中找到了[解决办法](https://stackoverflow.com/questions/52111151/node-on-method-firing-too-many-times)：把`ipcRenderer.on()`用`ipcRenderer.once()`替代，这是因为每一次点击按钮打开dialog都会设置一个监听器，多次打开就需要手动删除之前的监听器，这样子很麻烦，用`ipcRenderer.once()`就会在程序块执行结束后自行删除监听器。

## dialog选择文件夹会返回undefined
这是一个原因不明的问题，还没去StackOverflow上找找。现在的做法是直接过滤掉undefined的数据，目前没有很大的问题。


# Vue & Vuex

## Vue数据更新，视图不更新-2019/03/24
点击文件对话框可以添加图片，但是拖入就添加不了，vue的数据对象也更新了，可能是更新数据的方法有问题。参考[Vue中数组和对象更改后视图不刷新的问题](https://blog.csdn.net/zifeiyu130/article/details/78950244)
尝试了N种方法，仍然tmd解决不了，考虑添加初始化图片。

添加初始化图片仍然不能解决问题，情况是dom中有添加的卡片元素，就是在页面上没有显示。经过多次查找，在`.card-columns`的外层div上有一个`v-show='showTip'(showTip=false)`，而且在设计页面的时候多包上了一层div（具体记不太清楚了，应该是给功能扩展留出的空间）。最后解决的方式是：去掉了多余的div和`v-show=false`，重新写了一下gallery相关的样式，得以解决。

## 全局变量、函数-2019/03/26
谷歌了很多种注册全局变量、函数的方法，在我这里都行不通，可能是我个人水平的原因。
最后解决的方案是，将三代组件合并成父子两代组件，在父组件里声明大部分变量，然后通过`props`和`this.$emit()`方法在父子组件之间通信并同步变量解决了问题。

在使用`this.drag_tip_seen_flag = true;this.$emit('get_drag_tip_seen_flag', drag_tip_seen_flag)`向父组件传递更改过的`dragTipSeenFlag`变量的情况下，当点击`&times;`关闭选项卡的时候，Console会出现Vue的警告:
{% note danger %}
[Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "drag_tip_seen_flag"
[Vue warn]: Error in v-on handler: "ReferenceError: drag_tip_seen_flag is not defined"
found in......
{% endnote %}
意思是由于更改了变量而警告改变量可能会被覆盖，需要注意。在把该两行代码换成`this.$emit('get_drag_tip_seen_flag', true)`之后，警告消失。这里的解决方式只是个例，如果父子组件之间互相传递的变量比较多而引发该问题时，就需要考虑换一种方法了。（我是tmd再也不想接触vue的全局变量和全局函数了）

## Vuex state数据返回错误
在将数据移至Vuex后，发现从state中获取的bool数据不符合预期，总是返回错误的数据。只有在一开始初始化的时候才正确，更不用说更新这个state了。

## \[vuex\] [do not mutate vuex store state outside mutation handlers.](https://stackoverflow.com/questions/46044276/vuex-do-not-mutate-vuex-store-state-outside-mutation-handlers) 2019/04/07
意思是说不要在mutation之外更改state中变量的值，例如再actions中对state中某一变量赋值就会出现此错误。

# 界面布局

## card-columns布局-2019/03/23
图片少于4张的时候会显示两列（同理，少于两张会显示1列），这是因为页面设计的排版是面向列布局的，当图片大于4张的时候自动会占满3列。
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-23-card-columns-bug.jpg 似bug又不是bug %}

## 卡片阴影移位-2019/03/24
Bootstrap中.card-columns>card加CSS阴影后，card[1,2]和card[1,3]上方阴影被截取到前一列最下方。猜测时因为`.card-columns`的面向列排版，导致阴影被错位了。**解决方法**：在`.card`的CSS里加一个`margin: 8px;`，给卡片上方阴影留出空间即可。
{% img 	https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-24-card-columns-%E9%98%B4%E5%BD%B1%E7%A7%BB%E4%BD%8D.jpg 阴影移位 %}


# Node.js

## 奇怪的字符202A

在读取图片的测试过程中，由于路径字符串的问题，导致读取文件时路径被当成相对路径处理报错。当我把该字符串放到控制台处理时，用其作为路径执行会报“文件不存在”的错误。然后通过[`string.charCodeAt(0)`](https://www.fileformat.info/info/unicode/char/202a/index.htm)发现字符串的第一位出现了一个不常见的字符`8234`，16进制为`202AH`，谷歌了一下看着好像是一个控制字符，可能是我在文件属性的“安全选项卡”复制路径的时候多复制了一个字符，让重新用正确的路径字符串读取文件的时候，错误消失。

![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-27-fucking-char-1.jpg)
![](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-27-fucking-char-2.jpg)

当把该字符复制到js代码里时，编辑器里是看不到的，但是会报代码语法错误。