---
layout: post
title: Shell 编程基础
date: 2018-01-06 00:00:00 +0300
categories:
- Linux
tags: [Linux, Shell] # add tag
---


{% blockquote 威廉·莎士比亚 %}
The time of life is short; to spend that shortness basely, it would be too long. 
	人生短暂，若虚度年华，则短暂的人生就太长了。
{% endblockquote %}

<!-- more -->

### Shell 介绍

Shell本身是一种用C语言编写的程序，从用户的角度来看，Shell是用户与Linux操作系统沟通的桥梁。用户既可以输入命令执行，又可以利用 Shell脚本编程，完成更加复杂的操作。在Linux GUI日益完善的今天，在系统管理等领域，Shell编程仍然起着不可忽视的作用。深入地了解和熟练地掌握Shell编程，是每一个Linux用户的必修课。
<br>Linux的Shell种类众多，常见的有：Bourne Shell（/usr/bin/sh或/bin/sh）、Bourne Again Shell--Bash（/bin/bash）、C Shell（/usr/bin/csh）等等。每种Shell都有其特点，基本上，掌握其中一种就足够了。
在本文中，我们使用的Shell版本是Bash，由于易用和免费，Bash在日常工作中被广泛使用；同时，Bash也是大多数Linux系统默认的Shell。

### Shell 基本格式

利用vi/vim等文本编辑器编写 Shell 脚本的固定格式如下：<br>

``` shell
#!/bin/sh
#comments
```

首行中的符号#!告诉系统其后路径所指定的程序即是解释此脚本文件的Shell程序。如果首行没有这句话，在执行脚本文件的时候，将会出现错误。
后续的部分就是主程序，除第一行外，以#开头的行就是注释行，直到此行的结束。如果一行空间不够，可以在行尾加 " ，这个符号表明下一行与此行会合并为同一行。
<br>
编辑完毕后，将脚本存盘为 `filename.sh`，运行前首先将文件属性设为可执行：

``` shell
chmod +x filename.sh
./finename.sh  #本行代码执行脚本
```

### Hello World

新学习一门语言的第一步大抵就是 Hello World 了吧，和 C 语言、Java 等不同，Shell 一句话就能做到：

``` shell
echo Hello World!
```

其中 echo 语句要输出的内容可加引号也可不加引号，要输出多个内容时只需将内容依次写出来即可。

### 变量

**注意：**赋值号两边应该没有空格,否则 num 会被当做一个命令

Shell Script是一种弱类型语言，使用变量的时候无需首先声明其类型。新的变量会在本地数据区分配内存进行存储，这个变量归当前的Shell所有，任何子进程都不能访问本地变量。这些变量与环境变量不同，环境变量被存储在另一内存区，叫做用户环境区，这块内存中的变量可以被子进程访问。

Shell 有两种类型的变量：<br>
**临时变量：**Shell程序内部定义的，作用范围仅限于本程序，对其他程序不可见。包括了用户自定义变量、位置变量。<br>
**永久变量：**永久变量是环境变量，其值不随shell脚本的执行结束而消失。

变量的辅助命令：

``` shell
set  #查看系统中所有定义的变量
unset 变量名  #删除变量
env #用于显示环境变量及其取值
export #用于将本地数据区中的变量转移到用户环境区
```

变量可以直接定义：

``` shell
variable_name=variable_value
echo $variable_name # $ 用于取变量的值
```

`$variable_name` 可以在引号中使用，这一点和其他高级语言是明显不同的。如果出现混淆的情况，可以用花括号来区分，例如：

``` shell
a=hello world
echo "Hi, $as"
```

就不会输出`Hi, hello world`，而是输出`Hi，`。这是因为 Shell 把 `$as` 当成一个变量，而 `$as` 未被赋值，其值为空。正确的方法是：

`echo "Hi, ${a}s`

使用单引号，单引号中的变量不会进行变量替换操作。
例如：

``` shell
$ABC = “time is $Date”
echo $ABC #输出：time is 2013-12-4
$ABC = ‘time is $Date’
echo $ABC 输出：time is $Date 
```

