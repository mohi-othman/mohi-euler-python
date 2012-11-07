import math

def factorize(number):
    n = number
    factors = []
    i = 2
    while (i <= n):
        while(n % i == 0):
            factors.append(i)
            n = n/i
        i+=1

    return factors

def solve(minDivisor, maxDivisor):
    factorsDict = dict()
    for i in range(minDivisor, maxDivisor+1):
        factors = factorize(i)
        distinctFactors = set()

        for f in factors:
            distinctFactors.add(f)

        for d in distinctFactors:
            if (d in factorsDict):
                factorsDict[d] = max(factorsDict[d], factors.count(d))
            else:
                factorsDict[d] = factors.count(d)

    result = 1
    for k in factorsDict.keys():
        result = result * k ** factorsDict[k]

    return result
                
def solve3(minDivisor, maxDivisor):
    cutOff = 1
    divisors = []
    for i in range(minDivisor, maxDivisor+1):
        cutOff *= i      

    multiplesDict = dict()
    
    for i in range(minDivisor, maxDivisor+1):
        print("multipliers for", i)
        factor = 1
        multiples = set()

        while(factor*i<=cutOff):
            multiples.add(factor*i)
            factor+=1

        multiplesDict[i] = multiples

        print('done')
        
    resultSet = multiplesDict[minDivisor]
    for i in range(minDivisor+1, maxDivisor+1):
        resultSet = resultSet & multiplesDict[i]
    
    return min(resultSet) 
    
def solve2(minDivisor, maxDivisor):
    num = maxDivisor
    cutOff = 1
    for i in range(minDivisor, maxDivisor+1):
        cutOff *= i

    print (cutOff)
    while(num<cutOff):
        flag = True
        for d in range(minDivisor, maxDivisor+1):
            flag = flag and (num%d==0)

        if flag: return(num)

        num+=1


print(solve(2,20))
