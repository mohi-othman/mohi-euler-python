import time

def GCD(u,v):
    if u<v:
        u,v = v,u

    while True:
        r = u%v
        if r==0:
            return v
        u,v = v,r

def solve(roof):
    minFraction = 1/3
    maxFraction = 1/2
    count = 0
    for d in range(1, roof+1):
        for n in range(int(d/3)+1, int(d/2)+1):
            if GCD(n,d)==1 and (minFraction < n/d < maxFraction):
                count+=1
                
    return count

t = time.clock()
print(solve(12000))
print(time.clock()-t)
