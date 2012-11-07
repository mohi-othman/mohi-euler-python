#Method to solve Pell's Equation found at:
#http://www.physicsforums.com/showthread.php?t=37854

from math import *
import time

def add(integer,fraction):
    if fraction == (0,0): return (integer,1)
    newFraction=(integer * fraction[1], fraction[1])
    return (newFraction[0]+fraction[0],fraction[1])

def flip(fraction):
    return (fraction[1],fraction[0])

def getNextIteration(number, numerator, denominator):
    root = floor(sqrt(number))
    integer = int(numerator*(root-denominator) // (number - denominator**2))
    newD = int((number-denominator**2)/numerator)
    newN = int(-denominator - (integer * newD))

    return(integer, newN, newD)

def getSeries(number):
    numerator = 1
    denominator = -floor(sqrt(number))
    integer = 0

    series = [int(sqrt(number))]

    while True:
        integer, numerator, denominator = getNextIteration(number, numerator, denominator)
                
        numerator, denominator = denominator, numerator    
        if integer-floor(sqrt(number)) == series[0]:        
            return series
        
        series.append(integer)

def collapse(series):
    past = (0,0)
    series.reverse()
    for member in series:
        past=flip(past)
        past=add(member,past)

    return past

def findPellSolution(number):
    series = getSeries(number)    
    if (len(series)-1)%2==0:
        series.append(series[0]*2)
        for i in range(1, len(series)-1):
           series.append(series[i])
        
    return collapse(series)
    





def solve(cutOff):
    #Get none squares
    numbers=[]
    for i in range(2,cutOff+1):
        q=sqrt(i)
        if int(q)!=q:
            numbers.append(i)

    #Get all minimal solutions for Pell's Equation
    solutions = []
    for D in numbers:
        solutions.append(findPellSolution(D))

    x = [a[0] for a in solutions]

    return (numbers[x.index(max(x))],max(x))

t = time.clock()
print(solve(1000))
print(time.clock()-t)
