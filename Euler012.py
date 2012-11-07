import math
import time

def triangleNumberGenerator():
    n = 1
    result = 0
    while True: 
        result += n        
        yield result
        n+=1

def getNumberOfFactors(N):    
    result = 0
    sqrN = math.sqrt(N)
    
    if N==1:
        result = 1
    else:
        result = 2
        if sqrN == int(sqrN):
            result += 1

    f = 2
    while f<sqrN:
        if N%f==0:
            result += 2
        f+=1

    return result
        
def solve(target):
    triangles = triangleNumberGenerator()

    while True:
        tri = next(triangles)
        count = getNumberOfFactors(tri)
        if count > target:
            return tri

t = time.clock()
print(solve(500))
print(time.clock() - t)
