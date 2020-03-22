def linefind(filename, s, encoding='UTF-8'):
    textaskjal = open(filename,'r') #opna file
    linenumber = 1 #skilgreini linenumber
    items = [] #bý til tómt fylki

    for line in textaskjal.readlines(): #finna línur í file
        if s in line: #finna línur með streng
            items.insert(linenumber, linenumber) #setja línunúmerin í fylkið
        linenumber+=1 #hækka línutal
    textaskjal.close() #loka file

    return(items) #skila fylkinu
