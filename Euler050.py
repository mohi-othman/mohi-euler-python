import math
import time
#from functools import reduce
t = time.clock()

cutOff = 1000000
primes = [2,3,5,7,11]
                     
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
        primes.append(n)
        
print("All primes below",cutOff,"found")
print(time.clock()-t)


maxCount = 1
maxSequence = []
count = len(primes)
while count>1:
    flag = False
    for i in range(count, len(primes)+1):
        sequence = primes[i-count:i]
        if sum(sequence)>cutOff:
            break
        if sum(sequence) in primes:
            flag = True
            maxSequence = sequence
            maxCount = count

    if flag:
        break
    else:
        count-=1
                       
print("Max sequence is:")
print(maxSequence)
print("It contains",maxCount,"elements")
print("The sum is",sum(maxSequence))
print(time.clock()-t)
    
        



