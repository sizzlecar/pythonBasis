# Python3字典

'''
    字典是一种可变容器模型，且可存储任意类型对象
    字典的每个键值对用:分割，每个键值对之间用逗号分割，整个字典在花括号{}中
'''

dictionary1 = {"name": "carl", "age": 18}
dictionary2 = {22: "carl", "age": 18}

print(dictionary1)
print(dictionary2)

# Python3中的键必须是唯一的，值可以取任何数据类型，但键必须是不可变的，如字符串，数字，元组

# 访问字典里的值
print(dictionary2["age"])
print(dictionary2[22])

# 删除字典元素
del dictionary1["name"]

print(dictionary1)

# 字典值可以是任意的python对象
# 键不可以重复，后一个会把前面的键的值覆盖
# 键必须不可变，所以可以用数字，字符串，或元组




# python字典内置方法

# 删除字典内的所有元素
dictionary2.clear()

# 返回一个字典的浅复制

dictionary3 = dictionary1.copy()


# 创建一个新字典，已序列中的元素作为key,value为所有键对应的初始值

new_list = ["tom", "bob", "jack", "rick"]
new_dict = dict.fromkeys(new_list)
print(new_dict)

# 获取字典中的值
print(new_dict.get("tom"))



# 以列表返回可遍历的(键, 值) 元组数组
dict1 = {"name": "carl", "age": 18}


result = dict1.items()
print(result)

# 返回一个迭代器
print(dict1.keys())

for key in dict1.keys():
    print(dict1.get(key))

dict2 = {"address": "shanghai"}


# 字典追加字典
dict1.update(dict2)

print(dict1)


# 返回所有value的迭代器
for value in dict1.values():
    print(value)

# 删除指定的key对应的键值对

dict1.pop('name')

print(dict1)


# 随机返回并删除字典中的一堆键和值(一般删除末尾对)

dict1.popitem()

print(dict1)













