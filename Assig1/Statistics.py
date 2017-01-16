import numpy
import CircleADT

def average(circleList):
    radiusList = []
    for i in circleList:
        radiusList.append(i.radius())
    return numpy.average(radiusList)

def stdDev(circleList):
    radiusList = []
    for i in circleList:
        radiusList.append(i.radius())
    return numpy.std(radiusList)

def rank(circleList):
    radiusList = []
    for i in circleList:
        radiusList.append(i.radius())

    rank = list(radiusList)
    for i in range(1,len(radiusList)+1):
        maxR = 0
        for n,r in enumerate(radiusList):
            if r > radiusList[maxR]:
                maxR = n
        rank[maxR] = i
        radiusList[maxR] = 0
        print(circleList[maxR].radius())
    return rank
                

        
            
