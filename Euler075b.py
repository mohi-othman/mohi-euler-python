from math import *
import time

def GCD(u,v, z=1):
    if z!=1:
        return GCD(GCD(u,v), z)
    if u<v:
        u,v = v,u

    while True:
        r = u%v
        if r==0:
            return v
        u,v = v,r

def getPrimitiveTriples(maxLength):
    limit = int(sqrt(maxLength/2))
    result = []
    for n in range(1, limit+1):
        for m in range (1, n):
            a = n**2 - m**2
            b = 2 * m * n
            c = n**2 + m**2
            L = a+b+c
            if L<=maxLength and GCD(a,b,c)==1:
                tri = [a,b,c,L]
                tri.sort()
                result.append(tri)
    return result

def getMultiples(maxLength, primitives):
    result = set()
    for tri in primitives:
        k = 1
        while True:
            L = tri[3]*k
            if L>maxLength:
                break
            a = tri[0]*k
            b = tri[1]*k
            c = tri[2]*k
            result.add((a,b,c,L))
            k+=1
    return result

def getSingles(triples):
    singlesDict = dict()
    for tri in triples:
        L = tri[3]
        if L in singlesDict:
            singlesDict[L]+=1
        else:
            singlesDict[L]=1
    return [x for x in singlesDict if singlesDict[x]==1]

maxLength = 1500000
t = time.clock()    
primitives = getPrimitiveTriples(maxLength)
print("getPrimitiveTriples",time.clock() - t)
multiples = getMultiples(maxLength,primitives)
print("getMultiples", time.clock() - t)
singles = getSingles(multiples)
print("singles", time.clock() - t)
print(len(singles))
print(time.clock() - t)
