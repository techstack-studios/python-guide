---
description: By runoob
---

# 字典

```text
    **字典（dictionary）**是Python中另一个非常有用的**内置数据类型**。

    列表是**有序的对象集合**，字典是**无序的对象集合**。两者之间的区别在于：**字典当中的元素是通过键来存取的，而不是通过偏移存取。**

    字典是一种映射类型，字典用 { } 标识，它是一个无序的 **键\(key\) : 值\(value\)** 的集合。

    键\(key\)必须使用**不可变类型**。

    在同一个字典中，键\(key\)必须是**唯一**的。
```

```text
#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
```

```text
    以上实例输出结果：
```

```text
1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict_keys(['name', 'code', 'site'])
dict_values(['runoob', 1, 'www.runoob.com'])
```

```text
    构造函数 dict\(\) 可以直接从键值对序列中构建字典如下：
```

```text
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
```

```text
    另外，字典类型也有一些内置的函数，例如clear\(\)、keys\(\)、values\(\)等。
```

{% hint style="info" %}
* 1、字典是一种映射类型，它的元素是键值对。
* 2、字典的关键字必须为不可变类型，且不能重复。
* 3、创建空字典使用 **{ }**。
{% endhint %}

