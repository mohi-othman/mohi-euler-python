#http://mathworld.wolfram.com/PartitionFunctionP.html
# Partitioning function
import time

def addNumber(numberToAdd, sumSoFar, targetTotal, result):
    sumSoFar += numberToAdd
    if sumSoFar == targetTotal:
        result[0]+=1
    else:
        for n in range (1, min(numberToAdd, targetTotal-sumSoFar)+1):            
           addNumber(n, sumSoFar, targetTotal, result)


def findCombos(targetTotal):
    result = [0]
    for n in range(1, targetTotal):
        addNumber(n, 0, targetTotal, result)


    return result

cache = dict()
def P(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n in cache:
        return cache[n]
    
    result=0    
    for k in range(1, int(n)+1):
        n1 = n - k * (3 * k - 1) / 2
        n2 = n - k * (3 * k + 1) / 2
        p1 = P(n1)
        p2 = P(n2)

        if k%2==1:
            result += p1 + p2
        else:
            result += - p1 - p2
        
    cache[n] = result
    
    return result

t = time.clock()
target = 10
#combos = findCombos(target)
combos = P(target)-1
print(combos)
print(time.clock()-t)
