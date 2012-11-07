import time
import math

def isPrime(n):    
    if n==1:
        return False
    if n<4:        
        return True        
    if n%2==0:
        return False
    if n<9:        
        return True       
        
    if n%3==0:
        return False

    r = math.sqrt(n)
    f = 5
    while f<=r:
        if n%f==0:
            return False
        if n%(f+2)==0:
            return False
        f+=6

    return True

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
print(solve(5))
print(time.clock()-t)
                
