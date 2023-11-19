"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""

#########################################

"""
Function Name: dinnerTime()
Parameters: N/A
Returns: None
"""
def dinnerTime():
    entrees = int(input('How many entrees will you be ordering? '))
    drinks = int(input('How many drinks will you be ordering? '))
    cost = (4.5*drinks) + (12*entrees)
    cost = round(cost, 2)
    print('The total cost of all the meals and drinks is ${}.'.format(cost))
    
    
#########################################

"""
Function Name: bottleBonanza()
Parameters: N/A
Returns: None
"""
def bottleBonanza():
    radius = float(input('What is the radius of the water bottle? '))
    height = float(input('What is the height of the water bottle? '))
    volume = (3.14*(radius**2)*height)
    volume = round(volume, 2)
    print('The volume of the water bottle is {}.'.format(volume))
    

    
#########################################

"""
Function Name: winterBreak()
Parameters: N/A
Returns: None
"""
def winterBreak():
    episodes = int(input('How many episodes did you watch? '))
    youtubeVideos = int(input('How many YouTube videos did you watch '))
    minutes = (episodes * 40) + (youtubeVideos * 10)
    hours = minutes//60
    remain = minutes%60
    print('You spent {} hours and {} minutes watching Netflix and YouTube over winter break.'.format(hours,remain))
    
    pass

#########################################

"""
Function Name: skateboardMoney()
Parameters: N/A
Returns: None
"""
def skateboardMoney():
    allowance = int(input('How much is your monthly allowance? '))
    percent = int(input('What percentage of your allowance do you want to save? '))
    percent = percent*.01
    saved = allowance * percent
    spend = (4.40 * 30) + (5.99 * 30)
    total = spend + saved
    left = allowance - total
    left = round(left,2)
    print("You'll have ${} left to spend on your skateboard after savings and fees.".format(left))
    
    pass


