import time
import math

def isPrime(n):
    flag = True
    if n == 1:
        flag = False
    elif n in [2,3,5,7]:
        flag = True
    elif n%2==0:
        flag = False
    elif n%3 == 0:
        flag = False
    else:  
        r = math.floor(math.sqrt(n))
        f = 5
        while (f<=r):
            if n%f==0:
                flag = False                
                break
            if n%(f+2)==0:
                flag = False                
                break
            f+=6

    return flag

def addDigit(digitsSoFar, digitsLeft, resultList):           
    for d in digitsLeft:
        myDigitsSoFar = list(digitsSoFar)
        myDigitsLeft = list(digitsLeft)
        myDigitsSoFar.append(str(d))
        myDigitsLeft.remove(d)
        if len(myDigitsLeft) == 0:
            resultList.append(''.join(myDigitsSoFar))
        else:            
            addDigit(myDigitsSoFar, myDigitsLeft, resultList)

    return resultList
        
def getPandigital(maxDigit):
    results = []
    digits = [i for i in range(1,maxDigit+1)]
    addDigit([], digits, results)
    pandigitals = list(map(lambda x:int(x), results))
    pandigitals.sort()
    pandigitals.reverse()
    return pandigitals

def solve():
    t = time.clock()
    for n in range (9,1,-1):
        print('getting pandigitals for n=',n)
        pandigitals=getPandigital(n)
        print('Done',time.clock()-t)
        for p in pandigitals:
            if isPrime(p):
                print('Result is ',p)
                print(time.clock()-t)
                return
   
        
solve()
