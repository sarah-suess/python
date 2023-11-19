"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: workout()
Parameters: exerciseName (str), interestedFriends (int), totalFriends (int)
Returns: None (NoneType)
"""
def workout(exerciseName,interestedFriends,totalFriends):
    percent = (int(interestedFriends) / int(totalFriends)) * 100
    if percent < 20.0:
     print("Let's try a different workout.")
    elif percent >= 20.0 and percent < 70.0:
     print("We will try to " + exerciseName + " for 30 minutes.")
    else:
     print("We are so excited to " + exerciseName + "!")

#workout("dance",1,10)
    
#########################################

"""
Function Name: iceCream()
Parameters: rating (float), distance (float)
Returns: choice (str)
"""

choice = " "

def iceCream(rating,distance):
    if distance == 7.5 and rating >= 4.5:
     choice = "Jeni's"
    elif distance == 3.6 and rating >= 4.5:
     choice = "Cold Stone"
    elif distance == 4.2 and rating >= 4.5:
     choice = "Morelli's"
    elif distance == 1.3 and rating >= 4.0:
     choice = "Bruster's"
    elif distance == 6.4 and rating >= 4.0:
     choice = "Sweet Stack"
    elif distance == 2.8 and rating >= 3.5:
     choice = "Baskin Robbins"
    else:
     choice = "Try again tomorrow."
    return choice


#print(choice)

    
#########################################

"""
Function Name: restaurantDecider()
Parameters: veganFriendly (bool), yelpStars (int), milesAway (int)
Returns: decisionStr (str)
"""

decisionStr = " "

def restaurantDecider(veganFriendly,yelpStars,milesAway):
    if veganFriendly == False:
     decisionStr = "Not tonight."
    elif veganFriendly == True and yelpStars < 3:
     decisionStr = "Not good enough food."
    elif veganFriendly == True and yelpStars >= 3 and milesAway > 5:
     decisionStr = "Too far!"
    elif veganFriendly == True and yelpStars >= 3 and milesAway <= 5:
     decisionStr = "Perfect restaurant!"
    return decisionStr

#print(decisionStr)

#########################################

"""
Function Name: dinnerTip()
Parameters: numFriends (int), dinnerCost (float)
Returns: tipAmount (float)
"""

tipAmount = 0

def dinnerTip(numFriends,dinnerCost):
    if numFriends <= 3:
     tipAmount = dinnerCost * .15
    elif numFriends > 3 and numFriends <= 7:
     tipAmount = dinnerCost * .20
    elif numFriends > 7:
     tipAmount = dinnerCost * .25

    tipAmount = round(tipAmount,2)
    return tipAmount

#print(tipAmount)

#########################################

"""
Function Name: planMaker()
Parameters: timeA (float), costA (int), timeB (float), costB (int)
Returns: planDecision (str)
"""

planDecision = " "

def planMaker(timeA,costA,timeB,costB):
    if costA > costB:
     planDecision = "planB"
    elif costB > costA:
     planDecision = "planA"
    elif costB == costA and timeA > timeB:
     planDecision = "planB"
    elif costB == costA and timeB > timeA:
     planDecision = "planA"
    elif timeA == timeB and costA == costB:
     planDecision = "No plans this weekend."
    return planDecision

#print(planDecision)







