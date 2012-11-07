#Problem 91
#18 March 2005

#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ?OPQ.


#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0  x1, y1, x2, y2  2.


#Given that 0  x1, y1, x2, y2  50, how many right triangles can be formed?

import math
import itertools
from fractions import Fraction

O = (0,0)

def getDistanceSquared(x,y):
    return math.fabs( (x[0]-y[0])**2 - (x[1]-y[1])**2 )

def isRightAngleTriangle(P,Q):
    OP = getDistanceSquared(O,P)
    OQ = getDistanceSquared(O,Q)
    PQ = getDistanceSquared(P,Q)
    
    hyp = max(OP,OQ,PQ)
    
    if PQ==hyp:
        return OP + OQ == PQ
    elif OQ==hyp:
        return PQ + OP == OQ
    elif OP==hyp:
        return PQ + OQ == OP
    

def solve(roof):
    result = roof * roof * 3
    setP = set([(x,y) for x in range(1,roof+1) for y in range(1,roof+1)])
    for p in setP:   
        slope = Fraction(-p[0],p[1])
        #go up    
        x = p[0]
        y = p[1]    
        while True:
            x=x-slope.denominator
            y=y-slope.numerator
            if 0<=x<=roof and 0<=y<=roof:
                result+=1
            else:
                break
        #go down
        x = p[0]
        y = p[1]    
        while True:
            x=x+slope.denominator
            y=y+slope.numerator
            if 0<=x<=roof and 0<=y<=roof:
                result+=1
            else:
                break

    
    return result



# Messy Brute Force - doesn't work
def solve2(roof):
    result = set()    
    setP = set([(x,y) for x in range(0,roof+1) for y in range(0,roof+1) if (x,y)!=(0,0)])
    setQ = set([(x,y) for x in range(0,roof+1) for y in range(0,roof+1) if (x,y)!=(0,0)])
    cartProduct = set(itertools.product(setP, setQ))
    possiblePoints = set()
    for pair in cartProduct:
        if (pair[1],pair[0]) not in possiblePoints and pair[0]!=pair[1]:
            possiblePoints.add(pair)

    for (P,Q) in possiblePoints:
        if isRightAngleTriangle(P,Q):
            result.add((P,Q))

    
    #[print(a) for a in result]
    return len(result)