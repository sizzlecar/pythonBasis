# Python3 迭代器与生成器

'''
    迭代是访问集合元素的一种方式

    迭代器是一个可以记住遍历位置的对象

    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，
    迭代器只能往前不会会退

    迭代器有两个基本的方法 iter() 和 next()

    字符串，列表，或元组对象都可以用于创建迭代器

'''

list = [1, 2, 3, 5, 6]

# 创建迭代器对象
it = iter(list)

print(next(it))

print(next(it))

print(next(it))

# 迭代器的遍历
# 列表可以直接遍历 为什么要先获取迭代器?
for x in it:
    print(x, end=" ")


print('-------------------')


# 创建一个迭代器

'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__()
和 __next__()


__iter__() 方法返回一个特殊的迭代器对象，这个迭代器对象实现了
__next__() 方法并通过StopIteration异常标识迭代的完成


__next__() 方法会返回下一个迭代器对象


'''

class Number:

    def __iter__(self):
        self.num = 1
        return self


    def __next__(self):
        x = self.num
        self.num += 1
        return x



number = Number()

num_iter = iter(number)

print(next(num_iter))
print(next(num_iter))
print(next(num_iter))


'''
    StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
    在__next__()方法中我们可以设置在完成指定循环次数后触发StopIteration
    异常来结束迭代

'''


class Number2:

    def __iter__(self):
        self.num = 1
        return self


    def __next__(self):
        if(self.num < 30):
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration


number2 = Number2()

number2_iter = iter(number2)

for x in number2_iter:
    print(x)
