import time

primes = [2,3,5,7,11,13]

def getNearestPrime(number):
    for i in range(max(primes)+2, number+1):
        flag = True
        for p in primes:
            if i%p==0:
                flag = False
                break

        if flag:
            primes.append(i)

    return max(primes)
            
def isPrime(number):
    if number%2!=0 and (number in primes or getNearestPrime(number) == number):
        return True
    else:
        return False


cutOffA = 1000
cutOffB = 1000
resultDict = dict()
t=time.clock()
for a in range(-cutOffA+1,cutOffA):
    for b in range(-cutOffB+1,cutOffB):
        #print((a,b))
        n = 0
        while(True):
            y = n**2 + a*n + b
            if not isPrime(y):
                resultDict[n] = (a,b) 
                break
            n+=1
maxSeq = max(resultDict.keys())
resultSet = resultDict[maxSeq]
product = resultSet[0]*resultSet[1]
             
print(maxSeq, resultSet, product)
print(time.clock()-t)
        
    
