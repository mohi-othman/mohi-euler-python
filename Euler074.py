import cProfile
import time
from math import *

from functools import *

factDict = dict()
def factorial(n):
    if n in factDict:
        return factDict[n]
    if n in (0,1): result= 1
    else: result = n * factorial(n-1)
    factDict[n]=result
    return result

def digitCount(n):
    return floor(log10(n))+1

factorialDigitsDict = dict()
def factorialDigits(n):
    if n in factorialDigitsDict:
        return factorialDigitsDict[n]
    result = sum((factorial(int(d)) for d in str(n)))
    factorialDigitsDict[n]=result
    return result

chainCountDict = dict()                
def getChainCount(n):
    if n in chainCountDict:
        return chainCountDict[n]
    
    terms = {n}

    while True:
        n = factorialDigits(n)
        if n in terms:
            break
        terms.add(n)
    result = len(terms)
    for t in terms:
        chainCountDict[t] = result
    return result

def solve(target, roof):
    result = 0
    for n in range(1, roof):
        if getChainCount(n)==target:
            result+=1
    return result

t = time.clock()
print(solve(60,1000000))
print(time.clock()-t)
