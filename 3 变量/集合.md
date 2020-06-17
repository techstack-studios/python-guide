---
description: By runoob
---

# 集合

```text
    集合（set）是由**一个或数个形态各异的大小整体组成的**，构成集合的事物或对象称作**元素**或是**成员**。

    基本功能是进行**成员关系测试**和**删除重复元素**。
```

可以使用大括号 { } 或者 set\(\) 函数创建集合，

{% hint style="info" %}
创建一个空集合必须用 set\(\) 而不是 { }，因为 { } 是用来创建一个空字典。
{% endhint %}

创建格式：

```text
parame = {value01,value02,...}
或者
set(value)
```

```text
#!/usr/bin/python3

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素
```

```text
    以上实例输出结果：
```

```text
{'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
Runoob 在集合中
{'b', 'c', 'a', 'r', 'd'}
{'r', 'b', 'd'}
{'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
{'c', 'a'}
{'z', 'b', 'm', 'r', 'l', 'd'}
```

