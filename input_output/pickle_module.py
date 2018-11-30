# pickle模块
import pickle

'''
    python 的pickle 模块实现了基本的数据序列化和反序列化
    通过pickle 模块的序列化操作我们能将程序中运行的对象信息保存到文件中去，永久存储
    通过pickle 模块的反序列化操作，我么能够从文件中创建上一次程序保存的对象

'''

# pickle.dump(obj, file, [,protocol])

text = {
    "a": [1, 2, 23, 4],
    "b": "name",
    "c": (1, 2, 3.222, 4),
    "d": None
}

path = "C:\\Users\\Administrator\\Desktop\\new.txt"
file = open(path, "wb")
# 乱码
pickle.dump(text, file)
