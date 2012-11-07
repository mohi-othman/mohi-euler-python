import time
t = time.clock()
n=1
count=0
while len(str(9**n))<=n:    
    x = 1
    p = x**n
    while(len(str(p))<=n):
        if len(str(p))==n:
            print(n, p)
            count+=1
        x+=1
        p = x**n
    n+=1
print(count)
print(time.clock()-t)
