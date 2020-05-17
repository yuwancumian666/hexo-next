---
layout: post
title: Scala 函数
subtitle: 爱哭的嘎达傻空了大概看到过
date: 2018-03-18 00:00:00 +0800
categories:
- Scala
tags: [Scala, Spark] 
---

{% blockquote 泰戈尔, 飞鸟集 %}
	The sadness of my soul is her bride's veil. It waits to be lifted in the night. 
	我灵魂里的忧郁就是她新婚的面纱。这面纱等候着在夜间卸去。
{% endblockquote %}
<!-- more -->

这里所写的重点是在 Scala 中出现的但在 Python 和其他正经语言中没有出现的语法。

### 纯函数

+ 有一个或多个输入参数
+ 只使用输入参数完成运算
+ 返回一个值
+ 对于相同的输入总返回相同的值
+ 不使用或影响函数之外的任何数据
+ 不受函数之外的任何数据的影响

### 无参函数

最基本的 Scala 函数是表达式的一个命名包装器，如果需要一个函数来格式化当前数据，检查一个远程服务是否提供了新数据，或者只是要返回一个固定的值，就可以采用这个格式。

*注意：*括号可以加也可以不加，调用时亦然。但是如果定义函数时没加括号，调用时也不能加括号。

``` scala
def fun1 = "Hello World!"
def fun2 : String = "Hello World!"
def fun2() : String = "Hello World!"
```


### 定义函数的几种方法

Scala 的函数会把函数体的最后一个表达式的值作为函数的返回值返回，而有些情况可能在函数结束前返回一个值，用 **return** 关键字即可

``` scala
def add(x:Int, y:Int) : Int = {
    x + y
}
def Fibo(n:Int) : Long = {
    if (n==1 | n==2) return 1
	Fibo(n-1) + Fibo(n-2)
}
```

### 表达式块调用函数

表达式块调用函数就是利用一个表达式块的返回值调用函数

``` scala
Fibo{val n=2;2*3}
```

### 尾递归

@annotation.tailrec
节省栈空间

### 嵌套函数

``` scala
def max(a:Int, b:Int, c:Int) = {
    def max(x:Int, y:Int) = {
	    if (x > y) x else y
	}
	max (a, maax(b, c))
}
// -------------------------------
def info (name:String, age:Int) = {
    println(s"name:$name, age:$age")
}
info("tom, 1")
// 或
def info (name:String="tom", age:Int) = {
    println(s"name:$name, age:$age")
}
info(name="tom", age=1)
```

