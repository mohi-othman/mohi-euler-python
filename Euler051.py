#http://pastebin.com/YMYPrBGY

import time
import math

digits = [0,1,2,3,4,5,6,7,8,9]
digitsWithMask = list(map(lambda x: str(x), digits))
digitsWithMask.append('*')
primes = [2,3]
targetCount = 8

def isPrime(n):
    if n in primes:
        return True
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = math.floor(math.sqrt(n))
    f = 5
    while f<=r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f+=6

    return True
    

def addDigit(size, digitsSoFar, results):
    pool = []
    if len(digitsSoFar) == 0:
        pool = [x for x in digitsWithMask if x!='0']
    else:
        pool = digitsWithMask

    size -=1
    if size == 0 and '*' not in digitsSoFar:
        results.append(digitsSoFar + '*')
    else:
        for digit in pool:       
            newDigit = digitsSoFar + digit    
        
            if size == 0:
                results.append(newDigit)                
            else:
                addDigit(size, newDigit, results)
    
def getPermutations(size):
    results = []
    addDigit(size, '', results)  

    return results 

t = time.clock()
primeSubs = []
flag = False
n=2

while not flag:    
    masks = getPermutations(n)
    
    print(n, 'digits')
    print(len(masks), 'Permutations Found')
    print(time.clock() - t)   
    
    for mask in masks:
        if mask[-1:] != '*' and int(mask[-1:])%2 == 0:
            continue
        subs = list(map(lambda x: int(mask.replace('*',str(x))), digits))
        primeSubs = [x for x in subs if len(str(x))==len(mask) and isPrime(x)]
        
        if len(primeSubs) >= targetCount:
            flag = True
            break
    print('No Primes Found')
    print(time.clock() - t)
    
    n+=1

primeSubs.sort()    
print('Solved:')              
print(primeSubs)
        
print(time.clock() - t)
