"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""


#########################################
"""
Function Name: showToWatch()
Parameters: friendsFavShows (list) and favoriteShow (str)
Returns: list of friends (list)
"""
def showToWatch(friendsFavShows, favoriteShow):
    friendList = []
    for tup in friendsFavShows:
        if favoriteShow in tup[1]:
            friendList.append(tup[0])
    if not friendList:
        return "Lonely night :("
    friendList.sort()
    return friendList


'''
    for tup in friendsFavShows:
        for show in tup[1]:
            if show == favoriteShow:
                friendList.append(tup[0])
    if friendList == False:
        return "Lonely night :("
    else:
        friendList.sort()
        return friendList
    '''

#print(showToWatch([('Eric', ['Friends', 'B99']), ('Anthony', ['Money Heist','Friends']), ('Sara', ['Friends', 'Elite'])], 'Euphoria'))


#########################################
"""
Function Name: fixLabels()
Parameters: labelList (list)
Returns: list of correct labels (list)
"""
def fixLabels(labelList):
    itemList = []
    priceList =[]
    correctList = []
    for item in labelList:
        if type(item) == float:
            priceList.append(item)
        elif type(item) == str:
            itemList.append(item)
    if range(len(itemList)) == range(len(priceList)):
        for num in range(len(itemList)):
            correctList.append((itemList[num],priceList[num]))
    else:
        return "Missing Labels"
    correctList.sort()
    return correctList
    
            
           

#print(fixLabels(['oranges', 'grapes','appleS',4.00, 2.00, 'apples', 0.99, 'bananas']))
    
    
#########################################
"""
Function Name: newPlaylist()
Parameters: playlist (list)
Returns: list of songs (list)
"""
def newPlaylist(playlist):
    songlist = []
    timelist = []
    totalMin = 0
    totalSec = 0
    for (song,time) in playlist:
        songlist.append(song)
        timelist.append(time)
        songlist.sort()
    for time in timelist:
        splits = time.split(":")
        totalMin += int(splits[0])
        totalSec += int(splits[1])
    totalTime = round(totalMin + (totalSec / 60),2)
    songtup = tuple(songlist)
    newPlaylist = [ songtup, totalTime ]
    return newPlaylist

    '''
    print(totalTime)
    print(songlist)
    print(timelist)
    print(totalMin)
    print(totalSec)
    print(songtup)
    '''


#print([("All Too Well", "10:13"),
                #("Forever & Always", "3:46"),
                #("Love Story", "3:56"),
                #("Mr. Perfectly Fine", "4:38")])

#########################################
"""
Function Name: birthdays()
Parameters: friends (list) and birthdates (list)
Returns: list of names (list)
"""
def birthdays(friends, birthdates):
    endList = []
    count = 0
    import calendar
    for month,day in birthdates:
            if calendar.weekday(2022,month,day) == 5 or calendar.weekday(2022,month,day) == 6:
                endList.append(friends[count])
                count += 1
            else:
                count += 1
    endList.sort()
    return endList
                
            
#print(birthdays(['Sarra', 'Isabelle', 'Andrea'], [(12,31), (4,9), (4,8)]))

#########################################
"""
Function Name: smashBros()
Parameters: fighterList (list), opponent (str)
Returns: list of good picks (list)
"""
def smashBros(fighterList, opponent):
    final = []
    import smashData
    for fighter in fighterList:
        if fighter in counterPick(opponent):
            final.append(fighter)

    return final
            
print(smashBros(['bowser', 'marth'], 'ness'))





