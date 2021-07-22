def readFromFile(fileName):
    file = open(fileName, "r")
    txtContents = file.readlines()
    return txtContents

def getTimesOfDates(allDataFromFile):
    knownDates = 0
    index = 0
    while index < len(allDataFromFile):
        if allDataFromFile[int(index)] != "NI\n":
            knownDates += 1
        index += 5
    return knownDates

def getWatchedPercentage(allDataFromFile):
    seen = 0.0
    index = 4
    while index < len(allDataFromFile):
        if allDataFromFile[int(index)] == "1\n":
            seen += 1.0
        index += 5
    return float(seen) / float((len(allDataFromFile) / 5)) * 100

def getTimeSpentWatching(allDataFromFile):
    minutes = 0
    index = 3
    while index < len(allDataFromFile):
        if int(allDataFromFile[int(index + 1)]) == 1:
            minutes += int(allDataFromFile[int(index)])
        index += 5
    days = int(minutes / 1440)
    hours = int((minutes % 1440) / 60)
    minutes -= int(days * 1440)
    minutes -= int(hours * 60)
    return str(days) + " napot " + str(hours) + " órát és " + str(minutes) + "percet "

def getIndexToDates(date, allDataFromFile):
    year = int(date[0] + date[1] + date[2] + date[3])
    month = int(date[5] + date[6])
    day = int(date[8] + date[9])
    index = 0
    returnString = ""
    def compareDates():
        if year > releaseYear:
            return True
        elif year == releaseYear and month > releaseMonth:
            return True
        elif year == releaseYear and month == releaseMonth and day >= releaseDay:
            return True
        else: return False
    while index < len(allDataFromFile):
        releaseDate = allDataFromFile[int(index)]
        if len(releaseDate) != 11 and releaseDate != "NI\n":
            return returnString
        if releaseDate != "NI\n":
            releaseYear = int(releaseDate[0] + releaseDate[1] + releaseDate[2] + releaseDate[3])
            releaseMonth = int(releaseDate[5] + releaseDate[6])
            releaseDay = int(releaseDate[8] + releaseDate[9])
            if allDataFromFile[int(index + 4)] == "0\n":
                if compareDates():
                    returnString += str(allDataFromFile[int(index + 2)]).rstrip("\n") + "\t" + str(allDataFromFile[int(index + 1)]).rstrip("\n") + "\n"
        index += 5
    return returnString

# 1. feladat #
txtContents = readFromFile("lista.txt")

# 2. feladat
print("\n2. Feladat")
print("A listában " + str(getTimesOfDates(txtContents)) + " vetítési dátummal rendelkező epizód van.")

# 3. feladat #
print("\n3. Feladat")
print("A listában levő epizódok ""{:.2f}".format(float(getWatchedPercentage(txtContents))) + "%-át látta.")

# 4. feladat #
print("\n4. Feladat")
print("Sorozatnézéssel " + getTimeSpentWatching(txtContents) + " töltött.")

# 5. feladat #
print("\n5. Feladat")
getDateInput = ""
while len(getDateInput) != 10:
    getDateInput = input("Adjon meg egy dátumot! Dátum=")
print(getIndexToDates(getDateInput, txtContents))