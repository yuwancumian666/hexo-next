---
title: Nursery 开发笔记
date: 2020-09-27 17:26:11
categories:
- .Net
tags:
- C#
- WPF
- 笔记
---

Nursery是一个简单的进程托管Demo，用于启动console应用程序。

<!-- more -->


# 问题

## CheckBoxList

这里一开始用的是[ObservableCollection](https://www.c-sharpcorner.com/uploadfile/syedshakeer/checkboxlist-in-wpf/)的方式，后感感觉太过于繁杂，改为直接向`ListBox`中添加`CheckBox`：`ProcessListBox.Items.Add(checkBox);`。


## ListView的动态更新

或许有用的资料
1. [CheckBoxList(ObservableCollection)in WPF](https://www.c-sharpcorner.com/uploadfile/syedshakeer/checkboxlist-in-wpf/)
2. [WPF ListView实时更新及INotifyPropertyChanged使用演示](https://blog.csdn.net/farsee520/article/details/106799065)
3. [WPF Listview绑定数据发生改变后前端没有更新](https://blog.csdn.net/djshichaoren/article/details/79957523)

### 尝试

这里想的是另起一个监控线程，对线程的实时信息进行更新。对`infoList`更新后，通过`ProcessInformationListView.ItemsSource = infoList;`使其生效，但是遇到了线程间对对象访问的问题：
{% note danger %}
`System.InvalidOperationException:“调用线程无法访问此对象，因为另一个线程拥有该对象。`
{% endnote %}
``` cs
ProcessInformationListView.Dispatcher.BeginInvoke(new Action(() =>
{
    ProcessInformationListView.ItemsSource = infoList;
    ArgsButton.Content = "test";
    logger.Info("size:" + infoList.Count);
}));
```
改成这段代码之后，监控线程（monitor）能更改主线程的对象（button的内容发生更改可以证明），但是`ListView`
的内容并不会更改。不仅如此，monitor执行后主线程不能向ListView中添加内容了，如果先添加了内容，monitor执行后内容不会改变。

### 最终解决方式

1. `LIstView`的数据源使用`ObservableCollection`：`private ObservableCollection<ProcessInformation> InfoList { get; set; }`
2. 实体类`ProcessInformation`继承`INotifyPropertyChanged`接口
``` cs
public class ProcessInformation : INotifyPropertyChanged
    {
        private string _Process;
        private int _PID;
        private string _CPU;
        private string _Memory;
        public event PropertyChangedEventHandler PropertyChanged;

        public string Process {
            get { return _Process; }
            set { _Process = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("Process"));
            }
        }
        public int PID {
            get { return _PID; }
            set { _PID = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("PID"));
            }
        }
        public string CPU {
            get { return _CPU; }
            set { _CPU = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("CPU"));
            }
        }
        public string Memory {
            get { return _Memory; }
            set { _Memory = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("Memory"));
            }
        }
    }
```
3. 跨线程访问（这个就不用了，因为`ObservableCollection`实现了`INotifyPropertyChanged`接口，当`InfoList`发生改变时会自动更新`ListView`，不用手动更新`ListView.ItemsSource`，也就不会发生跨线程访问`ListView`了。ps: 好像是跨线程更改前台的数据才会出现[这个问题](#尝试)）
不更新、不能添加`GridView`的原因也应该是没有实现`INotifyPropertyChanged`接口

``` cs
ProcessInformationListView.Dispatcher.BeginInvoke(new Action(() =>
{
    ProcessInformationListView.ItemsSource = InfoList;
}));
```

## 不支持从调度程序线程以外的线程对其 SourceCollection 进行的更改

``` csharp
private ObservableCollection<ProcessInformation> infoList { get; set; }
infoList = new ObservableCollection<ProcessInformation>();
infoList.Remove(item);
```

{% note danger %}
`System.NotSupportedException:“该类型的 CollectionView 不支持从调度程序线程以外的线程对其 SourceCollection 进行的更改。”`
{% endnote %}

`ObservableCollection`类型的`CollectionView`不支持从调度程序线程以外的线程对其 SourceCollection 进行的更改。（我也不懂是哪个线程对该对象进行了访问，不是我的监控线程）

[解决方式](https://www.cnblogs.com/Stay627/p/12082792.html)：
``` csharp
ThreadPool.QueueUserWorkItem(delegate
{
    SynchronizationContext.SetSynchronizationContext(new DispatcherSynchronizationContext(
        System.Windows.Application.Current.Dispatcher));
    SynchronizationContext.Current.Post(pl =>
    {
        for (int i = 0; i < infoList.Count; i++)
        {
            var item = infoList[i];
            if (item.Process.Equals(fileName))
            {
                infoList.Remove(item);
                return;
            }
        }
    }, null);
});
```

# 功能

## [NotifyIcon](https://handyorg.github.io/handycontrol/extend_controls/notifyIcon/)
程序托盘图标用的是[HandyControl](https://handyorg.github.io/handycontrol/)的控件。
根据文档编辑图标、绑定事件即可。
``` xml
<hc:NotifyIcon x:Name="NotifyIcon" Text="ProcessNursery" 
                Visibility="Visible"
                Icon="/assets/Nursery32x32.ico" Click="NotifyIcon_Click">
    <hc:NotifyIcon.ContextContent>
        <StackPanel VerticalAlignment="Center">
            <Button Command="hc:ControlCommands.PushMainWindow2Top" MinWidth="100" Content="OpenPanel"/>
            <Button Click="ExitApp" MinWidth="100" Style="{StaticResource ButtonPrimary}" Content="Exit"/>
        </StackPanel>
    </hc:NotifyIcon.ContextContent>
</hc:NotifyIcon>
```

## 日志系统

[NLog](https://nlog-project.org/)的日志系统，主要是调试时候找问题的。

分为以下几种日志等级：
{% note default %} Trace {% endnote %}
{% note primary %} Debug {% endnote %}
{% note success %} Info {% endnote %}
{% note info %} Warn {% endnote %}
{% note warning %} Error {% endnote %}
{% note danger %} Fatal {% endnote %}

### 配置

NLog使用需要添加配置文件，可以添加到`App.config`，也可以新建`NLog.config`然后添加内容。我手动新建配置文件之后使用不了，使用NuGet命令添加成功。（工具->NuGet 包管理器->程序包管理器控制台，输入`Install-Package NLog.Config [-Version 4.7.5]`）。关于自定义日志，可以看[这里](https://github.com/NLog/NLog/wiki)

``` xml
<?xml version="1.0" encoding="utf-8" ?>
<nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.nlog-project.org/schemas/NLog.xsd NLog.xsd"
	  autoReload="true"
      throwExceptions="false"
      internalLogLevel="Off" internalLogFile="c:\temp\nlog-internal.log">
  <targets>
	  <target name="console" xsi:type="ColoredConsole" layout="${date:format=yyyy/MM/dd HH\:mm\:ss} ${uppercase:${level}}> ${message}">
		  <highlight-row condition="level == LogLevel.Debug" foregroundColor="Green" />
		  <highlight-row condition="level == LogLevel.Info" foregroundColor="Cyan" />
		  <highlight-row condition="level == LogLevel.Warn" foregroundColor="Yellow" />
		  <highlight-row condition="level == LogLevel.Error" foregroundColor="Red" />
		  <highlight-row condition="level == LogLevel.Fatal" foregroundColor="Red" backgroundColor="White" />
	  </target>
	  <target name="debugger" xsi:type="Debugger"
					  layout="${date:format=HH\:mm\:ss} | ${level:padding=-5} | ${message}" />
  </targets>

  <rules>
	  <logger name="*" writeTo="console" />
	  <logger name="*" minlevel="Debug" writeTo="debugger" />
  </rules>
</nlog>
```

### 使用

``` cs
private static Logger logger = LogManager.GetCurrentClassLogger();
logger.Debug("Debug");
logger.Info("Info");
logger.Error("Error");
```


## 进程的CPU与内存

使用.Net的`PerformanceCounter`类型对进程的性能进行监控

``` cs
Process process = pNersury[fileName].process;
PerformanceCounter cpuCounter = new PerformanceCounter("Process", "% Processor Time", process.ProcessName);
PerformanceCounter memCounter = new PerformanceCounter("Process", "Working Set", process.ProcessName);
infoList[i].CPU = cpuCounter.NextValue().ToString() + CPUnit;
infoList[i].Memory = ((long)memCounter.NextValue() >> 10).ToString() + MemoryUnit;
```


## 实时获取子进程的输出

参考：
1. [启动一个进程并实时获取状态信息](https://www.cnblogs.com/tcjiaan/p/5957422.html)
2. [c# - 从Process获取实时输出](https://www.coder.work/article/246276)

{% note info %}
`UseShellExecute`必须为`false`，不然无法在代码中读标准。
`RedirectStandardOutput`必须为`true`，这样我们才能在代码中访问标准流。
`EnableRaisingEvents`必须为`true`，这样才会引发`OutputDataReceived`和`Exited`
{% endnote %}

解决方式是两条内容的结合：
``` cs
Process child = new Process();
child.StartInfo.RedirectStandardOutput = true;
child.StartInfo.RedirectStandardError = true;
child.StartInfo.CreateNoWindow = true;
child.StartInfo.UseShellExecute = false;
child.EnableRaisingEvents = true;  // 这样才会引发OutputDataReceived
child.OutputDataReceived += new DataReceivedEventHandler((s, e) =>
{
    Console.WriteLine(e.Data);
});
child.ErrorDataReceived += new DataReceivedEventHandler((s, e) =>
{
    Console.WriteLine(e.Data);
});
child.Start();
child.BeginOutputReadLine();
child.BeginErrorReadLine();
```


