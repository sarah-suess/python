


def write_stuff(fname,string):
    strList = string.split()
    aFile = open(fname, "w")
    for word in strList:
        aFile.write(word + "\n")
        
    


write_stuff("day24miniquiz.txt","One week until Spring Break!")