### 算术运算

``` shell
((i=$j+$k))  # 等价于  i=`expr $j + $k` 
((i=$j-$k))  # 等价于  i=`expr $j - $k` 
((i=$j*$k))  # 等价于  i=`expr $j * $k` 
((i=$j/$k))  # 等价于  i=`expr $j / $k` 
```

### 条件控制

if 语句：

``` shell
if [ 条件 ];
  then
elif …; 
  then
else
fi
```

case 语句：

``` shell
case a in
    "A") ;;
    *) ;;  # 默认情况，相当于C语言的 default
 esac 
```

与其他语言不同，Shell中if语句的条件部分要以分号来分隔。其中[]表示条件测试，常用的条件测试有下面几种：

``` shell
[ -f "$file" ]  #判断$file是否是一个文件
[ $a -lt 3 ]  #判断$a的值是否小于3，同样-gt和-le分别表示大于或小于等于
[ -x "$file" ]  #判断$file是否存在且有可执行权限，同样-r测试文件可读性
[ -n "$a" ]  #判断变量$a是否有值，测试空串用-z
[ "$a" = "$b" ]  #判断$a和$b的取值是否相等
[ cond1 -a cond2 ]  #判断cond1和cond2是否同时成立，-o表示cond1和cond2有一成立
```

要注意条件测试部分中的空格。在方括号的两侧都有空格，在-f、-lt、=等符号两侧同样也有空格。如果没有这些空格，Shell解释脚本的时候就会出错。

### 数组

数组声明和使用的简单用法：

``` shell
array=(a b c)
${array[0]} 通过下标去数组内容
${array[*]} 取所有元素
${#array[*]} 取长度
```

### 循环

**for 循环：**

语法1：

``` shell
for n in a b c d 
    do 
    #  代码
done
```

语法2：

``` shell
for((i=0;i<100;i++))
    do 
    #  代码
done 
```

**while 循环：**

``` shell
while [ 条件 ]
    do
    #  代码
done
# 注意:在变量自增的时候 
#   如果直接 $num+1 字符串拼接
num=$(($num+1)) #当数字计算
num=$[$num+1]
```

### 函数

定义函数

``` shell
function 函数名() { 
    函数体
    echo $1 #  取第一个参数
}
```

调用函数: 函数名 参数1 参数2

echo 输出结果; $(函数名取结果)

### 举个栗子

这是代叔的一个练习

``` shell
function round(){
    dat=$((`date +"%s%N"`))
    echo ${dat:0-8}
}
function random(){
    dat=$((`date +"%s%N"`))
    num=$(($dat % 10))
    num1=$(($num % $(($2 - $1))))
    num2=$(($num1 + $1))
    echo $num2
}
function cost(){
    if [ $1 -le 3 ];
    then echo 8
    elif [ $1 -gt 3 ];
    then 
        num1=$[$1-3]
        num2=$[$num1*2]
        num3=$[$num2+8]
        echo $[$num3]
    fi
}
phone1=('137' '192' '135' '155' '188')
phone2=`round 00000000 99999999`
pho=`random 0 5`
phone=${phone1[$pho]}$phone2
mile=`random 1 21`
time=$(date +'%Y-%m-%d %H:%M:%S')
city=('哈尔滨' '北京' '上海' '大数据')
harbin=('香坊区' '道里区' '道外区' '南岗区' )
beijing=('海淀区' '朝阳区' '宣武区' '丰台区')
shanghai=('奉贤区' '嘉定区' '宝山区' '黄浦区')
bigdata=('Java' 'Python' 'Hadoop' 'Linux')
money=`cost $mile`
len=`random 0 4`
len2=`random 0 4`
case $len in
"0") address1=${harbin[$len2]};;
"1") address1=${beijing[$len2]};;
"2") address1=${shanghai[$len2]};;
"3") address1=${bigdata[$len2]};;
esac
address=${city[$len]}
echo Time:$time Phone:$phone Address:$address$address1 Mile:$mile Sum:$money >> Taxi.log
```


