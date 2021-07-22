
def readFile(textFile):
    file = open(textFile, 'r')
    contents = file.readlines()
    file.close
    return contents

def getDepth(distance):
        return txtContents[int(distance)]

def getUndamagedPercentage():
    undamaged = 0
    for x in txtContents:
        if int(x) == 0:
            undamaged += 1
    return float(undamaged / len(txtContents) * 100)

def getPitStartingPoint(startingPoint):
    if startingPoint == None:
        return None
    if startingPoint >= len(txtContents):
        return None
    for x in range(startingPoint, len(txtContents)):
        if int(txtContents[x]) != 0 and int(txtContents[x - 1]) == 0:
            return x
        if x == len(txtContents):
            return None

def getPitDepths(startingPoint, file):
    if startingPoint == None:
        return None
    depthAtDistance = ""
    distance = startingPoint
    while int(getDepth(distance)) != 0:
        depthAtDistance += str(getDepth(distance).rstrip("\n") + " ")
        if int(getDepth(distance + 1)) == 0:
            file.write(depthAtDistance)
            file.write("\n")
        if distance + 1 != len(txtContents):
            distance += 1
        else:
            break
    return distance

def writePitsToFile():
    loop = 0
    numberOfHoles = 0
    file = open("godor.txt", "w")
    while getPitStartingPoint(loop) != None:
        loop = getPitDepths(getPitStartingPoint(loop), file)
        numberOfHoles += 1
    file.close
    return numberOfHoles

def checkIfPit(atDistance):
    if int(getDepth(atDistance)) == 0:
        return "Az adott helyen nincs gödör."
    else: return ""

def getPitStartFromMiddle(fromDistance):
    if checkIfPit(fromDistance) == "":
        distance = int(fromDistance)
        while int(getDepth(distance - 1)) != 0:
            distance -= 1
            if distance <= 0:
                return
        return distance + 1

def getPitEndFromMiddle(fromDistance):
    if checkIfPit(fromDistance) == "":
        distance = int(fromDistance)
        while int(getDepth(distance + 1)) != 0:
            distance += 1
            if distance == len(txtContents):
                return
        return distance + 1

def checkMonotonity(pitStart, pitEnd):
    distance = pitStart
    while int(getDepth(distance)) <= int(getDepth(distance + 1)):
        distance += 1
    if int(getDepth(distance + 1)) < int(getDepth(distance)):
        monotonityFromStart = distance
    distance = pitEnd
    while int(getDepth(distance)) <= int(getDepth(distance - 1)):
        distance -= 1
    if int(getDepth(distance - 1)) < int(getDepth(distance)):
        monotonityFromEnd = distance
    if monotonityFromStart > monotonityFromEnd:
        return True
    else:
        return False

def getMaxDepth(pitStartingPoint):
    maxDepth = 0
    distance = pitStartingPoint
    while int(getDepth(distance)) != 0:
        if int(getDepth(distance)) > maxDepth:
            maxDepth = int(getDepth(distance))
        distance += 1
    return maxDepth
     
def getPitVolume(pitStartingPoint):
    volume = int(getDepth(pitStartingPoint)) * 10
    distance = pitStartingPoint
    while int(getDepth(distance)) != 0:
        volume += int(getDepth(distance)) * 10
        distance += 1
    return volume

def getWaterVolume(pitStartingPoint):
    volume = (int(getDepth(pitStartingPoint)) - 1) * 10
    distance = pitStartingPoint
    while int(getDepth(distance)) != 0:
        volume += (int(getDepth(distance)) - 1) * 10
        distance += 1
    return volume

txtContents = readFile('melyseg.txt')
print("\n1. feladat:")
print("A file " + str(len(txtContents)) + " adatot tartalmaz")

print("\n2. feladat:")
getDistance = input("Távolság: ")
if int(getDistance) > len(txtContents) or int(getDistance) < 0:
    getDistance = '7'
    print("A kért adat az adott helyről nincs megadva. Alapérték: 7")
depth = getDepth(getDistance) 
print("A godor melysege a megadott távolságba: " + str(depth)) 

print("\n3. feladat:")
print("A talaj érintetlen része: ""{:.2f}".format(float(getUndamagedPercentage())) + "%")

print("\n5. feladat")
print("A gödrök száma: " + str(writePitsToFile()))

print("\n6. feladat:")
print(checkIfPit(getDistance))
if checkIfPit(getDistance) == "":
    print("a)")
    print("A gödör " + str(getPitStartFromMiddle(getDistance)) + " méternél kezdődik és " + str(getPitEndFromMiddle(getDistance)) + " méternél ér véget.")

    print("\nb)")
    if checkMonotonity(getPitStartFromMiddle(getDistance), getPitEndFromMiddle(getDistance)):
        print("Folyamatosan Mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    print("\nc)")
    print("A gödör legnagyobb mélysége: "  + str(getMaxDepth(getPitStartFromMiddle(getDistance))))

    print("\nd)")
    print("A gödör térfogata: " + str(getPitVolume(getPitStartFromMiddle(getDistance))) + " m^3")

    print("\ne)")
    print("A gödör vízbefogadó képessége: " + str(getWaterVolume(getPitStartFromMiddle(getDistance))) + " m^3")

input("Enterre kilép.")