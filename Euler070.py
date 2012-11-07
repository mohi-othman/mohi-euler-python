import time
from math import *
from itertools import *

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
    numbers = []
    primes = findPrimes(10000)

    #only get numbers that have two prime factors
    for p in primes:
        for n in [x for x in primes if x<=p]:
            numbers.append(p*n)
        

    #remove primes
    #numbers = [x for x in numbers if x not in primes]
    result = []    
    for n in numbers:
        phi = int(phiEuler(n, primes))
        if sorted(str(phi)) == sorted (str(n)):
            result.append((n/phi, n))

    result.sort()
    return result

t = time.clock()
result = solve(10**7)
print(result[0])
print(time.clock()-t)
