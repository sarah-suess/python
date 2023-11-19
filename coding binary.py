

def convert(string):
    total = 0
    string = string[::-1]
    for index, value in enumerate(string):
        if value == "1":
            total += 2 ** index
    return total
    


print(convert("101"))
            
