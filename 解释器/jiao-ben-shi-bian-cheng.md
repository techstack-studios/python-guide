---
description: By runoob
---

# 脚本式编程

将如下代码拷贝至 **hello.py**文件中：

```text
print ("Hello, Python!");
```

通过以下命令执行该脚本：

```text
python3 hello.py
```

输出结果为：

```text
Hello, Python!
```

在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：

```text
#! /usr/bin/env python3
```

然后修改脚本权限，使其有执行权限，命令如下：

```text
$ chmod +x hello.py
```

执行以下命令：

```text
./hello.py
```

输出结果为：

```text
Hello, Python!
```

