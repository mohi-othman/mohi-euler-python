import time

def findNextValue(n):
        result = 0
        if n%2==0:
            result = n/2
        else:
            result = 3*n+1

        return result


def Solve():
    cache = dict()
    cutOffValue = 1000000
    maxStart = 0
    maxCount = 0
    t = time.clock()

    for startValue in range(1,cutOffValue):    
        value = startValue
        count = 1

        while(value>1):
            value = findNextValue(value)
            if value in cache.keys():
                count+= cache[value]            
                break        
            count+=1
        
        cache[startValue] = count

        if count>maxCount:
            maxCount = count
            maxStart = startValue
                
    print(maxStart)
    print(maxCount)
    print(time.clock() - t)


def SolveNoCache():    
    cutOffValue = 1000000
    maxStart = 0
    maxCount = 0
    t = time.clock()

    for startValue in range(1,cutOffValue):    
        value = startValue
        count = 1

        while(value>1):
            value = findNextValue(value)           
        
            count+=1
        
        
        if count>maxCount:
            maxCount = count
            maxStart = startValue
                
    print(maxStart)
    print(maxCount)
    print(time.clock() - t)
