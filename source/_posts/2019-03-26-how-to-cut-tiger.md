---
title: 图片切割脚本使用
date: 2019-03-26 21:46:06
tags: 
- 教程
---

环境要求：python3、PS（或其他能准确获取指定像素点的软件）
<!--more-->

1. 在待处理图片文件夹里新建一个`cut`的文件夹，里边放入一批拍摄角度、对象在图片的位置均相似的图片。Windows的多选是`Ctrl+Shoft+左键`，MacOS不明:simple_smile:
   {% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-1.png 新建cut文件夹 %}
   {% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-2.png 选中相似的图片 %}
2. 在脚本的最上方填入“待处理图片的路径”和“输出图片的路径”，如：
{% code lang:python %}
# csv保存路径
csv_path = r'D:\Users\Teemo Nicolas\Downloads\002\\'
# 待处理图片路径
img_path = r'D:\Users\Teemo Nicolas\Downloads\002\right\cut\\'
# 新文件写入路径
new_img_path = r'D:\Users\Teemo Nicolas\Downloads\02\right\\'
{% endcode %}
其中，csv是图片处理记录的数据，没什么重要性，选填，但是执行脚本的时候需要输入“n”或直接把这段功能的代码注释掉掉。

3. 在PS里获取信息。

打开图片后，用矩形选框工具选好位置，其长宽比可固定为3:2；右键单击选框，选择“变换选区”，然后在“信息面板”查看该矩形选框的信息（左上角坐标：X、Y；选框长宽：W、H），将这四个数填入脚本下方对应位置。
{% code lang:python %}
# 起始点坐标，PhotoShop获得
start_x = 459
start_y = 231
# 切割尺寸，PhotoShop获得
crop_length = 2649
crop_height = 1766
{% endcode %}
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-3.jpg 变换选区 %}
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-4.png 查看选框信息 %}
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-5.jpg 信息面板 %}

4. 执行代码。
首先，脚本会对cut文件夹下中间的那张图片做测试，因为预览图中图片的方向并不一定是其真实方向，可能预览图中老虎头朝上，而文件信息中的老虎是头朝下的，就会出现错误。一般而言，将图片横向放置不会有错。如果测试图片和预期不一致，输入“n”退出程序，然后选一张图片调整为正确的方向重新获取XYWH执行脚本

确认无误后，回车继续，新文件将会保存到`new_img_path`指定位置（该文件夹必须存在）。
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-6.png 输出测试图 %}
{% img https://github-pages-1253649638.cos.ap-beijing.myqcloud.com/post-images/2019/2019-03-26-cut-tiger-7.png 结果示例 %}
