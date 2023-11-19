
def digit_list(num):
    if num == 0:
        return ["0"]
    else:
        return digit_list(num-1) + [str(num)]


print(digit_list(3))
    
