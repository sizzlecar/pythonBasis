# Python3 函数

def hello(name):
    print("hello !" + name)


fun = hello

fun('test')

print(hello)
print(fun)

# 参数

'''
    1.必须参数
    2.关键字参数
    3.默认参数
    4.不定长参数


'''


# 1.必须参数

# 必须参数必须以正确的顺序传入函数，调用时的数量必须和声明时的一样

def require_fun(name):
    print('hello!' + name)


require_fun('chejinxuan')


# require_fun()

# 2.关键字参数
# 关键字参数允许函数调用时参数的顺序与声明时的顺序不一致


def key_para(age, name):
    print("年龄:" + age + " 姓名:" + name)


key_para(name="今晚打老虎", age="18")


# 3.默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数
# 加了*的参数会以元组的形式导入，存放所有未命名的变量参数
# 加了**的参数会以字典的形式导入

def default_parm(age="100", name="xx"):
    print("年龄:" + age + "姓名:" + name)


default_parm(name="xx2", age="22")
default_parm(age="22")
default_parm("45")


# 4.不定长参数

def no_length(class_name, *students):
    print("班级名称:" + class_name)
    print(students)


no_length("三年级一班", "张三", "李四", "王五", "赵六")

no_length("三年级二班")


def no_length_2(arg1, **other_params):
    print(arg1)
    print(other_params)


no_length_2("parms_one", name="blus", age=18)


# 声明函数时，参数中*可以单独出现

def f(a, b, *, c):
    return a + b + c

# f(1,2,3)
print(f(1, 2, c=3))

# 匿名函数
'''
    1.lambda只是一个表达式，函数体必def简单很多
    2.lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑
    3.lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数

'''

sum = lambda arg1, arg2: arg1//arg2

print(sum(10, 3))

# 变量作用域

'''
    Python的作用域一共有4种
    L(local) 局部作用域
    E(Enclosing) 闭包函数外的函数中
    G(Global) 全局作用域
    B(Built-in) 内建作用域 
    Python解释器会已 L->E->G->B 的规则查找
    
'''

# 内建作用域
# 跟全部作用域有什么区别
x = int(3.9)

# 全局作用域
count = 0


def outer():
    # 闭包函数外的函数中
    outer_var = 1
    def inner():
        # 局部函数作用域
        inner_var = 2


'''
    Python中只有模块，类，以及函数(def,lambda)才会引入新的作用域
    也就说这些语句内定义的变量外部也可以访问
'''

if True:
    msg = "today is blue"

print(msg)



def test():
    var_c = "2"


# print(var_c)

'''
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问，调用函数时，所有
    在函数内声明的变量名称都将会被加入到作用域中

'''

total = 0
def sum(arg1, arg2):
    total = arg1 + arg2
    print(total)
    return total


sum(10, 20)
print("total", total)

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了

def update_global(a, b):
    global total
    print(total)
    total = a + b
    print(total)


update_global(100, 200)
print("全局变量total:", total)

# 如果要修改嵌套作用域 enclosing作用域，外层非全局作用域 中的变量则需要nonlocal 关键字

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 1000
        print(num)
    inner()
    print(num)

outer()