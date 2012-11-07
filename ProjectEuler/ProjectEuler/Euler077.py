import HelperMath
import Euler031

primes = []

def Solve(target):    
    combos = 0
    testStart = 0
    while combos < target:
        testStart+=1
        combos = HelperMath.PartitionP(testStart)

    primes = HelperMath.Eratosthenes(testStart)
    maxPrime = max(primes)    

    numberToTest = testStart
        
    while True:
        combos = Euler031.countBreaks(numberToTest, primes)
        if numberToTest in primes:
            combos-=1

        if combos>=target:
            return numberToTest
        numberToTest+=1
        if numberToTest > maxPrime:
            maxPrime = HelperMath.NextPrime(maxPrime)
            primes.append(maxPrime)


    

    
    

    
    