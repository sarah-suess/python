"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""


#########################################
"""
Function Name: pageNumbers()
Parameters: bookList (list)
Returns: total (int)
"""
def pageNumbers(bookList):
    if bookList == []:
        return 0
    else:
        return bookList[0] + pageNumbers(bookList[1:])
    
#print(pageNumbers([199, 434, 210]))
#print(pageNumbers([342, 145, 302]))


#########################################
"""
Function Name: letterPyramid()
Parameters: letter (str), rows (int)
Returns: None (NoneType)
"""
def letterPyramid(letter, rows):
    import string
    if letter in string.ascii_lowercase:
        if rows == 0:
            return ''
        else:
            letterPyramid(letter, rows - 1)
            print(letter * rows)
    
#letterPyramid("a", 6)
#letterPyramid("S", 6)
  
#########################################
"""
Function Name: specialChar()
Parameters: usernames (list)
Returns: aDict (dict)
"""
def specialChar(usernames):
    count = 0
    if usernames == []:
        return {}
    else:
        aDict = specialChar(usernames[1:])
        each = usernames[0]
        for char in each:
            if char in ".-_!~#":
                count += 1
            aDict[each] = count
        return aDict

        

#print(specialChar(["cra1g_da_g0at", "arush1-f0r-da-w1n", "RAMya!", "pa1g3L#md"]))
#print(specialChar(["aryan", "fareeda4firstplace!!", "audrey.all.over.the.world"]))

#########################################
"""
Function Name: messageDecoder()
Parameters: hiddenMessage (str), characters (str)
Returns: decodedMessage (str)
"""
def messageDecoder(hiddenMessage, characters):
    if len(hiddenMessage) == 0:
        return ''
    elif hiddenMessage[0] in characters:
        return messageDecoder(hiddenMessage[1:], characters)
    else:
        return hiddenMessage[0] + messageDecoder(hiddenMessage[1:], characters)
        

#print(messageDecoder("zdzi)N$nez)r @z) $WiLzla$Ge?z", "z$)"))
#print(messageDecoder("5tcudy#incg Isn t&He# l1b#racRy&!", "c#s&"))

#########################################
"""
Function Name: stringCombiner()
Parameters: stringList (list)
Returns: combinedString (str)
"""
def stringCombiner(stringList):
    if stringList == [] or stringList ==():
        return ''
    else:
        if type(stringList[-1]) == str:
            return stringCombiner(stringList[:-1]) + stringList[-1]
        else:
            return stringCombiner(stringList[:-1]) + stringCombiner(stringList[-1])
                            
                
                   


#print(stringCombiner([["Ramblin "],("Wreck"),"!"]))
#print(stringCombiner(["cs 1", ("301 i",[]), "s awes", ["ome!"]]))









