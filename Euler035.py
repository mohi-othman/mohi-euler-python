import math
import time
from functools import reduce
t = time.clock()
cutOff = 1000000
primes = set([2,3,5,7,11])
result = set()

def getRotations(number):
    textNumber = str(number)
    length = len(textNumber)
    result = []

    for i in range(0, length):
        result.append(int(textNumber[-length+i:] + textNumber[:i]))

    return result
                      
# find all primes
for n in range(max(primes)+2,cutOff,2):
    flag = True
        
    if n%3 == 0:
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
        
    if flag:
        primes.add(n)

print(len(primes)," primes found")
print(time.clock()-t)
for p in list(primes):
    txt = list(str(p))
    if '0' in txt or '4' in txt or '6' in txt or '8' in txt or ('2' in txt and p!=2):
        primes.discard(p)

print(len(primes)," primes left")
print(time.clock()-t)

for p in primes:    
    rotations = []
    rotations = getRotations(p)      
    
    flag = True
    for r in rotations:        
        if r not in primes:
            flag = False
            break        
    
    if flag:
        result = result.union(rotations)
#    else:
#        primes = primes.difference(rotations)
a = list(result)
a.sort
print(a)
print(len(result))        
print(time.clock()-t)    
