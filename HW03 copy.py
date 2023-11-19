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

def safeDecoder(characterString):
    passcodeString = ""
    count = -1
    for chars in characterString:
        count += 1
        if chars in "0123456789":
                passcodeString += str(count)
    return passcodeString
                
#print(safeDecoder("0p3n_Up_th3_$4f3!"))   
            


"""
Function Name: testScore()
Parameters: test1(str), test2(str)
Returns: maxPercentage(float)
"""

def testScore(test1,test2):
    score1 = 0
    score2 = 0
    for chars in test1:
        if chars in "012345":
            score1 += int(chars)
    score1 = (score1 / 25) * 100
    for chars in test2:
        if chars in "012345":
            score2 += int(chars)
    score2 = (score2 / 25) * 100
    if score1 > score2:
        return score1
    elif score2 > score1:
        return score2
    elif score2 == score1:
        return "Same Percentage"

#print(testScore("3_5_4_2_5", "2_5_5_2_5"))            


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
        









