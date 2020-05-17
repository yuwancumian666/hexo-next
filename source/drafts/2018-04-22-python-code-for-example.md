---
layout: post
title: Python代码示例
date: 2018-04-22 13:34:51 +0800
categories:
- Python
tags: 
- Python 
---

{% centerquote %} 在马晓剑老师课堂上讲的一节课所用的示例代码O(∩_∩)O😄 {% endcenterquote %}

<!-- more -->

### Python 示例

``` python
# 变量命名
i = 1
c = 'c'
string = "string"
# 循环
for i in range(1, 6):
    print(i)
# output:
# 1
# 2
# 3
# 4
# 5

# 切片
''' 
[s t r i n g]
[0 1 2 3 4 5]
切片原则是“含头不含尾”
可以切片的对象有列表、字符串等
''' 
string[:3]  # "str"
string[1:4]  # "tri"
string[3:]  # "ing"
``` 

### C语言

``` C
// 变量命名
int i = 1
char c = 'c'
char s[6] = {'s', 't', 'r', 'i', 'n', 'g'};
//循环
for (i = 1; i < 6; i++){
    printf("%d", i);
}
/*output:
1
2
3
4
5
*/
``` 

### TensorFlow 安装及查看

``` shell
# 安装
pip install tensorflow	# cpu版本
pip install tensorflow-gpu	# gpu 版本

# 查看
pip list
``` 
