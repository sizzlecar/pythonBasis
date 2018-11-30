# 列表推导式

list = [1, 2, 3, 4, 5]

print([3 * x for x in list])

print([[x, x ** 2] for x in list])

programmer = [' java', 'c ', ' c++ ']

print([x.strip() for x in programmer])

print([3 * x for x in list if x > 3])

# 其他循环和技巧
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print([x + y for x in list1 for y in list2])

print([list1[i] * list2[i] for i in range(len(list1))])

# 矩阵变换

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)])

# del 语句

'''
    使用del语句可以从一个列表中依索引而不是值来删除一个元素
    可以使用del语句从列表中删除一个切割，或者清空整个列表


'''

list_a = [1, 2, 3, 4, 5, 6, 7]

# 删除最后一个元素
del list_a[-1]

print(list_a)


# 删除某一段元素

del list_a[0:3]

print(list_a)

# 删除全部的元素

del list_a[:]

print(list_a)

# 删除list_a 变量
del list_a

# print(list_a)



# 元组嵌套


t = 3232, 4343, 'xxxx'

print(t)

u = t, ('22', 'xxx', 444)
print(u)




