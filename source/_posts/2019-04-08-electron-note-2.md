---
title: Electron-Vue开发笔记——1
date: 2019-04-08 14:54:37
category: 
- [Node.js]
- [Electron]
tags: 
- 前端
- echarts
- Electron-Vue
---

在基本功能完成以后，开启debug模式。

<!-- more -->

# 图表

## Echarts
Buper中的图表是借助[Echarts](https://echarts.baidu.com/index.html)构建的。
### 主题
在[Echarts 主题在线构建工具](https://echarts.baidu.com/theme-builder/)可以下载默认主题。当然，你也可以借助此工具自定义更加炫酷的主题。

在此项目中直接按照说明加载主题是不成功的，解决方式有两个：
1. 把主题的json另存为`*.js`文件，然后
``` js
// theme.js
const theme = {/*json*/}
export default theme;

// *.vue
import theme from './themes/theme'
echarts.registerTheme('themename', theme);
echarts.init(document.getElementById('chart'), 'themename');
```
2. 把下载的js（不是json）文件中`root.echarts`改为`echarts`，然后在该文件里 `import echarts from 'echarts'`。然后在vue组件中可以直接使用`*.js`中注册的主题名字。