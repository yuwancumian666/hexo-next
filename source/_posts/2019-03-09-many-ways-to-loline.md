---
title: Loline —— 加载本地json
date: 2019-03-09 18:34:40
tags:
- Loline
- json
---

# 使用数据的几种方式

## RESTful API
这种方式在{% post_link loline 上一篇文章 %}中已经使用过。

在使用Ajax跨域请求json的方式下，遇到了两点麻烦：
1. 阿里云服务器上运行的python脚本有*不知名的问题*。
2. GitHub Pages的博客上需要使用HTTPS来跨域请求，这就需要一个SSl证书，但是自己的证书不会被浏览器信任，而去阿里云申请证书（有免费的）需要注册域名，太麻烦了，所以就改变一下请求json的方式，改用本地加载数据的方式。

<!-- more -->

## 加载本地json

{% note warning %}
注意`"/json/champions.json"`不能写成`"json/champions.json"`的形式，不然会在post页面显示404错误。
> http://localhost:4000/2019/03/08/loline/json/champions.json 404 (Not Found)
{% endnote %}

{% code lang:html next\layout\_scripts\commons.swig %}
<script type="text/javascript">
	$.get("/json/champions.json", function (data) {
		var ranint = function(min, max) {
    	return Math.round(Math.random() * (max - min)) + min;
		}(1, data.length);
		champion = data[ranint-1];
		$('#loline-content').css('display', '').text(champion.words);
		$('#loline-from').css('display', '').text('——' + champion.title_zh+' '+champion.name_zh);
	});
</script>
{% endcode %}

下边是相应的属性设置，但实际上和之前一言设置都差不多。
{% fold 点击查看 %}

{% code lang:html next\layout\_macro\sidebar.swig %}
<div class="sidebar-inner">
        <div>
          <blockquote class="blockquote-loline">
            <b><span style="color:burlywood;"><span id="loline-content"></span></span></b>
          </blockquote>
        </div>
        <div style="text-align: right; font-size: 0.8em; color: black;" id="loline-from"></div>
        <div style="margin-top: 15px; font-size: 0.8em; color: black;"><a href="https://yuwancumian666.github.io/2019/03/08/loline/#more">LOLine</a></div>
      </div>
      <div style="height: 15px"></div>
{% endcode %}
{% endfold %}

## 直链访问

可以以直链请求json的方式获取数据，数据源可以为博客所在的仓库。

这种方式返回的data数据类型为`string`，所以代码也有相应的更改。

{% code lang:javascript next\layout\_scripts\commons.swig %}
$.get("https://raw.githubusercontent.com/.../champions.json", function (data) {
    console.log('url: '+'{{ url }}');
		champions = JSON.parse(data);
		var ranint = function(min, max) {
    	return Math.round(Math.random() * (max - min)) + min;
		}(1, data.length);
		champion = champions[ranint-1];
		$('#loline-content').css('display', '').text(champion.words);
		$('#loline-from').css('display', '').text('——' + champion.title_zh+' '+champion.name_zh);
	});
{% endcode %}


# CSS——数据展示

模仿`block-quote`标签的样式，在侧边栏中加入`block-loline`，如此一来又出现了新问题：svg大小和颜色控制不好，便换回了原来的样子。

## blockquote-loline样式

{% fold 查看代码： %}

{% code lang:styl next\source\css\_common\components\tags\blockquote-center.styl %}
.blockquote-loline {
  position: relative;
  margin: 40px 0;
  padding: 0;
  border-left: none;
  text-align: center;

  &::before, &::after {
    position: absolute;
    content: ' ';
    display: block;
    width: 100%;
    height: 24px;
    opacity: 0.2;
    background-repeat: no-repeat;
    background-position: 0 -6px;
    background-size: 22px 22px;
  }
  &::before {
    top: -20px;
    background-image: url($sidebar-quote-left);
    border-top: 1px solid $grey-light;
  }
  &::after {
    bottom: -20px;
    background-image: url($sidebar-quote-right);
    border-bottom: 1px solid $grey-light;
    background-position: 100% 8px;
  }

  p, div { text-align: center; }
}
{% endcode %}
{% endfold %}

## 设置base变量

自定义了两个SVG，在`SVG: path`标签中可以加入`fill="#B2B7F2"`定义SVG的颜色。

在`next\source\css\_common\components\tags\blockquote-center.styl`中发现可用自定义变量，然后在下方文件中更改了以下原来的svg并新建了两个变量。

{% code lang:styl next\source\css\_variables\base.styl %}
// blockquote-loline icon 只是更改了一下颜色
$sidebar-quote-left = '../images/sidebar-quote-l.svg'
$sidebar-quote-right = '../images/sidebar-quote-r.svg'
{% endcode %}
