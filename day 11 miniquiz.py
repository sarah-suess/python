

def count_even(num):
    count = 0
    num = str(num)
    for nums in num:
        if nums in "02468":
            count += 1
    return count

print(count_even(222))
