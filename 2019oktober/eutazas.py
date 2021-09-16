def readFile(textfile):
    file = open(textfile, 'r')
    contents = file.readlines()
    file.close
    return contents

def numberOfPassengers(textContents):
    returnString = str(len(textContents))
    return returnString

def invalidPassengers(textContents):
    dataId = 0
    invalid = 0
    while dataId < len(textContents):
        stringSplit = textContents[dataId].split()
        if stringSplit[1][0:8] > stringSplit[4] and int(stringSplit[4]) > 10:
            invalid += 1
        if int(stringSplit[4]) == 0:
            invalid += 1
        dataId += 1
    return invalid

def mostPassengers(textContents):
    dataId = 0
    stops = 0
    biggestStop = 0
    mostPassengers = 0
    count = 0
    while stops < 30:
        while dataId < len(textContents):
            stringSplit = textContents[dataId].split()
            if int(stringSplit[0]) == int(stops):
                count += 1
            dataId += 1
        if (count > mostPassengers):
            mostPassengers = count
            biggestStop = stops
        count = 0
        dataId = 0
        stops += 1
    return str(mostPassengers) + str(biggestStop)

                
    

txtContents = readFile('utasadat.txt')

print("2. Feladat")
print("A buszra " + numberOfPassengers(txtContents) + " utas akart felszállni.")
print("3. Feladat")
print("A buszra " + str(invalidPassengers(txtContents)) + " utas nem szállhatott fel.")
print("4. Feladat")
print("A legtöbb utas (" + mostPassengers(txtContents)[0:2] + " fő) a " +
      mostPassengers(txtContents)[2] + ". megállóban szállt fel")
