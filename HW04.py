"""
Georgia Institute of Technology - CS1301
HW04 - Strings and Lists
"""

#########################################

"""
Function Name: messageDecoder()
Parameters: message (str)
Returns: decodedMessage (str)
"""
def messageDecoder(message):
    decodedMessage = ""
    for char in message:
        if char == " ":
            decodedMessage += char
        elif (char.isalpha()) == True:
            decodedMessage += char
    if not decodedMessage:
        return "No message"
    else:
        decodedMessage = decodedMessage[::-1]
    return decodedMessage

#print(messageDecoder('Ol2$l@eh'))


#########################################


"""
Function Name: clubMembers()
Parameters: interested (list), recruits (list)
Returns: memberList (list)
"""
def clubMembers(interested, recruits):
    memberList = interested
    for ppl in recruits:
        if ppl in interested:
            continue
        elif ppl not in interested:
            memberList.append(ppl)
    return memberList

#print(clubMembers(["George", "Angelina", "Parvati", "Lavender"],["Ron", "Angelina", "Colin"]))
            
    
#########################################

"""
Function Name: checkCareer()
Parameters: students (list), career (str)
Returns: selectedStudents (list)
"""
def checkCareer(students, career):
    count = 0
    selectedStudents = []
    for ppl in students:
        if students[count][1] == career:
            selectedStudents.append(students[count][0])
            count += 1
        else:
            count += 1
    return selectedStudents

#print(checkCareer([["Ginny", "Quidditch Player"], ["Luna", "Professor"],
                 #["Padma", "Professor"]], 'Quidditch Player'))

#########################################

"""
Function Name: highGrades()
Parameters: students (list), gpas (list)
Returns: honorsStudents (list)
"""
def highGrades(students, gpas):
    honorsStudents = []
    count = 0
    for gpa in gpas:
        if gpa >= 3.5:
            honorsStudents.append(students[count])
            count += 1
        else:
            count += 1
    return honorsStudents

#print(highGrades(["Harry", "Dean", "Dudley", "Cho", "Luna"], [3.4, 3.4, 2.4, 3.2, 3.2]))

#########################################

"""
Function Name: quidditchPlay()
Parameters: playOrder (list), partners (list)
Returns: isApproved (bool)
"""
def quidditchPlay(playOrder, partners):
    count = 0
    test = 2
    for player in playOrder:
        if partners[0] == player and partners[1] == playOrder[count+1]:
            return True
            test = 4
        elif partners[0] == player and partners[1] == playOrder[count-1]:
            return True
            test = 4
        else:
            count += 1
    if test == 2:
        return False

        


    
    
    

#print(quidditchPlay(['George', 'Fred', 'Harry', 'George',  'Oliver', 'Alicia'], ['Oliver', 'Harry']))
        
    





