# Python3 元组
'''
    元组与列表类似，区别在于元组不能进行修改
    元组使用小括号，列表使用方括号
'''

tuple_a = ('xx', 1111, 2222.222)
print(tuple_a)

# 不需要括号
tuple_b = "a", "b", ":", 3333.4444
print(tuple_b)
print(type(tuple_b))

# 创建空元组

tuple_c = ()

print(tuple_c)
print(type(tuple_c))

# 当元组中只包含一个元素时，需要在元素后面添加逗号，否则会被当作运算符使用

tup_d = ('xx')
print(type(tup_d))

tup_e = ("xx", )
print(type(tup_e))

# 访问元组

tuple_d = (1, 2, 3, "xx", 222.4444)

print("tuple_d[0]", tuple_d[0])
print("tuple_d[1:]", tuple_d[1:])
print("tuple_d[-2:-1]", tuple_d[-2:-1])




