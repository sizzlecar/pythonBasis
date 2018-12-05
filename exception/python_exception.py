import sys

# 错误和异常

'''

while True:
    try:
        x = int(input("Enter a number,please: "))
        print("you enter number is: ", x)
    except ValueError:
        print("That was no vaild number. try again ")
    finally:
        print("Finally is running")
'''

try:
    file = open("C:\\Users\\Administrator\\Desktop\\new.txt")
    s = file.readline()
    i = int(s.strip())
except OSError as os:
    print("OSError", os)
except ValueError as value:
    print("ValueError", value)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
