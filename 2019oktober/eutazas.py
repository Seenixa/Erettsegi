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

def discountCounter(textContents):
    dataId = 0
    discountCount = 0
    freeCount = 0
    while dataId < len(textContents):
        stringSplit = textContents[dataId].split()
        if int(stringSplit[4]) > 10 and int(stringSplit[1][0:8]) <= int(stringSplit[4]):
            if stringSplit[3] == "TAB" or stringSplit[3] == "NYB":
                discountCount += 1
            if stringSplit[3] == "NYP" or stringSplit[3] == "RVS" or stringSplit[3] == "GYK":
                freeCount += 1
        dataId += 1
    return str(discountCount) + " " + str(freeCount)

def numberOfDays(year1:int, month1:int, day1:int, year2:int, month2:int, day2:int):
    month1 = (month1 + 9) % 12
    year1 = year1 - month1 / 10
    d1= 365*year1 + year1 / 4 - year1 / 100 + year1 / 400 + (month1*306 + 5) / 10 + day1 - 1
    month2 = (month2 + 9) % 12
    year2 = year2 - month2 / 10
    d2= 365*year2 + year2 / 4 - year2 / 100 + year2 / 400 + (month2*306 + 5) / 10 + day2 - 1
    napokszama = d2-d1
    return int(napokszama)

def soonToExpire(textContents):
    dataId = 0
    returnString = ""
    while dataId < len(textContents):
        stringSplit = textContents[dataId].split()
        if int(stringSplit[4]) > 10:
            year1 = int(stringSplit[1][0:4])
            month1 = int(stringSplit[1][4:6])
            day1 = int(stringSplit[1][6:8])
            year2 = int(stringSplit[4][0:4])
            month2 = int(stringSplit[4][4:6])
            day2 = int(stringSplit[4][6:8])
            if numberOfDays(year1, month1, day1, year2, month2, day2) <= 3:
                returnString += stringSplit[2] + " " + stringSplit[4][0:4] + "-" + stringSplit[4][4:6] + "-" + stringSplit[4][6:8] + "\n"            
        dataId += 1
    return returnString

def writeToFile(filename, stringToWrite):
    file = open(filename, 'w')
    file.write(stringToWrite)
    file.close

txtContents = readFile('utasadat.txt')

print("2. Feladat")
print("A buszra " + numberOfPassengers(txtContents) + " utas akart felszállni.")
print("3. Feladat")
print("A buszra " + str(invalidPassengers(txtContents)) + " utas nem szállhatott fel.")
print("4. Feladat")
print("A legtöbb utas (" + mostPassengers(txtContents)[0:2] + " fő) a " +
      mostPassengers(txtContents)[2] + ". megállóban szállt fel")
print("5. Feladat")
freeOrDiscount = discountCounter(txtContents).split()
print("Ingyenesen utazók száma: " + freeOrDiscount[1])
print("A kedvezményesen utazók száma: " + freeOrDiscount[0])

writeToFile("figyelmeztetes.txt", soonToExpire(txtContents))

input("Enterre kilép")
