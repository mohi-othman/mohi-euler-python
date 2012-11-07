#Problem 85
#
#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#    
#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

#http://www.gottfriedville.net/mathprob/comb-subrect.html

def recCount(n,m):
    return  m*(m+1)*n*(n+1)/4

def solve(target):
    #find max dimension
    m=1    
    while True:    
        m2 = m    
        m2+=1        
        if recCount(1,m2)>=target:
            delta1 = target - recCount(1,m)
            delta2 = recCount(1,m2) - target
            if delta1 > delta2:                
                m = m2
            break
        else:            
            m = m2
    max = m
    recDict = dict()
    for n in range(1,max):
        for m in range(1,max):
            recDict[(n,m)] = abs(target-recCount(n,m))
    x = sorted(recDict, key=recDict.get)
    n = x[0][0]
    m = x[0][1]

    return(n,m,recCount(n,m),n*m)

