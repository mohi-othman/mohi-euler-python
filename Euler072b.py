import time
from math import *
from itertools import *
from functools import *

def findPrimes(roof):
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

def countMultiples(numbers, maxValue):
##    numbers.append(1)
##    maxCount = int(log(maxValue,2))
##    combos = combinations_with_replacement(numbers,maxCount)
##    result = len([x for x in combos if reduce(lambda a,b:a*b, x)<maxValue])
##    return result
    result = set()
    for n in numbers:
        i = 1
        while i*n < maxValue:
            result.add(i*n)
            i+=1
    return len(result)

def solve(number):    
    primes = findPrimes(number)
    count = 0
    for d in range(2, number+1):
        factors = findPrimeFactors(d, primes)
        #nonFactors = [x for x in primes if x<d and x not in factors]
        count+= (d-1)-countMultiples(factors, d)
        #count+= countMultiples(nonFactors, d)
        
    return count

t=time.clock()
print(solve(10000))
print(time.clock()-t)
    
    
