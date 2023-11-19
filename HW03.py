"""
Georgia Institute of Technology - CS1301
HW03 - Iterations
"""

#########################################

"""
Function Name: avgTotal()
Parameters: numString(str)
Returns: average(float)
"""

def avgTotal(numString):
    total = 0
    if len(numString) > 0:
        for nums in numString:
            total += int(nums)
        average = total / len(numString)
        return average
    elif len(numString) == 0:
        average = 0.0
        return average
    

#print(avgTotal(""))

    
"""
Function Name: safeDecoder()
Parameters: characterString(str)
Returns: passcodeString(str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: testScore()
Parameters: test1(str), test2(str)
Returns: maxPercentage(float)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: trip()
Parameters: tripTotalCost(float), bankBalance(float), interestRate(float)
Returns: months(int)
"""

def trip(tripTotalCost,bankBalance,interestRate):
    months = 0
    interestRate = interestRate * .01
    while tripTotalCost > bankBalance:
        months += 1
        bankBalance += (bankBalance * interestRate)
    return months

#print(trip(100000.0, 112.15, 2.1))



"""
Function Name: rightTriangles()
Parameters: numRows(int), character(str)
Returns: None
"""

def rightTriangles(numRows,character):
    single = character
    if numRows >= 2:
        for nums in range(numRows):
            print(character)
            character += single
    else:
        print("No Triangle")
        
#rightTriangles(1, '!')
        









