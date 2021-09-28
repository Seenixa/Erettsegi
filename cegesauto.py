def readFile(fileName):
    file = open(fileName, 'r')
    txtContents = file.readlines()
    return txtContents

def lastCarOut(textCont):
    lastLine = textCont[len(textCont) - 1].split()
    lastDay = lastLine[0]
    lastCar = lastLine[2]
    return lastDay + " " + lastCar

def getDayInfo(textCont, day):
    dataId = 0
    returnString = ""
    while dataId < len(textCont):
        splitLine = textCont[dataId].split()
        if int(splitLine[0]) == int(day):
            returnString += splitLine[1] + " " + splitLine[2] + " " + splitLine[3] + " "
            if splitLine[5] == "0":
                returnString += "ki" + "\n"
            else:
                returnString += "be" + "\n"
        dataId += 1
    return returnString

def notReturned(textCont):
    dataId = len(textCont) - 1
    carId = 300
    isOut = 0
    while carId >= 300 and carId < 310:
        splitLine = textCont[dataId].split()
        if splitLine[2] == ("CEG" + str(carId)):
            carId += 1
            if splitLine[5] == "0":
                isOut += 1
        dataId -= 1
    return str(isOut)

def distanceTraveled(textCont):
    dataId = 0
    returnString = ""
    traveledMin = 0
    traveledMax = 0
    carId = 300
    while carId >= 300 and carId < 310:
        while dataId < len(textCont):
            splitLine = textCont[dataId].split()
            if splitLine[2] == ("CEG" + str(carId)):
                if traveledMin == 0:
                    traveledMin = int(splitLine[4])
                if int(splitLine[4]) > traveledMax:
                   traveledMax = int(splitLine[4])
            dataId += 1
        returnString += "CEG" + str(carId) + " " + str(traveledMax - traveledMin) + " km\n"
        carId += 1
        traveledMin = 0
        traveledMax = 0
        dataId = 0
    return returnString

def distanceSingle(textCont):
    dataId = 0
    returnString = ""
    carId = 300
    carStarted = False
    travelStart = 0
    travelEnd = 0
    travelDistance = 0
    maxTravelDistance = 0
    while carId >= 300 and carId < 310:
        while dataId < len(textCont):
            splitLine = textCont[dataId].split()
            if splitLine[2] == ("CEG" + str(carId)):
                if splitLine[5] == "0" and carStarted == False:
                    travelStart = int(splitLine[4])
                    carStarted = True
                if splitLine[5] == "1" and carStarted == True:
                    travelEnd = int(splitLine[4])
                    travelDistance = travelEnd - travelStart
                    travelStart = 0
                    travelEnd = 0
                    carStarted = False
            if travelDistance > maxTravelDistance:
                maxTravelDistance = travelDistance
                returnString = "Leghosszabb út: " + str(maxTravelDistance) + " km, személy: " + splitLine[3]
            dataId += 1
        carId += 1
        travelStart = 0
        travelEnd = 0
        carStarted = False
        dataId = 0
    return returnString
                    
def writeJourneyInfo(textCont, plateNumber):
    file = open(str(plateNumber) + "_menetlevel.txt", 'w')
    carId = plateNumber[3:6]
    dataId = 0
    stringToWrite = ""
    while dataId < len(textCont):
        splitLine = textCont[dataId].split()
        if splitLine[2] == ("CEG" + carId):
            if splitLine[5] == "0":
                stringToWrite += splitLine[3] + "\t" + splitLine[0] + ".\t" + splitLine[1] + "\t" + splitLine[4] + "\tkm\t"
            if splitLine[5] == "1":
                stringToWrite += splitLine[0] + ".\t" + splitLine[1] + "\t" + splitLine[4] + "\tkm\n"
        dataId += 1        
    file.write(stringToWrite)
    file.close
    return "Menetlevél kész."
                

#1. Feladat
textContents = readFile('autok.txt')

#2. Feladat
print("2. Feladat")
lastCarInfo = lastCarOut(textContents).split()
print(lastCarInfo[0] + ". nap rendszám: " + lastCarInfo[1] + "\n")

#3. Feladat
print("3. Feladat")
userInput = input("Nap: ")
while(int(userInput) > 30 or int(userInput) <= 0):
    print("A megadott érték helytelen: " + userInput)
    print("Egy 1 és 30 kozotti számra van szükség.")
    userInput = input("Nap: ")
print("Forgalom a(z) " + userInput + ". napon:")
print(getDayInfo(textContents, userInput))

#4. Feladat
print("4. Feladat")
print("A hónap végén " + notReturned(textContents) + " autót nem hoztak vissza.\n")

#5. Feladat
print("5. Feladat")
print(distanceTraveled(textContents))

#6. Feladat
print("6. Feladat")
print(distanceSingle(textContents))

#7. Feladat
print("7. Feladat")
licensePlateNumber = input("Rendszám: ")
if int(licensePlateNumber[3:6]) > 310:
    print("szar rendszámot adtál")

print(writeJourneyInfo(textContents, licensePlateNumber))

input("\nProgram vége. Enterre kilép.")
