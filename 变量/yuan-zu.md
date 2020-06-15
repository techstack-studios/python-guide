---
description: By runoob
---

# 元组

```text
    元组（tuple）与列表类似，不同之处在于**元组的元素不能修改**。元组写在小括号 \(\) 里，元素之间用逗号隔开。

    元组中的元素类型也可以不相同：
```

```text
#!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
```

```text
    以上实例输出结果：
```

```text
('abcd', 786, 2.23, 'runoob', 70.2)
abcd
(786, 2.23)
(2.23, 'runoob', 70.2)
(123, 'runoob', 123, 'runoob')
('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')
```

```text
    元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。

    其实，可以把字符串看作一种特殊的元组。
```

```text
>>> tup = (1, 2, 3, 4, 5, 6)
>>> print(tup[0])
1
>>> print(tup[1:5])
(2, 3, 4, 5)
>>> tup[0] = 11  # 修改元组元素的操作是非法的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

```text
    虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

    构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
```

```text
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
```

```text
    string、list 和 tuple 都属于 sequence（序列）。
```

{% hint style="info" %}
* 1、与字符串一样，元组的元素不能修改。
* 2、元组也可以被索引和切片，方法一样。
* 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
* 4、元组也可以使用+操作符进行拼接。
{% endhint %}

