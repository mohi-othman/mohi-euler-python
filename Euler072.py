import time
import math
from functools import *

#Euclid's algorithm
def GCD(u,v):
    if u<v:
        u,v = v,u

    while True:
        r = u%v
        if r==0:
            return v
        u,v = v,r

def findFactors(n):
    result = set()
    if n%2==0:
        result.add(2)
        while n%2==0:
            n/=2
    d=3
    while n>1:
        if n%d==0:
            result.add(d)
            while n%d==0:
                n/=d
        d+=2
    return result

def solve(roof):
    count = 0
    for d in range(2,roof+1):
        count+=1 # 1/d is always reduced
        nCandidates = []
        
        if d%2==0:
            nCandidates = range(3,d,2)
        else:
            nCandidates = range(2,d)
            
        for n in nCandidates:            
            if GCD(n,d)==1:
                count+=1
    return count

t = time.clock()
print(solve(10000))
print(time.clock() - t)
