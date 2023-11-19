

def reduce_prices(dictionary,products):
    for item in products:
        if item in dictionary:
            price = dictionary[item]
            price = price - 1
            price = round(price,2)
            dictionary[item] = price
    return dictionary


        
print(reduce_prices({"muffin":3.99, "roll":1.99, "croissant":4.99, "bagel":2.99},["muffin", "bagel"]))

