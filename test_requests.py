


import requests 
def testRequests(): 
  res = requests.get("https://restcountries.com/v2/name/united") 
  print("Success!") 
testRequests() 
