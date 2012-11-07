#Problem 95
#13 May 2005

#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

#12496  14288  15472  14536  14264 ( 12496  ...)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.

import HelperMath
import math
import time

primes = []

def getChain(n,roof):
    global primes
    current = n    
    chain = [n]
    while True:        
        properDivisors = HelperMath.factorizeWithPrimes(current,primes)
        properDivisors.remove(current)
        s = sum(properDivisors)
        if s==n:
            break        
        elif s in chain or s>roof:
            return []
        else:
            chain.append(s)
            current = s
    return chain
    

def solve(roof):
    global primes
    primes = HelperMath.Eratosthenes(int(math.sqrt(roof))+1)    
    maxCount = 0
    maxChain = None
    memo = dict()
    for n in range(2, roof+1):
        print(n)
        if n in memo:
            pass
        else:
            chain = getChain(n,roof)            
            for x in chain:
                memo[x] = chain 
            if len(chain)>maxCount:
                maxCount = len(chain)
                maxChain = chain
    print("length=",maxCount,"smallest member=",min(maxChain),maxChain)

    