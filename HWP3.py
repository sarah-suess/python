

### HOMEWORK PROBLEM 3
"""
Function Name: dinoHunter
Parameters: dinoList (list), ageList (list), dinoStr (str), ageList (list)
Returns: dinoDict (dict)
"""
#### SOLUTION CODE

def dinoHunter(dinoList, ageList, dinoStr, ageStr):
    dinoDict = {}
    i = 0
    if dinoStr not in dinoList:
        dinoList.append(dinoStr)
        ageList.append(ageStr)
    for i in range(len(dinoList)):
        dinoDict[dinoList[i]] = ageList[i]
        i+=1
    return dinoDict


#### TEST CASE

print(dinoHunter(["Stegosaurus", "T-Rex", "Triceratops"], ["100 Million", "65 Million", "80 Million"], "Velociraptor", "55 Million"))
# {'Stegosaurus': '100 Million', 'T-Rex': '65 Million', 'Triceratops': '80 Million', 'Velociraptor': '55 Million'}
