---
layout: post
title: 软件及开发包安装中的那些坑
date: 2019-02-22 00:00:00 +0800
description: 
categories:
- Software
tags: 
- C/C++
- CUDA
- LaTex
- GitHub Pages
- 软件
- 笔记
---

{% cq %} 先把坑都踩一遍是为了以后踩更多的坑。 {% endcq %}

<!-- more -->

## latexindent

+ 来自：安装LaTex-formatter需要安装的工具
+ 方式：解压缩，（可数的）文件直接拖入目录
+ 目录：`C:\Program\texlive\2018\texmf-dist\scripts\latexindent`
+ 文件：latexindent.exe
+ 使用方式：选中代码->右键`格式化选定内容`

注：更改了该目录下的`defaultSettings.yaml`的某些设置

``` yaml
# line222~line246
indentAfterHeadings:
    part:
       indentAfterThisHeading: 1
       level: 1
    chapter: 
       indentAfterThisHeading: 1
       level: 2
    section:
       indentAfterThisHeading: 1
       level: 3
    subsection:
       indentAfterThisHeading: 1
       level: 4
    subsection*:
       indentAfterThisHeading: 1
       level: 4
    subsubsection:
       indentAfterThisHeading: 1
       level: 5
    paragraph:
       indentAfterThisHeading: 1
       level: 6
    subparagraph:
       indentAfterThisHeading: 1
       level: 7
```

## ruby-jekyll

大佬[Pchou的博客](http://www.pchou.info/ssgithubPage/2014-07-04-build-github-blog-page-08.html)

1. 安装[Ruby with Devkit](https://rubyinstaller.org/downloads/)，所有组件都在这里了，注意安装路径不要出现空格
2. ruby安装完，会提示安装MSYS2，跟着提示走就好。现在新版本的Ruby已经集成了[RubyGems]([RubyGems](https://rubygems.org/pages/download))
3. 环境安装好就可以安装Bundle和Jekyll了（`gem install jekyll`），但是在今天（2019-2-22）安装的过程中发现bundle是安装环境是已经安装好了的。
4. 到博客目录下依次执行以下命令：
``` bash
bundle install
bundle update
bundle exec jekyll serve
```

### 关于ryby及Jekyll的某些错误

1. `jekyll 3.7.4 | Error:  incompatible character encodings: UTF-8 and GBK`
不知道如何解决，尝试设置命令行字符编码`chcp 65001`（不行）
已知的可能解决方法：设置 -> 时间和语言 -> 区域 -> 更改日期、时间或数字格式 -> 管理 -> 更改系统区域设置：选中“使用Unicode UTF-8 提供全球语言支持”，然后重启电脑，应该就解决了。
2. 执行`bundle`命令时出现`C:/Program/Ruby25-x64/lib/ruby/2.5.0/rubygems.rb:289:in 'find_spec_for_exe': can't find gem bundler (>= 0.a) with executable bundle (Gem::GemNotFoundException)`，在[StackOverflow](https://stackoverflow.com/questions/47026174/find-spec-for-exe-cant-find-gem-bundler-0-a-gemgemnotfoundexception)上找到答案：`Gemfile.lock`文件最后的`BUNDLED WITH`版本改为已安装的bundler版本。或者删除Gemfile.lock文件，重新`bundle exec jekyll serve`

## VSCode中C/C++找不到头文件

可能需要设置这些环境变量：

```bash
LIBRARY_PATH
C:\Program\mingw64\lib\gcc\x86_64-w64-mingw32\7.3.0

C_INCLUDE_PATH
C:\Program\mingw64\include;
C:\Program\mingw64\lib\gcc\x86_64-w64-mingw32\7.3.0\include;

CPLUS_INCLUDE_PATH
C:\Program\mingw64\include;
C:\Program\mingw64\lib\gcc\x86_64-w64-mingw32\7.3.0\include\c++;
C:\Program\mingw64\lib\gcc\x86_64-w64-mingw32\7.3.0\include\c++\backward;
C:\Program\mingw64\lib\gcc\x86_64-w64-mingw32\7.3.0\include\c++\x86_64-w64-mingw32;
```

## CUDA cuDNN

复制cuDNN到CUDA目录

``` cmd
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin\cudnn64_7.dll
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include\cudnn.h
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64\cudnn.lib
```

