---
description: By runoob
---

# 列表

```text
    List（列表） 是 Python 中使用最频繁的数据类型。

    列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列        表（所谓嵌套）。

    列表是写在方括号 \[\] 之间、用逗号分隔开的元素列表。
```

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

```text
    列表截取的语法格式如下：
```

```text
变量[头下标:尾下标]
```

```text
    索引值以 0 为开始值，-1 为从末尾的开始位置。
```

![](https://www.runoob.com/wp-content/uploads/2013/11/list_slicing1.png)

```text
    加号 + 是列表连接运算符，星号 \* 是重复操作。如下实例：
```

```text
#!/usr/bin/python3

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
```

```text
    以上实例输出结果：
```

```text
['abcd', 786, 2.23, 'runoob', 70.2]
abcd
[786, 2.23]
[2.23, 'runoob', 70.2]
[123, 'runoob', 123, 'runoob']
['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
```

```text
    与Python字符串不一样的是，列表中的元素是可以改变的：
```

```text
>>> a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 将对应的元素值设置为 []
>>> a
[9, 2, 6]
```

```text
    List 内置了有很多方法，例如 append\(\)、pop\(\) 等等，这在后面会讲到。
```

{% hint style="info" %}
* 1、List写在方括号之间，元素用逗号隔开。
* 2、和字符串一样，list可以被索引和切片。
* 3、List可以使用+操作符进行拼接。
* 4、List中的元素是可以改变的。
{% endhint %}

```text
    Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
```

![](https://www.runoob.com/wp-content/uploads/2013/11/python_list_slice_2.png)

```text
    如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
```

```text
def reverseWords(input):

    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
```

```text
    输出结果为：
```

```text
runoob like I
```

