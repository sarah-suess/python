"""
Georgia Institute of Technology - CS1301
HW08 - API
"""


#########################################
"""
Function Name: highestPopulation()
Parameters: regionalBloc (str)
Returns: country with highest population (str)
"""
def highestPopulation(regionalBloc):
    poplist = []
    import requests
    baseurl = "https://restcountries.com/v2/regionalbloc/"
    fullurl = baseurl + regionalBloc
    r = requests.get(fullurl)
    data = r.json()
    for each in data:
        population = each['population']
        country = each['name']
        trytup = (population,country)
        poplist.append(trytup)
        poplist.sort()
    length = len(poplist)
    highest = poplist[length - 1]
    final = highest[1]
    return final
    
#print(highestPopulation('eu'))

#########################################
"""
Function Name: commonTimeZones()
Parameters: code1(str) , code2(str)
Returns: list of common time zones (list)
"""
def commonTimeZones(code1, code2):
    mutlist = []
    import requests
    baseurl = "https://restcountries.com/v2/alpha/"
    fullurl1 = baseurl + code1
    fullurl2 = baseurl + code2
    r1 = requests.get(fullurl1)
    r2 = requests.get(fullurl2)
    data1 = r1.json()
    data2 = r2.json()
    timelist1 = data1["timezones"]
    timelist2 = data2["timezones"]
    for each in timelist1:
        if each in timelist2:
            mutlist.append(each)
    if not mutlist:
        return "No Common Time Zones"
    return mutlist
    
        
#commonTimeZones('rus', 'chn')
    
    
#########################################
"""
Function Name: registerDomains()
Parameters: companyName (str), countryList (list)
Returns: list of domain names (list)
"""
def registerDomains(companyName, countryList):
    domainlist = []
    length = len(countryList)
    import requests
    baseurl = "https://restcountries.com/v2/name/"
    for country in countryList:
        try:
            fullurl = baseurl + country
            r = requests.get(fullurl)
            data = r.json()
            for each in data:
                domain = each["topLevelDomain"]
                domain = domain[0]
                site = companyName.lower() + domain
                domainlist.append(site)
        except:
            length -= 1
            continue
    if len(domainlist) > length:
        domainlist = domainlist[:length]
    
    return domainlist

        

#print(registerDomains('Amazon', ['germany', 'narnia', 'mexico', 'hogwarts']))
#print(registerDomains('Google', ['france', 'japan', 'canada']))
#print(registerDomains('Apple', ['tatooine', 'iceland', 'hungary', 'ireland']))
#print(registerDomains('Apple', ['hungary', 'ireland']))    

#########################################
"""
Function Name: findCountry()
Parameters: capitalList (list)
Returns: Dictionary mapping each capital to its country(dict)
"""
def findCountry(capitalList):
    countryDict = {}
    import requests
    baseurl = "https://restcountries.com/v2/capital/"
    for capital in capitalList:
        fullurl = baseurl + capital
        r = requests.get(fullurl)
        data = r.json()
        for each in data:
            country = each['name']
            countryDict[capital] = country
    return countryDict

#print(findCountry(['tokyo', 'delhi', 'stockholm']))
#print(findCountry(['paris', 'canberra', 'copenhagen']))


#########################################
"""
Function Name: commonLanguages()
Parameters: regionalBloc (str)
Returns: most common language (str) or languages (list)
"""
def commonLanguages(regionalBloc):
    mostCommon = []
    langDict = {}
    import requests
    baseurl = "https://restcountries.com/v2/regionalbloc/"
    fullurl = baseurl + regionalBloc
    r = requests.get(fullurl)
    data = r.json()
    for each in data:
        lanList = each['languages']
        for item in lanList:
            language = item['name']
            if language not in langDict:
                langDict[language] = 1
            if language in langDict:
                langDict[language] += 1
    tupList = list(langDict.items())
    tupList.sort(key = lambda x: x[1],reverse=True)
    initial = tupList[0][1]
    for lang, value in tupList:
        if value == initial:
            mostCommon.append(lang)
        else:
            continue
    if len(mostCommon) > 1:
        mostCommon.sort()
        return mostCommon
    else:
        language = mostCommon[0]
        return language
    
        

#print(commonLanguages('cais'))
#print(commonLanguages('eu'))






    

