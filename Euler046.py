import math
import time

primes = [2,3]

def isPrime(n):
    if n in primes:
        return True
       
    for number in range(max(primes)+2, n+1,2):
        flag = True
        for p in primes:
            if number%p == 0:
                flag = False
                break
        if flag:
            primes.append(number)

    return (n in primes)

def isGoldbach(n):
    for p in [x for x in primes if x<n]:
        x = (n-p)/2
        s = math.sqrt(x)
        if s==int(s):
            return True               

    return False

def solve():
    n = 3
    while True:
        if not isPrime(n) and not isGoldbach(n):
            print(n)
            return
        n+=2

start = time.clock()
solve()
print(time.clock()-start)
            
        
