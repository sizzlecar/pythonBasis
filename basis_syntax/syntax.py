import keyword



'''
标识符
    1.第一个字符必须是字母或者下划线
    2.标识符的其他部分由字母数字下划线组成
    3.标识符对大小写敏感
'''
a = 5
_a = 5
a_a = 5
a_2 = 6
_A = 7


# 单行注释
print(keyword.kwlist)


"""
缩进代表代码块

"""


if True:
    print("I am true")
else:
    print("I am false")

# 多行语句
total = "one" + \
    "tow" + \
    "three"

print(total)

total = ["one",
         "two",
         "three"]
print(total)


# 同一行显示多条语句

x = "runoob"; print(x)

# print 默认输出是换行的，如果实现不换行需要在变量末尾加上end = ""

print('我')
print('换')
print('行')
print('----------')
print('我', end=" ")
print('不', end=" ")
print('换', end=" ")
print('行', end=" ")


