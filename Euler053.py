import time
from functools import reduce

lowerBound = 1
upperBound = 100
cutOff = 1000000

def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda a,b:a*b, range(1,n+1))

t = time.clock()
count = 0
for n in range(lowerBound,upperBound+1):
    for r in range(1, n+1):
        c = factorial(n) / (factorial(r) * factorial(n-r))
        if c > cutOff:
            count+=1

print(count)
print(time.clock() - t)
