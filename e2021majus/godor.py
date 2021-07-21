
print("A program fut")

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

txtContents = readFile('melyseg.txt')
print("\n1. feladat:")
print("A file " + str(len(txtContents)) + " adatot tartalmaz")

print("\n2. feladat:")
depth = 8 # getDepth(input("Távolság: ")) #
print("A godor melysege a megadott távolságba: " + str(depth)) 

print("\n3. feladat:")
print("A talaj érintetlen része: ""{:.2f}".format(float(getUndamagedPercentage())) + "%")

print("\n5. feladat")
print("A gödrök száma: " + str(writePitsToFile()))