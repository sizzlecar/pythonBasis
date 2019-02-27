# Python3 I/O


# 读和写文件

# open() 将会返回一个file对象，基本语法格式如下：

# open(filename,mode)

'''
    filename : 包含了你要访问的文件名称的字符串值
    mode : 决定了打开文件的模式，只读，写入，追加等
        这个参数时非强制的，默认文件访问模式为只读


    模式	描述
    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。



'''

path = "D:\\pythonWorkSpace\\monkey-picking-peach\\source\\pygame"

file = open(path, "rb")
file.close()

# 文件对象的方法

# read(size)

'''
    read 方法将读取一定数目的数据，然后作为字符串或者字节对象返回
    size 是一个可选的数字类型的参数，当size被忽略了或者为负，那么该文件
    的所有内容都将被读取并返回


'''

#
file = open(path, "r")
content = file.read()
print(content)

# 从文件中读取单独的一行

file = open(path, "r")
line = file.readline()
print(line)

# 读取文件包含的所有的行,返回一个list
file = open(path, "r")
lines = file.readlines()
print(lines)

# 迭代文件对象

file = open(path, "r")
for line in file:
    print(line)

# write()


# write(string) 将string写如文件中，然后返回写入的字符数

file = open(path, "w")
num = file.write("今晚打老虎\n 老虎打今晚")
print(num)

# 写如一个不是字符串的东西
file = open(path, "w")
value = ('www.guantingting.cn', 22)
file.write(str(value))

# tell() 返回文件对象当前所处的位置，从文件开头开始计算起的字节数
file = open(path, "w")
file.write("xxxxx")

print(file.tell())
file.write("xxxxx2222")
print(file.tell())

# 改变文件当前的位置，seek(offset,from_what)
'''
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
    默认值为0
'''

file = open(path, "w+")
file.write('0123456789abcd')

# 从文件首行首字符开始移动5个字符
file.seek(5)
print(file.read(1))

# 从当前位置往后移动1个字符
# file.seek(1, 1)
print(file.read(1))

# 从文件的结尾往前移动1个字符
# file.seek(-1, 2)
print(file.read(1))

# 关闭资源 close()

