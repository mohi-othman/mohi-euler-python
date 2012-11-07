import time
from math import *

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    if n == 3:
        return True    
    if n < 9:
        return True
    if n%3 == 0:
        return False

    r = int(sqrt(n))
    f = 5
    while f<=r:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False
        f+=6

    return True

def solveJump1(roof):
    n = 0
    count = 0
    while count<roof:
        n+=1
        if isPrime(n):
            count+=1
    return n

def solveJump2(roof):
    n = 1
    count = 1
    while count<roof:
        n+=2
        if isPrime(n):
            count+=1
    return n

roof = 1000001

t = time.clock()
print(solveJump1(roof))
print(time.clock() - t)

t = time.clock()
print(solveJump2(roof))
print(time.clock() - t)
