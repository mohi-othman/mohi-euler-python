import time

minValue = 1000
maxValue = 9999

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


def arePermutations(a,b,c):
    aSet = set(list(str(a)))
    bSet = set(list(str(b)))
    cSet = set(list(str(c)))

    return aSet == bSet == cSet

    
def findSequences():
    for n in range(minValue, maxValue-1):
        for increment in range(1, (maxValue-n)//2):
            n2 = n + increment
            n3 = n2 + increment
            if arePermutations(n,n2,n3) and isPrime(n) and isPrime(n2) and isPrime(n3):
                print(n,n2,n3)
                print(str(n)+str(n2)+str(n3))

t = time.clock()
findSequences()
print(time.clock()-t)
