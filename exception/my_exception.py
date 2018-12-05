
# 用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)



try:
    raise MyError(22222)
except MyError as my_error:
    print(my_error)



# 预定义的清理行为

'''
 一些对象定义了标准的清理行为，无论系统是否成的使用了它，一旦不需要了，
 那么这个标准的清理行为就会执行
'''

path = "C:\\Users\\Administrator\\Desktop\\今晚打老虎.txt"

# with语句可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open(path, "rb+") as file:
    for str in file.readlines():
        print(str)
