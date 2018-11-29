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


