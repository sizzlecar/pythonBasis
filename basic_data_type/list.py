# Python3列表

'''
    序列是Python中最基本的数据结构，序列中的每个元素都分配一个数字，自己的索引
    Python有6个序列的内置类型，最常见的是列表和元组
    序列都可以进行的操作包括索引，切片，加，乘，检查成员
    列表内的数据不需要具有相同的类型
'''

list_a = [1, 2, 3, "xxx", "carl"]
list_b = [4, 5, 6, 7, 8]

# 使用索引来访问列表中的值

print("list_a[0]", list_a[0])
print("list_a[0:3]", list_a[0:3])
print("list_a[-1]", list_a[-1])
print("list_a[-1:-3]", list_a[-3:-1])

list_b[0] = 'blus'

print(list_b)

# 追加元素
list_b.append(3.444)
print(list_b)

# 删除列表元素

del list_b[2]
print(list_b)

# 列表拼接

list_c = ["tom", "jack", "rose"]
list_d = ["Zhang San", "Zhao Si", "Wang Wu", 22222222222222222222222222222]

print(list_c + list_d)

# 嵌套列表

list_e = [1.2, 3, 4]
list_d = ["sam", "lucy", list_e]
print(list_e)
print(list_d[2][0])

# Python 列表常用方法

# len() 列表元素个数
print(len(list_e))

# max 返回列表元素最大值
print(max(list_c))

# min 返回列表元素最小值
print(min(list_c))

# 将元组转成列表

un_update_list = (1, 2, 4)

update_list = list(un_update_list)
update_list[0] = "w"
print(update_list)

# 列表常用方法
'''
序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表


'''




