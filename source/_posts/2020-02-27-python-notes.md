---
title: Python 技巧
date: 2020-02-27 23:53:34
categories:
- Python
tags:
- 笔记
- 面试
---

这里记录了 Python 中不熟悉或者古怪的操作。🧐

<!-- more -->

# 字符串


## 二元运算

### 测试

非空字符串之间进行 `and` 运算，返回最后一个字符串，进行 `or` 运算返回首个字符串，但对 `True` 和 `False` 不适用🙅‍。

``` python 非空字符串之间
>>> 'str' and 'int'
'int'

>>> 'str' or 'int'
'str'
```
``` python 空与非空字符串
>>> 'str' and ''
''
>>> '' and 'str'
''
>>> 'str' or ''
'str'
>>> '' or 'str'
'str'
```

``` python 字符串与布尔值
# True
>>> True and 'str'
'str'
>>> 'str' and True
True

# False
>>> False and 'str'
False
>>> 'str' and False
False
```

### 且运算

列元素与行元素进行“且”运算，如：`'str' and 'int'`

``` python
|  and  | 'int'   ''    True   False |
---------------- ---------------------
| 'str' | 'int'   ''    True   False |
|  ''   |  ''     ''     ''     ''   |
| True  | 'int'   ''    True   False |
| False | False  False  False  False |
```

列元素与行元素行“且”运算，如：`'int' and 'str'`

``` python
|  and  | 'str'   ''    True   False |
--------------------------------------
| 'int' | 'str'   ''    True   False |
|  ''   |  ''     ''     ''     ''   |
| True  | 'str'   ''    True   False |
| False | False  False  False  False |
```

### 或运算

列元素与行元素进行“或”运算，如：`'str' or 'int'`

``` python
|  or   | 'int'   ''    True   False |
--------------------------------------
| 'str' | 'str'  'str'  'str'  'str' |
|  ''   | 'int'   ''    True   False |
| True  | True   True   True   True  |
| False | 'int'   ''    True   False |
```

列元素与行元素行“且”运算，如：`'int' or 'str'`

``` python
|  or   | 'str'   ''    True   False |
--------------------------------------
| 'int' | 'int'  'int'  'int'  'int' |
|  ''   | 'str'   ''    True   False |
| True  | True   True   True   True  |
| False | 'str'   ''    True   False |
```

## 多元运算

``` python


```


# 元组

## 拆包

{% codeblock 拆包 lang:python %}

{% endcodeblock %}


# 函数

## 匿名函数

匿名函数只能有一个表达式，不写return，表达式的结果就是返回值

``` python
f = lambda x: x*x
f()
```

## 闭包

外层函数引用了内层函数的变量（参数也算变量），然后返回内层函数的情况，称之为闭包（Closure）。

``` python
def outer(parms):
    def inner():
        return parms
```

## 装饰器

decorator 本质上是一个高阶函数，它接收一个函数作为参数，然后返回一个新函数。

``` python
def Log(f):
    print("call ", f.__name__)
    return f

# 装饰器"@Log"等价于 "func = Log(func)"
@Log
def func():
    print("Hello World!")

func()
# call  func
# Hello World!

# 如果需要在装饰器中传入参数，可以用闭包
def LOG(f):
    def flog(*args, **kwargs):
        print("call ", f.__name__)
        return f(*args)
    return flog


@LOG
def func():
    print("Hello World!")
```

# 面向对象

## 类属性和实例属性

如果更改某一实例的类属性，则只影响该实例，类和其他实例的类属性不受影响。
此操作实际上是给该实例添加了一个实例属性并为其赋值，访问该实例“类属性”的时候，实际上访问的是其“实例属性”
因为当实例属性和类属性重名时，实例属性优先级高，会屏蔽掉类属性的访问。

``` python 解释代码 https://www.imooc.com/code/6176 慕课网
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')
print 'Person.address = ' + Person.address
p1.address = 'China'
print 'p1.address = ' + p1.address
print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
"""
Output: 
Person.address = Earth
p1.address = China
Person.address = Earth
p2.address = Earth
"""
```

## isinstalce() & type()

isinstalce()用来判断一个对象和一个已知类型是否相同，考虑继承关系，会认为子类是一种父类类型，
而type()不考虑继承关系。

