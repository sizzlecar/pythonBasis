
class Father:
    name = None
    age = None
    address = None
    __private = None

    def say(self):
        print("My name is " + self.name + ",我今年" + self.age + "岁了" + "我住在：" + self.address)


class Son(Father):
    pass

class Brother(Father):
    pass


son = Son()
son.age = 18
print('---')
print(Father().age)

br = Brother()
br.age = 28
print(Father().age)



one = Father()
one.name = "one"

print(Father().name)

two = Father()
two.name = "two"
print(Father().name)

# 类属性与方法
'''
私有属性：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问

类的方法：类内部定义的方法参数列表必须包含一个self，代表当前类的实例

类的私有方法：两个下划线开头声明该方法为私有方法，只能在类的内部调用，不能在类的外部调用



'''


# 类的专有方法：

'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方

'''

# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(100, -89)
v2 = Vector(10, 1000)

print((v1 + v2).__str__())
