#http://pastebin.com/qY4kJrUp
#************************* Euler031.py ***********************************************
from math import *

def breakIntoSmallerBits(amount, coin, usedCoins, smallerBits):        
    global count
    myAmount = amount
    myUsedCoins = list(usedCoins)
    
    if coin > 0:        
        myAmount -= coin
        myUsedCoins.append(coin)

    if myAmount == 0:
        count+=1        
    else:
        for newCoin in [c for c in smallerBits if c<=amount and c>=coin]:
            breakIntoSmallerBits(myAmount, newCoin, myUsedCoins, smallerBits)
    
    return count

def countBreaks(amount, smallerBits):
    global count 
    count = 0
    breakIntoSmallerBits(amount,0,[],smallerBits)
    return count
#*************************************************************************************






#************************** HelperMath.py ********************************************
def Eratosthenes(roof):
    candidates = [x for x in range(2, roof)]
    strikeOut = {x: False for x in candidates}
   
    while True:
        p = min(candidates)
        if p**2 > roof:
            break
        m = 2
        x = p*m
        while x<roof:
            strikeOut[x] = True
            m+=1
            x= p*m
       
        candidates = [x for x in candidates[1:] if not strikeOut[x]]
       
    return [x for x in strikeOut.keys() if not strikeOut[x]]

PartitionPCache = dict()

def PartitionP(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n in PartitionPCache:
        return PartitionPCache[n]
    
    result=0    
    for k in range(1, int(n)+1):
        n1 = n - k * (3 * k - 1) / 2
        n2 = n - k * (3 * k + 1) / 2
        p1 = PartitionP(n1)
        p2 = PartitionP(n2)

        if k%2==1:
            result += p1 + p2
        else:
            result += - p1 - p2
        
    PartitionPCache[n] = result
    
    return result
#*************************************************************************************








#******************************* Euler077.py *****************************************
primes = []

def Solve(target):    
    combos = 0
    testStart = 0
    while combos < target:
        testStart+=1
        combos = HelperMath.PartitionP(testStart)

    primes = HelperMath.Eratosthenes(testStart)
    maxPrime = max(primes)    

    numberToTest = testStart
        
    while True:
        combos = Euler031.countBreaks(numberToTest, primes)
        if numberToTest in primes:
            combos-=1

        if combos>=target:
            return numberToTest
        numberToTest+=1
        if numberToTest > maxPrime:
            maxPrime = HelperMath.NextPrime(maxPrime)
            primes.append(maxPrime)

#************************************************************************************