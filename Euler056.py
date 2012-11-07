#Decided not to use Python's big int capabilites
#Why? Because its more fun this way!

import time
from functools import reduce

def numberToList(number):
    l = list(map(lambda x:int(x), list(str(number))))
    l.reverse()
    return l

def bigAdd(xList, yList):
    xLen = len(xList)
    yLen = len(yList)
    result = []

    carryOver = 0
    for i in range(0, max(xLen,yLen)):
        x = 0
        y = 0
        if xLen>i:
            x = xList[i]
        if yLen>i:
            y = yList[i]

        z = x + y + carryOver
        if z > 9 and i == max(xLen,yLen)-1:
            result.append(z%10)
            result.append(z//10)
        elif z > 9:
            result.append(z%10)
            carryOver = z//10
        else:
            result.append(z)
            carryOver = 0

    return result
                
    
def bigMultiply(xList, yList):
    lines=[]
    xLen = len(xList)
    yLen = len(yList)
    
    for x in range(0, xLen):
        line = []
        for i in range(0,x):
            line.append(0)
            
        carryOver = 0        
        for y in range(0, yLen):
            z = xList[x] * yList[y] + carryOver
            if z > 9 and y == yLen-1:
                line.append(z%10)
                line.append(z//10)
            elif z > 9:
                line.append(z%10)
                carryOver = z//10
            else:
                line.append(z)
                carryOver = 0

        lines.append(line)

    return reduce(lambda x,y: bigAdd(x,y),lines)                     
                       
                       
    
def bigPower(base, exponent):    
    baseList = numberToList(base)
    baseList.reverse()
    result = list(baseList)
    for i in range(1, exponent):
        result = bigMultiply(result, baseList)


    return result
                
def solve():
    result = 0
    for base in range (1,100):
        for exponent in range (1,100):
            #print(base, exponent)
            s = sum(bigPower(base, exponent))
            result = max(result, s)

    return result

def solve2():
    result = 0
    for base in range (1,100):
        for exponent in range (1,100):
            x = base ** exponent
            s = sum(numberToList(x))
            result = max(result, s)

    return result

t = time.clock()
print(solve2())
print(time.clock() - t)
