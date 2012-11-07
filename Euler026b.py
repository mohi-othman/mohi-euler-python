import time
import math

def findPrimes(minimum, maximum):
    primes = [2,3,5,7,11]
    for n in range(max(primes)+2, maximum+1,2):
        flag = True
        for p in primes:
            if n%p == 0:
                flag = False
                break

        if flag: primes.append(n)
    
    return [n for n in primes if n>=minimum]


t = time.clock()
maxSlice = 1000
maxDigit = maxSlice*(maxSlice-1)
cutOff = 1000
fractionDict = dict()
recurring = dict()
primes = findPrimes(7, cutOff)
print("Primes found: ", time.clock()-t)

for d in primes:
    result = ""
    number = 10

    while(len(result)<maxDigit):
        factor = 1

        while number<d:
            factor+=1
            number = number * 10**factor
            
        result += str(int(number/d))
        number = number%d
        if number == 0: break
    
    fractionDict[d] = result[:maxDigit]

print("Division completed: ", time.clock()-t)
      
for fraction in fractionDict:
    for slice in range(1,maxSlice+1):        
        text = fractionDict[fraction]
        if len(text)<maxDigit:
            break
        
        flag = True            
        firstSlice = text[:slice]
        text = text[slice:]
        while(len(text)>0):          
            if firstSlice!=text[:slice]:
                flag = False
                break

            text = text[slice:]

        if flag:
            recurring[slice] = (fraction, firstSlice)
            break

slices = list(recurring.keys())
slices.sort()
slices.reverse()
print(slices[0], recurring[slices[0]])
print(time.clock()-t)
