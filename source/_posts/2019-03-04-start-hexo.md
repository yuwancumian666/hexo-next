---
title: GitHub Pages——Hexo配置笔记
date: 2019-03-04 20:29:12
category:
- Hexo
tags: 
- 笔记
- Hexo
- NexT
comments: true
---

{% cq %} Hello Hexo! {% endcq %}

<!-- more -->

# 填坑

## Markdown中不能使用变量

`Ruby-Jekyll`环境下，是可以直接在markdown中插入yaml中定义的变量的，所以就可以把OSS(COS)存储的图片链接放到yaml里，方便管理。从Jekyll转到Hexo发现在markdown中使用变量是行不通的，但是知道了半点解决办法——注册插件：[GitHub](https://github.com/hexojs/hexo/issues/2756)和[知乎](https://www.zhihu.com/question/264598381)的解决方案。在此方案下我做了一些不完全的测试：
1. 在`source/_data`目录下新建文件夹并有序存放yaml文件，在`hexo generate`过程中是找不到yaml文件的。
2. 把yaml放在根目录下，能找到文件，但是找不到变量的键，1中也会有此种情况。
3. 直接把数据放在`站点配置文件`中，可用找到变量并引用其值，但是只能硬编码，不能动态地找到变量，因为js中的变量类型是字符串

{% codeblock lang:javascript themes/next/scripts/include-variable.js %}
hexo.extend.tag.register('variable', function(args) {
    // 这里 传入的变量 args[0] 类型是字符串，所以不能和 js 语句相连接，如：hexo.config.data.args[0]
    // `hexo g`过程中打印下列信息，也就是执行该文件
    console.log("------------------variable---------------------");
    console.log(args[0])
    console.log(hexo.config.url)
    console.log(hexo.config.data.iOS)
    // return `img src="` + args[0] + `" /`;
    return ``+hexo.config.data.iOS;
  });
{% endcodeblock %}

## 关于代码块附加说明的样式

在代码高亮主题`night bright` 下，使用`{% raw %}{% codeblock %} {% endcodeblock %}{% endraw %}`添加说明后，页面显示字体颜色和背景相近，不容易分辨，可以更改css样式来解决这一问题：

{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-05-codeblock-caption.jpg 540 280 %}

{% codeblock lang:styl public/css/main.css %}
if $highlight_theme == "night bright"
  $highlight-background   = #000000
  $highlight-current-line = #2a2a2a
  $highlight-selection    = #424242
  $highlight-foreground   = #555  /* #eaeaea */
  $highlight-comment      = #969896
  $highlight-red          = #d54e53
  // ……
{% endcodeblock %}


# 配置与美化


## 图片并排

Hexo默认情况下是不能让图片并排显示的，这里需要更改一下设置，将下方代码块的两行注释掉即可。
Markdown中的语法`{% raw %}{% gp 1-n %} {% endgp %}{% endraw %}`，n代表需要并排的图片个数。

{% note warning %}
不可在行内使用单反引号引用标签插件，否则会被hexo理解为插入标签。
{% endnote %}

{% codeblock lang:javascript next/source/css/_common/components/tags/group-pictures.styl %}
.page-post-detail .post-body .group-picture-column {
  // float: none;
  margin-top: 10px;
  // width: auto !important;
  img { margin: 0 auto; }
}
{% endcodeblock %}

当图片设置为并排显示以后，不能使用"fancybox"的预览功能，要在另一个文件中注释掉一句代码：

{% codeblock lang:javascript themes/next/source/js/src/utils.js %}
wrapImageWithFancyBox: function() {
    $('.content img')
      .not(':hidden')
      // .not('.group-picture img, .post-gallery img')
      .each(function() {
{% endcodeblock %}

## 一言

来自这里：[ouuan](https://ouuan.github.io/hexo博客搭建指北/#一言（ヒトコト）)

1. 在代码所示文件中找到这一字段：`<aside id="sidebar" class="sidebar">`，然后在下边粘贴。
{% code lang:html themes/next/layout/_macro/sidebar.swig %}
<!-- 
<aside id="sidebar" class="sidebar">
 -->
<!-- 一言 start -->
<div class="sidebar-inner">
    <div>
        <div style="display: table-cell;vertical-align: top; color:#B2B7F2;font-size:24px;font-family:'Times New Roman',serif;font-weight:bold;text-align:left;">“</div>
        <div style="display: table-cell;text-align: left; vertical-align: middle; text-indent: 2em; padding: 0.8em 0.2em 1em 0.2em"><b><span style="color:burlywood;"><span id="hitokoto-content"></span></span></b></div>
        <div style="display: table-cell; vertical-align: bottom; color:#B2B7F2;font-size:24px;font-family:'Times New Roman',serif;font-weight:bold;text-align:left;">”</div>
    </div>
    <div style="text-align: right; font-size: 0.8em; color: black;" id="hitokoto-from"></div>
    <div style="margin-top: 15px; font-size: 0.8em; color: black;"><a href="https://hitokoto.cn/">Hitokoto</a></div>
</div>
<div style="height: 15px"></div>
<!-- 一言 end -->
{% endcode %}

1. 
{% code lang:html themes/next/layout/_scripts/commons.swig %}
<script type="text/javascript">
    $.get('https://v1.hitokoto.cn/?c=a', function (data) {
        $('#hitokoto-content').css('display', '').text(data.hitokoto);
        $('#hitokoto-from').css('display', '').text('——' + data.from);
    });
</script>
{% endcode%}

3. 
{% code lang:styl themes/next/source/css/_custom/custom.styl %}
.sidebar {
    background: rgba(0, 0, 0, 0);
}
{% endcode %}

## 折叠块功能

详细内容请见该[链接](https://www.cnblogs.com/woshimrf/p/hexo-fold-block.html)

{% fold 所涉及到的文件： %}
+ themes\next\scripts\tags.js
+ themes\next\scripts\fold.js
+ themes\next\source\js\src\post-details.js
+ themes\next\source\css\_custom\custom.styl
{% endfold %}

## 网页背景

在[这里](https://yltx.cf/2019/01/18/%E5%8D%9A%E5%AE%A2%E6%90%AD%E5%BB%BA%E9%A3%9F%E7%94%A8%E6%8C%87%E5%8C%97/#%E5%8D%9A%E5%AE%A2%E8%83%8C%E6%99%AF)学到的背景图设置，看到其博客效果后向朋友学习了[如何去掉文章背景](#文章背景)。

设置网页背景及文章透明度
{% code lang:css themes/next/source/css/_custom/custom.styl %}
body {
    background-image:url(/images/background/20180830_040329207_iOS.jpg);
    background-repeat: no-repeat;  //
    background-attachment:fixed;  // 背景图不滚动
    background-size: cover;
}
.main-inner {
    opacity: 0.8;  // 文章透明度
}
{% endcode %}

## 文章背景

去除背景只需要把该元素的`background`属性注释掉即可。

{% note warning %}
使用深色背景会造成博客阅读困难
{% endnote %}

1. 文章及文章预览

{% code lang:css themes/next/source/css/_schemes/Pisces/_layout.styl%}
.content-wrap {
  float: right;
  box-sizing: border-box;
  padding: $content-desktop-padding;
  width: $content-wrap;
  // background: white;
  min-height: 700px;
  box-shadow: $box-shadow-inner;
  border-radius: $border-radius-inner;
  // ……
  }
{% endcode %}

2. 阅读全文按钮

{% code lang:css themes/next/source/css/_common/components/buttons.styl %}
.btn {
  display: inline-block;
  padding: 0 20px;
  font-size: $btn-default-font-size;
  color: $btn-default-color;
  // background: $btn-default-bg;
  border: $btn-default-border-width solid $btn-default-border-color;
  text-decoration: none;
  border-radius: $btn-default-radius;
  transition-property: background-color;
  the-transition();
  line-height: 2;
  // ……
}
{% endcode %}

## jemoji
给Hexo添加对表情的支持，使用的是[Github Emojis API](https://api.github.com/emojis)
### 安装
`$ npm install hexo-filter-github-emojis --save`
### 选项
在Hexo配置文件`_config.yml`中添加默认设置：
``` yaml
githubEmojis:
  enable: true
  className: github-emoji
  inject: true
  styles:
  customEmojis:
```
{% note info %}
如果对`::`添加表情的方式不感冒，可以尝试使用`{% raw %}{% github_emoji sparkles %}{% endraw %}`方式添加表情:tada:
{% endnote %}

{% note info %}
在front-matter中添加`no-emoji: true`可以禁用`::`的渲染，但`{% raw %}{% github_emoji sparkles %}{% endraw %}`不会被禁用{% github_emoji sparkles %}
{% endnote %}

# 标签插件

## bootstrap note

使用方式
`{% raw %}{% note class_name %} Content (md partial supported) {% endnote %}{% endraw %}`

{% note default %} default {% endnote %}
{% note primary %} primary {% endnote %}
{% note success %} success {% endnote %}
{% note info %} info {% endnote %}
{% note warning %} warning {% endnote %}
{% note danger %} danger {% endnote %}

{% note info %}
bootstrap note2
--------------
里边加了分割线`-------`的话，匿名分割线上方的一行会变成同级标题
{% endnote %}
## Gist

`{% raw %}{% gist gist_id file_name %}{% endraw %}`

{% fold 点击查看gist %}
网络原因打不开gist
<% gist 19169c91a19ab7580e4678e4ed25375f extensions.json %>
{% endfold %}

## swig标签

{% raw %}{% raw %}
content
{% endraw %}{% endraw %}



# 接下来



## 浮动插入图片，[像这个](https://notes.iissnan.com/2016/next-documentations-reload/#前季剧情回顾)

## 无法访问404
只能以`localhost:4000/404.html`的方式访问

## 本页侧边栏
滑到最上方，然后向右看:point_right:
