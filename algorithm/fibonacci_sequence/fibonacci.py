# 斐波那契数列

def get_fibonacci_nums(size):
    # 初始化数列1，2索引的值
    num_current = 1
    num_next = 1

    index = 1

    while index < size:
        if (index == 1 or index == 2):
            print(1)
            index += 1
            continue
        else:
            print(num_current + num_next)

        '''
        tmp = num_next
        num_next = num_current + num_next
        num_current = tmp    
        
        '''
        num_current, num_next = num_next, num_current + num_next

        index += 1



get_fibonacci_nums(10)