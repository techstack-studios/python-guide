---
description: By RICE
---

# 配置python环境

首先我们要先移步[https://python.org，下载Python：!\[\]\(https://pic1.zhimg.com/80/v2-665e04bf3906603be7532048927f4688\_1440w.jpg](https://python.org，下载Python：![]%28https://pic1.zhimg.com/80/v2-665e04bf3906603be7532048927f4688_1440w.jpg)\)

随后，我们把鼠标移动到Downloads上面，就会发现有不同平台的Python供我们下载：![](https://pic4.zhimg.com/80/v2-fd3135d965479d9a5d38e018c9ef3627_1440w.jpg)

如果您使用的是Windows或者macOS系统，那么只需要安装一个安装器并且按照提示进行操作就可以了，不过如果您使用的是Linux系统的话，那么在Python官网上一般只会提供源代码，需要自己编译，因此最方便的办法实际上就是通过系统自带的包管理器安装。Linux系统安装软件包的方式往往大同小异，而且Linux系统也非常多，所以我在这里用Ubuntu举例子：

```text
sudo apt install python3
```

一般来说通过这条命令就可以安装比较新的python3.x。

{% hint style="info" %}
如果使用的是Windows系统的话，那么在安装时一定要注意勾选Add Python 3.x to PATH，通过这种方式，我们才能够在Windows的命令提示符和powershell中运行Python。
{% endhint %}

在安装完成之后，可以打开命令提示符（UNIX/Linux上为终端），并且输入python3（UNIX/Linux）或者python（Windows），敲击回车，看看有没有进入Python的交互式Shell，如果成功进入，就意味着你已经安装好了Python环境，很快就可以开始我们的编程之旅了。

