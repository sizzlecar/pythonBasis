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

# 修改元组
# 元组中的元素值是不允许修改的，但是可以对元组进行连接组合

tup1 = (22, "xx")
tup2 = ("name", "age", 3333.4444)

print(tup1 + tup2)


# 元组运算符


# 获取元组的长度

print(len(tup2))


# 元组复制

print(('carl',) * 4)

# in
'xx' in ('xx', 22, 22.3)

# 迭代

for x in (2.3, 4, "xx"):
    print(x)

# 元组内置函数
'''
序号	方法及描述	实例
1	len(tuple)
计算元组元素个数。	
>>> tuple1 = ('Google', 'Runoob', 'Taobao')
>>> len(tuple1)
3
>>> 
2	max(tuple)
返回元组中元素最大值。	
>>> tuple2 = ('5', '4', '8')
>>> max(tuple2)
'8'
>>> 
3	min(tuple)
返回元组中元素最小值。	
>>> tuple2 = ('5', '4', '8')
>>> min(tuple2)
'4'
>>> 
4	tuple(seq)
将列表转换为元组。	
>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')


'''













