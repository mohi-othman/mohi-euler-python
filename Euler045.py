import time
import math

def getTriangle(n):
    return n*(n+1)/2

def getTriangleN(number):
    a = 1
    b = 1
    c = -2*number
    z = math.sqrt(b**2 - 4*a*c)    

    if z>b:
        x = (-b+z)/(2*a)
        return x
    else:
        return false
    
def isPentagonal(number):
    a = 3
    b = -1
    c = -2*number
    z = math.sqrt(b**2 - 4*a*c)    

    if z>b:
        x = (-b+z)/(2*a)
        return x==int(x)
    else:
        return false

def isHexagonal(number):
    a = 2
    b = -1
    c = -number
    z = math.sqrt(b**2 - 4*a*c)    

    if z>b:
        x = (-b+z)/(2*a)
        return x==int(x)
    else:
        return false
    
n = getTriangleN(40755)
n += 1
startTime = time.clock()
while True:
    tri = getTriangle(n)
    if isPentagonal(tri) and isHexagonal(tri):
        print(tri)
        print(time.clock()-startTime)
        break
    n+=1
