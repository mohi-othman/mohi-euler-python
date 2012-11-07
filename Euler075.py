import time
from math import *

def findAllPrimitivePythagoranTriples(maxLength):
    triangles = []
    for n in range(1, int(sqrt(maxLength)/2)+1):
        for m in range(1, n):
            a = n**2 - m**2
            b = 2*m*n
            c = n**2 + m**2
            if a+b+c<=maxLength:
                triangles.append((a,b,c))
        
    return triangles

def findPythagoranTriple(length):
    result = []
    if length%2==0:  
        limit = int(sqrt(length/2))
        for n in range(1, limit):
            for m in range(1, n):
                if n*(n+m) == length/2:
                    result.append((n**2-m**2, 2*m*n, n**2+m**2))
    return result
    

def findPythagoranTriple2(length):
    results = []
    for b in range(1,length//2):
        a = (length**2/2 - b*length)/(length-b)
        if a<b:
            break
        if a==int(a):
            results.append((int(a),int(b),int(length-(a+b))))            
        
    return results

def hasSinglePythagoranTriple2(length):
    count = 0
    for b in range(1,length//2):
        a = (length**2/2 - b*length)/(length-b)
        if a<b:
            break
        if a==int(a):            
            if count == 1:
                return False
            count+=1
        
    return (count==1)

def solve(roof):
    primitives = findAllPrimitivePythagoranTriples(roof)
    triDict = dict()
    for t in primitives:
        length = sum(t)
        if length in triDict:
            triDict[length].append(t)
        else:
            triDict[length]=[t]

    singles = [triDict[x][0] for x in triDict if len(triDict[x])==1]
    sums = list(map(lambda x: sum(x), singles))
    i = 0
    while True:
        if i>=len(sums):
            break
        n = sums[i]
        for x in [x for x in sums if x>n]:
            if x%n == 0:
                sums.remove(x)
        i+=1
        print(i, len(sums))
    
    return len(sums)

roof = 1500000
t = time.clock()
print(solve(roof))
print(time.clock() - t)
