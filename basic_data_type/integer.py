# python3 基本数据类型

'''

1.python中的变量不需要声明
2.每个变量使用前都需要赋值，变量赋值之后该变量才会被创建
3.python中变量没有类型，我们所说的类型是变量所指内存中对象的类型

'''

# 整形变量
count = 100

# 浮点型变量
miles = 1000.00

# 字符串
name = "carl"

print(count, miles, name)

# 多个变量复制

a = b = c = 1

print(a, b, c)


# 为多个对象指定多个变量

a, b, c = 1, 2, "xxx"

print(a, b, c)

"""
python3 中6个标准的数据类型
 
 #不可变数据
    1.Number (数字)
    2.String (字符串)
    3.Tuple (元组)
 #可变数据
    4.List (列表)
    5.Set(集合)
    6.Dictionary(字典)
"""


# Number (数字)

'''
python3 数字类型分为四种
    1.int
    2.float
    3.bool
    4.complex (复数)
'''
# 内置的type()函数可以查询变量所指的对象类型

a, b, c, d = 20, 1.0, True, 1 + 3j

print(type(a), type(b), type(c), type(d))


# 还可以用 isinstance来判断
a = 100.0

result = isinstance(a, float)

print(result)

# type(), isinstance 区别？？？


# 删除对象的引用

carl = "xxx"

del carl

print(carl)


# 一个变量可以通过赋值指向不同类型的对象

# //运算符返回一个整数

# 混合计算时python会把整型转换位浮点数












