import time
import math

def P(number):
    return (number*(3*number - 1))/2

def isP(number):
    a = 3
    b = -1
    c = -2*number
    z = math.sqrt(b**2 - 4*a*c)
    
    x = (-b+z)/(2*a)
    y = (-b-z)/(2*a)

    return (x>0 and x==int(x)) or (y>0 and y==int(y))

def solve():    
    pentagonals = []
    n = 1
    while True:
        newP = P(n)
        for oldP in pentagonals:
            #if isP(newP+oldP) and (newP-oldP) in pentagonals:
            if isP(newP+oldP) and isP(newP-oldP): 
                print(newP,oldP)
                print(newP-oldP)
                return
            
        pentagonals.append(newP)
        n+=1
          
def solve2():
    pentagonals = []
    n = 1
    while True:
        newP = P(n)
        #result = list(filter(lambda oldP: isP(newP+oldP) and (newP-oldP) in pentagonals, pentagonals))
        result = [(newP, oldP) for oldP in pentagonals if isP(newP+oldP) and (newP-oldP) in pentagonals]
        #result = [(newP, oldP) for oldP in pentagonals if isP(newP+oldP) and isP(newP-oldP)]
        if len(result)>0:
            print(result)
            return
        else:
            pentagonals.append(newP)
            n+=1
    
t = time.clock()    
solve2()
print(time.clock()-t)
