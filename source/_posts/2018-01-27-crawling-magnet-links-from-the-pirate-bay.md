---
layout: post
title: Python 爬取磁力链
date: 2018-01-27 00:00:00 +0800
categories:
- Python
tags: [Python, 爬虫] 
---

{% blockquote 泰戈尔, 飞鸟集 %}
The mystery of creation is like the darkness of night------it is great. Delusions of knowledge are like the fog of the morning. 
	创造的神秘，有如夜间的黑暗，——是伟大的。而知识的幻影，不过是晨间之雾。
{% endblockquote %}

<!-- more -->

### 海盗湾简介

大名鼎鼎的[**海盗湾**](https://thepiratebay.cd/ "The Pirate Bay")，号称是全银河系最大的 BitTorrent 服务器，拥有数百万资源。是一个专门存储、分类及搜索 BitTorrent 种子文件的  *反版权*  网站，现今大多资源的提供形式为磁力链 (Magnet)。

![main page](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-27-the-pirate-bay-1.png)
![search page](https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2018-01-27-the-pirate-bay-2.png)

### 设计思想

直接构造搜索页面的 url，把要查询的关键字替换掉浏览器查询的关键字，并借此发送请求。由于该网站构造比较简单，可以在搜索界面直接分析，找出磁力链接并进行翻页。

### 代码

**使用注意：**要搜索的内容需要写到 name_list （列表）里，作为变量传到 main() 模块里。

代码为了美观已将制表符替换为四个空格（页面制表符默认显示8个空格）。

**用到的模块**
{% code lang:python %}
import os
import re
import time
import random
import urlparse
import urllib2 as ulb
from     4 import BeautifulSoup as     


'''
该模块接受要下载的url、用户代理（默认‘wswp’）、
代理服务器（默认为空）和重新尝试次数（默认为2），
返回该网页的内容和搜索内容的最大页数（只在第一次返回）。
'''
def download(url, user_agent='wswp', proxy=None, num_retries=2):
    print ("Downloading: " + url)
    headers = {'User-agent': user_agent}
    request = ulb.Request(url, headers=headers)
    opener = ulb.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(ulb.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except ulb.URLError as e:
        print ("Download Error:" + e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    if url[-4] == '0':
        soup =     (html, "html5lib")
        max_href_index = int(soup.find('div',align="center").contents[-4].string) - 1
        return html, max_href_index
    else:
        return html


# 根据给定的网页内容，转化为 BeautifulSoup 文档对象，搜索磁力链节点并以列表形式返回
def get_links(html):
    soup =     (html, "html5lib")
    list = soup.find_all('a', href=re.compile(r'^magnet'))
    return list


# 创建一个以关键字命名的文本文件，将下载的磁力链依次写入并保存。
def main(name_list):    
    for name in name_list:
        page = 0
        f = open(name+'.txt','a')
        magnet_num = 0
        while True:
            url = "http://thepiratebay.cd/search/" + name +"/" + str(page) + "/7/"
            if page == 0:
                html, max_page_index = download(url)
            else:
                html = download(url)
            magnet_list = get_links(html)
            for magnet in magnet_list:
                f.write(magnet['href']+'\n')
                magnet_num += 1
            if page < max_page_index:
                page += 1
                print(r"Sleep for one second...")
                time.sleep(random.random()*2)
            else:
                break
        print("From "+name+" get "+str(magnet_num)+" magnets")
        f.flush()
        f.close()
        os.rename(name+'.txt',name+'-'+str(magnet_num)+'.txt')
{% endcode %} 

**总结**

移步[Github](https://github.com/moeext/Spiders/tree/master/PirateBay)看代码，有惊喜

这好像是第一次比较正式的爬虫，代码比较 low，好在能用么么哒(づ￣ 3￣)づ
