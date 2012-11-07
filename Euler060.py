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

def getCombos(number, otherNumbers, size, currentList, result):
    if number > 0:
        currentList.append(number)
    
    if len(currentList) == size:
        result.append(currentList)
        return
    elif len(otherNumbers) == (size - len(currentList)):
        currentList.extend(otherNumbers)
        result.append(currentList)
        return
    else:        
        getCombos(0, otherNumbers[1:], size, list(currentList), result)        
        getCombos(otherNumbers[0], otherNumbers[1:], size, list(currentList), result)
    
    
def getAllMasks(size, maxLength, currentMask, result):
    if currentMask.count('1') == size:                        
        result.append(currentMask)
        return
    elif (size - currentMask.count('1')) == (maxLength-len(currentMask)):        
        currentMask+= '1' * (maxLength-len(currentMask))
        result.append(currentMask)
        return
    else:
        for i in range(0,2):
            newMask = currentMask + str(i)
            getAllMasks(size, maxLength, newMask, result)
            
def getAllCombinations(newNumber, otherNumbers, size):
    result = []
    masks = []
    newList = [newNumber]
    newList.extend(otherNumbers)

    maxLength = len(otherNumbers)    
    getAllMasks(size-1, maxLength, '', masks)
    for mask in ['1' + m for m in masks]:
        x = [newList[n] for n in range(0, len(mask)) if mask[n]=='1']
        result.append(x)
    return result
##    result = []
##    masks = []
##    maxLength = len(otherNumbers)
##    getAllMasks(size-1, maxLength, '', masks)
##    
##    for mask in masks:
##        combination = [newNumber]        
##                
##        for i in range(0, len(mask)):
##            if mask[i]=='1':                
##                combination.append(otherNumbers[i])
##        result.append(combination)
##    return result       
        
def getAllConcats(numbers):
    result = list()

    for x in range(0, len(numbers)):
        for y in range(0, len(numbers)):
            if x!=y:
                result.append(str(numbers[x]) + str(numbers[y]))
    return result

##def getAllConcats(numbers):
##    result = list()
##    for a in numbers:
##        others = list(numbers)
##        others.remove(a)
##        for b in others:
##            result.append(str(a)+str(b))
##            
##
##    return result
        
    
def solve(groupSize):
    primes = [2,3,5,7,11]
        
    n = max(primes)
    while True:
        n += 2
        if isPrime(n):            
            if len(primes)+1 >= groupSize:
                combos = getAllCombinations(n, primes, groupSize)                                
                primes.append(n)
                for combo in combos:                                        
                    concats = getAllConcats(combo)
                    flag = True
                    for concat in concats:                        
                        if not isPrime(int(concat)):
                            flag = False
                            break

                    if flag:
                        #return numbers
                        return combo
            else:
                primes.append(n)
            
                    
                
            
            
t = time.clock()
print(solve(3))
print(time.clock() - t)
