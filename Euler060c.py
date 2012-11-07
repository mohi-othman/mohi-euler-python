import time
import math

primes = []

def findPrimes(limit):
    result = []
    crossLimit = math.floor(math.sqrt(limit))
    sieve = dict()
    for n in range(2,limit+1):
        sieve[n] = False

    for n in range(4, limit+1,2):
        sieve[n] = True

    for n in range(3, limit+1,2):
        if not sieve[n]:
            for m in range(n*n, limit+1, 2*n):
                sieve[m] = True

    return [x for x in sieve.keys() if not sieve[x]]

def isPrime(n):        
    return n in primes

def isConcatPrime(a,b):
    x = str(a)
    y = str(b)
    return isPrime(int(y+x)) and isPrime(int(x+y))

def getCombos(newNumber,otherNumbers,size, repository):
    result = repository[size]   
        
    if size == 2:                    
        for n in otherNumbers:            
            if isConcatPrime(newNumber, n):
                result.append([n, newNumber])                   
    else:
        if len(otherNumbers)>0:
            getCombos(otherNumbers[-1],otherNumbers[:-1],size-1,repository)
                        
                
        for concat in repository[size-1]:
            flag = True
            for n in concat:
               if not isConcatPrime(newNumber, n):
                   flag = False
                   break
            if flag:
                newResult = list(concat)
                newResult.append(newNumber)
                result.append(newResult)

def solve(size):   

    numbers = [3]
    newP = 5
    repository = dict()
    for r in range(2,size+1):
        repository[r]=[]
    
    while True:
    
        if isPrime(newP):
            getCombos(newP, numbers, size,repository)
            if len(repository[size])>0:
                return repository[size]
                break
            numbers.append(newP)

        newP+=2    

t = time.clock()
primes = findPrimes(9999999)
print(time.clock()-t)
print(solve(4))
print(time.clock()-t)
                
