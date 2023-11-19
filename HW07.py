"""
Georgia Institute of Technology - CS1301
HW07 - File I/O & CSV
"""


#########################################
"""
Function Name: featureActor()
Parameters: filename (str), actorName (str)
Returns: movieList (list)
"""
def featureActor(filename, actorName):
    movieList = []
    movFile = open(filename, "r")
    header = movFile.readline()
    text = movFile.readlines()
    for index, item in enumerate(text):
        item = item.strip()
        if item == actorName:
            position = index
            movie = text[position - 1]
            movie = movie.strip()
            movieList.append(movie)
    if not movieList:
        return "Actor not found"
    return movieList


#print(featureActor("movies.txt", "Tom Holland"))

#print(featureActor("movies.txt", "Tobey Maguire"))
    

#########################################
"""
Function Name: alphabetSearch()
Parameters: filename (str), letter (str)
Returns: movieDict (dict)
"""
def alphabetSearch(filename, letter):
    movieDict = {}
    testDict = {}
    movieList = []
    num = 1
    movFile = open(filename, "r")
    header = movFile.readline()
    text = movFile.readlines()
    for index, item in enumerate(text):
        item = item.strip()
        if index == num:
            movieList.append(item)
            actor = text[index+1].strip()
            testDict[item] = actor
            num += 4
    for each in movieList:
        if each[0] == letter.lower() or each[0] == letter.upper():
            actor2 = testDict[each]
            movieDict[each] = actor2
    if not movieDict:
        return "No movie tonight"
    return movieDict


#print(alphabetSearch("movies.txt", "d"))

#print(alphabetSearch("movies.txt", "C"))
    
    
    
#########################################
"""
Function Name: favFilms()
Parameters: filename (str), movieList (list)
Returns: None (NoneType)
"""
def favFilms(filename,movieList):
    num = 1
    count = 0
    listLen = len(movieList)
    movFile = open(filename, "r")
    header = movFile.readline()
    text = movFile.readlines()
    movFile.close
    outfile = open("favMovies.txt","w")
    outfile.write("Movie Data\n\n")
    for index, item in enumerate(text):
        item = item.strip()
        if index == num:
            num += 4
            if len(movieList) == 1:
                if item in movieList:
                    actor = text[index+1].strip()
                    genre = text[index+2].strip()
                    eachList = [item,actor,genre]
                    outfile.write(item+"\n")
                    outfile.write(actor+"\n")
                    outfile.write(genre)
                    #outfile.write("\n")
                    outfile.close
            elif len(movieList) > 1:
                 if item in movieList:
                     actor = text[index+1].strip()
                     genre = text[index+2].strip()
                     eachList = [item,actor,genre]
                     outfile.write(item+"\n")
                     outfile.write(actor+"\n")
                     if (listLen - 1) == count:
                         outfile.write(genre)
                         #outfile.write("\n")
                         outfile.close
                     else: 
                         outfile.write(genre+"\n")
                         outfile.write("\n")
                         outfile.close
                         count += 1
                    



#print(favFilms("movies.txt", ["Cars 2", "Shrek"]))

#print(favFilms("movies.txt", ["Eternals"]))
    

#########################################
"""
Function Name: movieNight()
Parameters: filename (str), timeLimit (int)
Returns: movie and average rating (tuple)
"""
def movieNight(filename, timeLimit):
    movieDict = {}
    movieCSV = open(filename, "r")
    headers = movieCSV.readline()
    data = movieCSV.readlines()
    for each in data:
        eachList = each.split(",")
        time = eachList[3].strip()
        IMDB = eachList[1].strip()
        rotTom = eachList[2].strip()
        movie = eachList[0].strip()
        if int(time) <= timeLimit:
            average = ((int(IMDB) + int(rotTom)) / 2)
            movieDict[average] = movie
    averageList = list(movieDict.keys())
    averageList.sort()
    averageList.reverse()
    try:
       highest = averageList[0]
       winner = movieDict[highest]
       final = tuple([winner,highest])
    except:
        return "Can't do movie night on Friday"
    return final

    
#print(movieNight('movies.csv', 120))

#print(movieNight('movies.csv', 150))

#########################################
"""
Function Name: movieRecs()
Parameters: filename (str), interestedList (list), expectedRatio (float)
Returns: recommendations (dict)
"""
def movieRecs(filename, interestedList, expectedRatio):
    recommendations = {}
    movieCSV = open(filename, "r")
    headers = movieCSV.readline()
    data = movieCSV.readlines()
    for each in data:
        eachList = each.split(",")
        time = eachList[3].strip()
        IMDB = eachList[1].strip()
        rotTom = eachList[2].strip()
        movie = eachList[0].strip()
        if movie in interestedList:
            average = ((int(IMDB) + int(rotTom)) / 2)
            ratio = average / int(time)
            if ratio >= expectedRatio:
                recommendations[movie] = int(time)
    if not recommendations:
        return "Too many expectations"
    return recommendations
    

#print(movieRecs('movies.csv', ['Maleficent','King Richard','Divergent','La La Land','Shang-Chi and the Legend of the Ten Rings', 'Roma'], 0.6))

#print(movieRecs('movies.csv', ['Luca', 'The Social Network', 'Titanic', 'Spiderman: No Way Home', 'Enola Holmes'], 0.65))   





