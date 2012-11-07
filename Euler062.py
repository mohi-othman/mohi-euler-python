import time
import math
    
def recur(numberSoFar, numbersLeft, result):
    if len(numbersLeft)==1:
        result.add(numberSoFar+numbersLeft[0])
        return
    else:        
        for n in numbersLeft:
                if len(numberSoFar)>0 or n!='0':
                    newNumber = numberSoFar+n
                    newList = list(numbersLeft)
                    newList.remove(n)
                    recur(newNumber, newList, result)
    
def getPermutations(number):
    numbers = list(str(number))
    result = set()
    recur('', numbers, result)
    return [int(x) for x in result if x!=str(number)]

def getCubeRoot(x):
        return round(x**(1/3),10)

def isInteger(x):
        return x==int(x)

def solve(start, target):
        while True:                
                cube = start**3
                start+=1        
        
                perms = getPermutations(cube)
                
                roots = [getCubeRoot(x) for x in perms]

                count = sum([isInteger(r) for r in roots])

                if count+1 >= target:
                        return cube
                
        
    
t = time.clock()
print(solve(345, 4))
print(time.clock()-t)

