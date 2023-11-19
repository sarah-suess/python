"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries adn Try/Except Blocks
"""

#########################################

"""
Function Name: findTicket()
Parameters: ticketDictionary (dict)
Returns: cheapestTicket (tuple)
"""
def findTicket(ticketDictionary):
    if not ticketDictionary:
        return "No tickets available!"
    values = list(ticketDictionary.values())
    keys = list(ticketDictionary.keys())
    prices = list(values)
    prices.sort()
    cheapest = prices[0]
    position = values.index(cheapest)
    airline = keys[position]
    cheapestTicket = tuple([airline,cheapest])
    return cheapestTicket

#print(findTicket({ "Air Canada" : 722, "Alaska" : 931 , "jetBlue": 871}))


#print(findTicket({ "Air Seoul" : 700, "Asiana Airlines" : 500, "China Eastern" : 900, "Frontier" :1000}))

#########################################

"""
Function Name: findHotel()
Parameters: hotelDictionary (dict)
Returns: preferredHotel (dict)
"""

def findHotel(hotelDictionary):
    preferredHotel = {}
    total = 1
    testList = []
    winner = ""

    for name in hotelDictionary:
        vote = hotelDictionary[name]
        if vote not in testList:
            testList.append(vote)
        else:
            total += 1
            winner = vote
    if total == 4:
        total = total - 1       
    if len(hotelDictionary) == 1:
            preferredHotel[vote] = 1
            total = 5
    else:
        preferredHotel[winner] = total
    
    if total <= 1:
        return "No hotels available!"

    return preferredHotel


"""
def findHotel(hotelDictionary):
    preferredHotel = {}
    count = 0
    hotels = list(hotelDictionary.values())
    hotelSet = list(set(hotels))
    loss = len(hotels) - len(hotelSet)
    total = loss + 1
    for hotel in hotels:
        if hotels[count] == hotelSet[count]:
            count += 1
        else:
            winner = hotels[count]

    if total <= 0:
        return "No hotels available!"

    preferredHotel[winner] = total
    return preferredHotel
"""

    
#print(findHotel({"Arvin" : "Grand Hyatt Beijing", "Craig" : "Grand Millennium Beijing","Josh": "Grand Hyatt Beijing"}))    

#print(findHotel({"Naomi" :  "Beijing Marriott Hotel","Paige" : "Beijing Marriott Hotel","Ramya" : "Beijing Marriott Hotel","Cynthia" : "The Bulgari Hotel"}))

#print(findHotel({'Craig': 'Beijing Marriott Hotel', 'Arushi': 'The Bulgari Hotel', 'Ramya': 'Beijing Marriott Hotel', 'Cynthia': 'The Bulgari Hotel', 'Josh': 'Beijing Marriott Hotel'}))

#print(findHotel({'Craig': 'Beijing Marriott Hotel', 'Arushi': 'The Bulgari Hotel', 'Ramya': 'Beijing Marriott Hotel', 'Cynthia': 'The Bulgari Hotel', 'Josh': 'Beijing Marriott Hotel'}))
    
#########################################

"""
Function Name: findEvent()
Parameters: myInterests (list), schedule (dict)
Returns: match (list)
"""


def findEvent(myInterests, schedule):
    matchList = []
    for key in schedule:
        dayList = schedule[key]
        for event in dayList:
            if event in myInterests:
                matchList.append(key)
    matchList = list(set(matchList))
    matchList.sort()
    return matchList

    
#print(findEvent(["Skiing","Snowboard","Curling"], {"Feb 18" : ["Skiing","Snowboard","Luge"],"Feb 19" : ["Skeleton", "Ski Jumping"],"Feb 20" : ["Skiing","Curling"]}))

#print(findEvent(["Luge","Ski Jumping","Figure Skating"], {"Feb 18" : ["Skiing","Snowboard","Luge"], "Feb 19" : ["Skeleton", "Ski Jumping"],"Feb 20" : ["Skiing","Curling"]}))


#########################################

"""
Function Name: figureSkating()
Parameters: technicalScores (list), componentScores (list)
Returns: finalScores (list)
"""
def figureSkating(technicalScores, componentScores):
    total = 0
    finalScores = []
    for num in range(len(technicalScores)):
        try:
            total = (technicalScores[num] + componentScores[num])
            finalScores.append(total)
        except:
            continue
    return finalScores

#print(figureSkating([100, "&", 110, 130, 110],["*", 120, 110, 130, 130]))

#print(figureSkating([180, ["Hi"], 150, 120, 100],[80, 90, None, 120, 110]))


#########################################

"""
Function Name: sportManagement()
Parameters: countryDict (dict)
Returns: sportDict (dict)
"""
def sportManagement(countryDict):
    singleList = []
    sportDict = {}
    sportsList = list(countryDict.values())
    for lists in sportsList:
        for event in lists:
            if event not in singleList:
                singleList.append(event)
            else:
                continue
    items = list(countryDict.items())

    for sport in singleList:
        for country,listy in items:
            if sport in listy:
                if sport not in sportDict:
                    sportDict[sport] = [country]
                else:
                    sportDict[sport].append(country)
    for sports in sportDict:
        countryList = sportDict[sports]
        countryList.sort()
        sportDict[sports] = countryList
    return sportDict


#print(sportManagement({"Belarus": ["Ice Hockey", "Skiing"], "Lebanon": ["Skiing", "Snowboard"],"Denmark":["Skiing", "Luge"]}))

#print(sportManagement({'Japan': ['Skiing', 'Ice Hockey'],'Taiwan': ['Skiing', 'Snowboard'],'Romania': ['Bobsleigh', 'Luge', 'Skeleton']}))








