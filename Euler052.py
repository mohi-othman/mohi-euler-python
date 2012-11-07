import time
from functools import reduce

number = 10
multipliers = [2,3,4,5,6]
t = time.clock()

while True:
    results = list(map(lambda x: number * x, multipliers))
    
    if reduce(lambda a,b: a and b, [len(str(x))==len(str(number)) for x in results]):
        digitSets = [list(str(x)) for x in results]
        for d in digitSets: d.sort()
        
        originalSet = list(str(number))
        
        originalSet.sort()
        
        matches = [x for x in digitSets if x == originalSet]
        if len(matches) == len(multipliers):
            print(number, results)
            print(time.clock() - t)
            break
    number += 1
    
    
