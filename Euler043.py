import time
import math

def addDigit(digitsSoFar, digitsLeft, resultList):           
    for d in digitsLeft:
        if d!=0 or len(digitsSoFar)>0:        
            myDigitsSoFar = list(digitsSoFar)
            myDigitsLeft = list(digitsLeft)
            myDigitsSoFar.append(str(d))
            myDigitsLeft.remove(d)
            if len(myDigitsLeft) == 0:
                resultList.append(''.join(myDigitsSoFar))
            else:            
                addDigit(myDigitsSoFar, myDigitsLeft, resultList)

    return resultList
        
def getPandigital(minDigit, maxDigit):
    results = []
    digits = [i for i in range(minDigit,maxDigit+1)]
    addDigit([], digits, results)
    pandigitals = list(map(lambda x:int(x), results))
    pandigitals.sort()
    pandigitals.reverse()
    return pandigitals

def getDigitConcat(number, positionArray):    
    text = str(number)
    if len(text)!=10: print(number)
    result = ''
    for p in positionArray:
        result += text[p-1]

    return int(result)

divisors = [2,3,5,7,11,13,17]
positionDict = dict()

positionDict[2] = (2,3,4)
positionDict[3] = (3,4,5)
positionDict[5] = (4,5,6)
positionDict[7] = (5,6,7)
positionDict[11] = (6,7,8)
positionDict[13] = (7,8,9)
positionDict[17] = (8,9,10)

result = []
t = time.clock()
numbers = getPandigital(0,9)
print("Pandigitals generated")
print(time.clock()-t)

for n in numbers:
    flag = True
    for d in divisors:
        if getDigitConcat(n,positionDict[d])%d != 0:
            flag = False
            break
    if flag:
        print(n)
        result.append(n)

print("Done. Sum is ",sum(result))
print(time.clock()-t)
