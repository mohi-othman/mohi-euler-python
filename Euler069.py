import time
from math import *

def findPrimes(roof):
    t= time.clock()
    numbers = range(2,roof+1)
    crossedOut = dict()
    
    for n in numbers:
        crossedOut[n] = False
    
    while True:
        p = numbers[0]
        
        for m in range(2,int(roof/p)+1):
            crossedOut[m*p] = True

        removedList = numbers[1:]  
        newNumbers = [x for x in removedList if not crossedOut[x]]
        if len(newNumbers)==len(removedList):
            break
        numbers = newNumbers

    print('primes found')
    print(time.clock()-t)
    return [x for x in crossedOut if not crossedOut[x]]

def findPrimeFactors(number, primes):    
    factors = []    
    for p in primes:
        maxFactor = int(sqrt(number))
        
        if p>maxFactor:
            factors.append(number)
            break
        
        if number%p==0:
            factors.append(p)
            while number%p==0:
                number/=p
            if number==1:
                break
    
    return factors

def phiEuler(number, primes):#get all prime factors
    if number == 1:
        return 1
    
    factors = findPrimeFactors(number, primes)

    #calculate
    #http://en.wikipedia.org/wiki/Euler%27s_totient_function
    result = number
    for f in factors:
        result*=(f-1)/f

    return result
    
    
def solve(roof):
    numbers = list(range(1,roof+1))
    primes = findPrimes(roof)            
    maxResult = 0
    maxN = 0
    for n in numbers:
        result = n / phiEuler(n, primes)
        if result>maxResult:
            maxResult = result
            maxN = n
    return(maxN, maxResult)

t = time.clock()
print(solve(10**6))
print(time.clock()-t)
