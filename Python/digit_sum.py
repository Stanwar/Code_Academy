def digit_sum(x):
    length = len(str(x))
    add = 0 
    num = x
    for i in range(length):
        num = num%10 
        add = add + num
        print add
        x = x//10
        num = x 
    return add