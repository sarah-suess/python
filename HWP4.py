

#### HOMEWORK PROBLEM 4
"""
Function Name: matchPerformance
Parameters: recordTup (tup), friendRecord (dict)
Returns: rankList (list)
"""
#### SOLUTION CODE

def matchPerformance(recordTup, friendRecord):
    winCount = 0
    alist = []
    rankList = []
    for match in recordTup:
        if match == "win":
            winCount += 1
    winPercentage = ((winCount*100)//len(recordTup))
    friendRecord["Jeff"] = winPercentage
    for key,value in friendRecord.items():
        alist.append(value)
        alist.sort(reverse = True)
    for each in alist:
        for key in friendRecord:
            if friendRecord[key] == each:
                rankList.append(key)
    return rankList


#### TEST CASE

print(matchPerformance(("win", "loss", "win", "win", "loss"), {"Jake":54, "Christine":64, "Noah":35}))
# ['Christine', 'Jeff', 'Jake', 'Noah']
