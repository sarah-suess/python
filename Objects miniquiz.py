class Farmer:
    def __init__(self,n):
        self.name = n
        self.animal_list = []
    def __str__(self):
        return "Farmer {} has {} animals total".format(self.name, len(self.animal_list))
    def add_stock(self,animal):
        self.animal_list.append(animal)
    def num_cows(self):
        total = 0
        for animal in self.animal_list:
            if animal.animal_type == "cow":
                total += 1
        return total
    


class Animal:
    def __init__(self,t):
        self.animal_type = t
    def __str__(self):
        return "This animal is a {}".format(self.animal_type)
    

# testing code
bessy= Animal("cow")
bossy = Animal("cow")
flicker = Animal("horse")
farmer = Farmer("McDaniel")
farmer.add_stock(bessy)
farmer.add_stock(bossy)
farmer.add_stock(flicker)
print(farmer) # Should print Farmer McDaniel has 3 animals total.
print(farmer.num_cows())  # should print 2 
