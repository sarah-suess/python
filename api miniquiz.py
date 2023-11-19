

def getting_warmer(woeid):
    import requests
    baseurl = "http://www.metaweather.com/api/location/"
    fullurl = baseurl + woeid
    r = requests.get(fullurl)
    data = r.json()
    print(data.keys())
    tempList = data["consolidated_weather"]
    todayDict = tempList[0]
    tomDict = tempList[1]
    maxtoday = todayDict['max_temp']
    maxtom = tomDict['max_temp']
    if maxtom > maxtoday:
        return True
    
print(getting_warmer("2352824"))
print(getting_warmer("2357024"))
    
