import math
def getCylindreVolume(radius, height) :
    volume = math.pi * (radius**2) * height
    return volume
x = getCylindreVolume(10, 12)
y = getCylindreVolume(2, 6)
print(round(x,4))
print(round(y,4))
print(int(x))

def getNumberofSlices(radius, height, volumeOfSlice) :
    volume = getCylindreVolume(radius, height)
    numberOfSlices = volume / volumeOfSlice
    return int(numberOfSlices)
numslice1 = getNumberofSlices(10, 10, 100)
print (numslice1)