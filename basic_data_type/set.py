# Python3 集合
'''

    集合set是一个无序的不重复元素序列
    可以使用大括号，{}或者set()函数创建集合
    创建一个空的集合要用set()因为{}是用来建一个空的字典
'''

set_a = {'a', 'b', 'c', 'a'}
print(set_a)

print('a' in set_a)
print(2 in set_a)

set_b = set("jinwandalaohu")
print(set_b)
set_c = set("todayisblue")
print(set_c)


# 集合间的运算

# b中有，a 中没有的元素
print(set_b - set_c)


# a 或 b 中包含的元素
print(set_b | set_c)

# a 和 b 都包含的元素

print(set_b & set_c)

# a有b没有或b有a没有的元素

print(set_b ^ set_c)

# 集合推导式

result = {x for x in 'jinwandalaohu' if x not in 'abc'}
print(result)



