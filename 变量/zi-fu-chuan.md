---
description: By runoob
---

# 字符串

```text
    Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

    字符串的截取的语法格式如下：
```

```text
变量[头下标:尾下标]
```

```text
    索引值以 0 为开始值，-1 为从末尾的开始位置。
```

![](https://www.runoob.com/wp-content/uploads/2013/11/o99aU.png)

```text
    加号 + 是字符串的连接符， 星号 \* 表示复制当前字符串，与之结合的数字为复制的次数。实例如下：
```

```text
#!/usr/bin/python3

str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串
```

```text
    执行以上程序会输出如下结果：
```

```text
Runoob
Runoo
R
noo
noob
RunoobRunoob
RunoobTEST
```

```text
    Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
```

```text
>>> print('Ru\noob')
Ru
oob
>>> print(r'Ru\noob')
Ru \n oob
>>>
```

```text
    另外，反斜杠\(\\)可以作为续行符，表示下一行是上一行的延续。也可以使用 **"""..."""** 或者 **'''...'''** 跨越多行。

    注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
```

```text
>>> word = 'Python'
>>> print(word[0], word[5])
P n
>>> print(word[-1], word[-6])
n P
```

```text
    与 C 字符串不同的是，Python 字符串不能被改变。向一个 索引位置赋值，比如word\[0\] = 'm'会导致错误。
```

{% hint style="info" %}
* 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
* 2、字符串可以用+运算符连接在一起，用\*运算符重复。
* 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
* 4、Python中的字符串不能改变。
{% endhint %}

