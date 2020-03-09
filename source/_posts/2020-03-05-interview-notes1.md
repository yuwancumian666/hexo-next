---
title: 面试题
date: 2020-03-05 15:26:26
categories:
- 面试
tags:
- 计算机网络
- Linux
- Mysql
- 笔记
---

杨超越附体🙏

<!-- more -->

# 计算机网络

## http和https的区别

+ https需要用到CA（certificate）申请证书，一般免费证书较少，申请需要一定费用
+ http是面向字符的超文本传输协议，明文传输，https带有ssl加密
+ http-tcp连接，使用80端口；https-ssl-tcp连接，使用443端口
+ http连接简单、无状态；https可进行加密传输、有身份认证，比http安全；
+ 无状态指的是数据包的发送、传输、接收都是相互独立的；无连接指的是通信双方都不长久维持双方任何信息





# Linux

## 系统相关

### 查看有几颗物理CPU和CPU核数

``` bash
root ~> cat /proc/cpuinfo | grep -c 'physical id'
8
root ~> cat /proc/cpuinfo | grep -c 'processor'
8
```

### 查看系统负载

``` shell
root ~> w
 16:46:06 up 31 min,  0 users,  load average: 0.52, 0.58, 0.59
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root ~> uptime
 16:46:26 up 32 min,  0 users,  load average: 0.52, 0.58, 0.59
```

### buffer与cache

buffer与cache都是内存中的一块区域，写磁盘：`CPU -> buffer -> disk`; 读磁盘：
`disk -> cache -> CPU`

### ps查看当前系统都有哪些进程

``` bash
root ~> ps -aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   9628  1044 ?        Ssl  16:14   0:00 /init
root        24  0.0  0.0   8912   232 tty1     Ss   16:17   0:00 /init
root        25  0.0  0.0  16920  3624 tty1     S    16:17   0:00 -bash
root      1052  0.0  0.0  17648  2048 tty1     R    17:01   0:00 ps -aux
root ~> ps -elf
F S UID        PID  PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
0 S root         1     0  0  80   0 -  2407 ?      16:14 ?        00:00:00 /init
0 S root        24     1  0  80   0 -  2228 -      16:17 tty1     00:00:00 /init
0 S root        25    24  0  80   0 -  4230 -      16:17 tty1     00:00:00 -bash
0 R root      1053    25  0  80   0 -  4345 -      17:01 tty1     00:00:00 ps -elf
```

### netstat查看端口和网络连接状况

> netstat -lnp 查看系统开启了哪些端口
> netstat -an 查看网络连接状况

### free查询可用内存

``` bash
root ~> free
              total        used        free      shared  buff/cache   available
Mem:        8175468     5991112     1955004       17720      229352     2050624
Swap:      25165824      415356    24750468
```



## 更改ip、dns、hostname

{% note info %}
**IP**
`ifconfig eth0 192.168.1.110 netmask 255.255.255.0` 即时生效
`vim /etc/sysconfig/network-scripts/ifcfg-eth0`
`service network restart`
{% endnote %}

{% note info %}
**hostname**
`hostname name1`
`vim /etc/sysconfig/network`
`reboot`
{% endnote %}

{% note info %}
**DNS**
`vim /etc/resolv.conf`
`vim /etc/sysconfig/network-scripts/ifcfg-eth0`
{% endnote %}

## 定时任务 crontab

任务格式：
minute hour day month week user  command
操作符：
+ `*` 取值范围内所有数字
+ `/` 每过多少时间单位，“0-23/2”表示每两小时执行一次，同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。
+ `-` 从何时到何时，例如“2-6”表示“2,3,4,5,6”
+ `,` 指定一个列表范围，例如“1,2,6,8,9”

> `* * * * * user command` 每分钟执行一次
> `20,45 * * * * user command` 每小时的第20和45分钟执行
> `20,45 21-23 * * * user command` 每天的第21到23点的第20和45分钟执行
> `20,45 21-23 */2 * * user command` 每两天的第21到23点的第20和45分钟执行
> `20 3 * * 6 user command` 每两周六的3:20执行

## tar归档压缩

打包是指将一大堆文件或目录变成一个总的文件；压缩则是将一个大的文件通过一些压缩算法变成一个小文件

> 选项  -c 压缩
>       -x 解压缩
>       -f 文件名
>       -v 显示
> 打包并压缩    tar -czvf 压缩后文件名 目标
> 解压缩  tar -xzvf 目标名
>             -xzvf 目标名 -C 目标目录


## chmod

文件权限等级：文件拥有者、群组、其他

`chmod mode file`

mode: [ugoa][[+-=][rwxX]...]
+ u表示文件拥有者，g表示与u同用户组的成员，o表示此外的人，a表示全部
+ 表示增加权限、- 表示取消权限、= 表示唯一设定权限
+ r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行

User、Group、及Other的权限也可以用数字表示r=4、w=2、x=1

## scp远程拷贝

scp [参数] [原路径] [目标路径]

``` bash
# 复制文件
$scp /opt/soft/demo.tar root@10.6.159.147:/opt/soft/scptest
# 复制目录 下载和上传
$scp -r root@10.6.159.147:/opt/soft/test /opt/soft/
$scp -r /opt/soft/test root@10.6.159.147:/opt/soft/scptest
```

## 其他

+ **top**: 实时显示process的动态
+ **touch 文件名**: 创建/更新文件
+ **tail**: 显示文件尾部几行内容，“+”指从第n行开始
+ **cat**: 显示文件内容；`cat m1 m1 > file`将m1和m2合并后放入file中

# Mysql

## 数据类型

char 和 varchar 类型相似，但他们的保存和检索方式不同，最大长度和尾部空格是否被保留也不同，存储和检索过程中不进行大小写转换。

## select

+ 在 WHERE 子句中用 BINARY 表示字符串比较区分大小写


## delete

+ delete和truncate仅删除表数据，drop连表数据和表结构一起删除
+ delete是DML语句，操作完没有提交事务还可以回滚；truncate和drop是DDL语句，操作即时生效，不能回滚
+ 执行速度：drop > truncate > delete

## like

`%`匹配任意个字符，`_`匹配单个字符，`[]`表示括号内所列字符的一个，`[^]`表示不在括号内的字符。

+ `%a`     //以a结尾的数据
+ `a%`     //以a开头的数据
+ `%a%`    //含有a的数据
+ `_a_`    //三位且中间字母是a的
+ `_a`     //两位且结尾字母是a的
+ `a_`     //两位且开头字母是a的

