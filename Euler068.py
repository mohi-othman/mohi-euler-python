import time
from itertools import *

def solve(numberOfCoreNodes):
    numbers = list(range(1, numberOfCoreNodes*2+1))
    coreNodes = []
    magicGons =[]

    #get permutations and only add those with no cyclic repeats
    for p in list(permutations(numbers, numberOfCoreNodes)):
        success = True
        for i in range(1, len(p)):
            if p[i:]+p[:i] in coreNodes:
                success = False
                break
        if success:
            coreNodes.append(p)                   
    
    
    for coreNode in coreNodes:        
        innerArms = []
        innerSums = []
        for n in range(0, len(coreNode)):
            arm = (coreNode[n], coreNode[(n+1)%len(coreNode)])
            innerArms.append(arm)
            innerSums.append(sum(arm))
        innerSums.sort()
        innerSums.reverse()

        outerNumbers = [x for x in numbers if x not in coreNode]
        outerNumbers.sort()
        
        sums = set([innerSums[n]+outerNumbers[n] for n in range(0, len(coreNode))])
        if len(sums)==1:
            magicSum = sums.pop()

            #find arm index with smallest outer number
            arm = [x for x in innerArms if x[0]+x[1]+outerNumbers[0]==magicSum][0]
            index = innerArms.index(arm)
            
            result = ''
            for n in range(0, len(innerArms)):
                innerArm = innerArms[(index+n)%len(innerArms)]
                result+= str(magicSum-sum(innerArm)) + str(innerArm[0]) + str(innerArm[1])
            magicGons.append(result)

    magicGons.sort()
    
    return magicGons[len(magicGons)-1]

t = time.clock()
print(solve(5))
print(time.clock()-t)
    
