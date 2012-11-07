#Problem 86
#07 January 2005
#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.
#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route is not always integer.
#By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest distance is integer when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.
#Find the least value of M such that the number of solutions first exceeds one million.

import math

def calcHyp(a,b):
    return math.sqrt(a**2+b**2)

def solve(target):    
    M = 0
    count = 0        
    while count<target:
        M+=1
        #print(M,count)
        for x in range(1,M+1):
            for y in range(x,M+1):                
                #if isSquare(M**2+(x+y)**2):
                if (M*(x+y))%12==0:
                    d = calcHyp(x+y,M)
                    if int(d)==d:
                        count+=1

    return M




