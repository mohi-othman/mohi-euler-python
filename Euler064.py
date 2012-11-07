from math import *
import time

def getNextIteration(number, numerator, denominator):
    root = floor(sqrt(number))
    integer = int(numerator*(root-denominator) // (number - denominator**2))
    newD = int((number-denominator**2)/numerator)
    newN = int(-denominator - (integer * newD))

    return(integer, newN, newD)


def findRootPeriod(number):
    numerator = 1
    denominator = -floor(sqrt(number))
    integer = 0

    series = []
    while True:
        integer, numerator, denominator = getNextIteration(number, numerator, denominator)
        
        series.append((integer, numerator, denominator))
        #print(integer, numerator, denominator)
    
        numerator, denominator = denominator, numerator    
        if len(series)>0 and len(series)%2==0:        
            left = series[:len(series)//2]
            right = series[-len(series)//2:]
            if left == right:
                print(series)
                return(len(series)//2)
                
    
def solve(roof):
    count = 0
    for n in range(1, roof+1):
        if sqrt(n)!=int(sqrt(n)):
            p = findRootPeriod(n)
            if p%2!=0: count+=1

    return count
t = time.clock()
print(solve(10000))
print(time.clock() - t)
