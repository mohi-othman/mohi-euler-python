def findPrimes(minimum, maximum):
    primes = [2,3,5,7,11]
    for n in range(max(primes)+2, maximum+1,2):
        flag = True
        for p in primes:
            if n%p == 0:
                flag = False
                break

        if flag: primes.append(n)
    
    return [n for n in primes if n>=minimum]

cutOff = 1000
numbers = set(findPrimes(6,cutOff))

#Exclude finites
maxAlpha = 0
alpha = 1
while(True):
    n = 2**alpha
    if n>=cutOff:
        break
    else:
        maxAlpha = n
        numbers.discard(n)
        alpha+=1

for alpha in range(0,maxAlpha+1):
    beta = 1
    while(True):
        n = 2**alpha * 5**beta
        if n>=cutOff:
            break
        else:
            numbers.discard(n)
            beta+=1
maxSize = 0
maxNum = 0
for n in numbers:
    right = 1%n
    
    print("n=",n)

    k=1
    while(True):
        if(10**k)%n == right:
            print("size=", k)
            if maxSize < k:
                maxSize = k
                maxNum = n
            break
        else:
            k+=1

print("-->",maxNum," size=",maxSize)
