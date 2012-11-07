import time
import math
import sys

sys.setrecursionlimit(1500)
cutOff = 1000


class fraction:
    def __init__(self, numerator, denominator):
        self.denominator = denominator
        self.numerator = numerator

    def numerator(self):
        return self.numerator

    def denominator(self):
        return self.denominator
    
    def toDecimal(self):
        return self.numerator/self.denominator

    def isNumeratorLonger(self):
        return int(math.log10(self.numerator)+1) > int(math.log10(self.denominator)+1)

    def flip(self):
        return fraction(self.denominator, self.numerator)

def simplifyFraction(x):
    while x.numerator%2==0 and x.denominator%2==0:            
            x.numerator/=2
            x.denominator/=2
            
    d = 3    
    while d<=min(x.numerator, x.denominator):
        while x.numerator%d==0 and x.denominator%d==0:            
            x.numerator/=d
            x.denominator/=d            
            
        d+=2

    return x
        
        
def addFraction(x,y): 
    return (fraction(x.numerator*y.denominator + y.numerator*x.denominator, x.denominator * y.denominator))

def multiplyFraction(x, y):
    return (fraction(x.numerator * y.numerator, x.denominator * y.denominator))
  
def divideFraction(x,y):
    return (multiplyFraction(x, y.flip()))

def intToFraction(number, denominator):
    return fraction(number*denominator, denominator)

def getIterations(iterationsLeft):    
    if iterationsLeft == 1:
        return fraction(2,1)
    else:
        return addFraction(fraction(2,1), divideFraction(fraction(1,1), getIterations(iterationsLeft-1)))

def solve():
    count = 0
    for i in range(1,cutOff+1):
        #print(i)
        root = addFraction(fraction(1,1),divideFraction(fraction(1,1),getIterations(i)))
        #print(root.toDecimal())
        if root.isNumeratorLonger():
            count+=1
        
    return count

   

t = time.clock()
print(solve())
print(time.clock() - t)

