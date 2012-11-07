import math
import time

###############################
def factorize4(number):
    factors = set()
    
    a = math.ceil(math.sqrt(number))
    delta = 0
    b = 0
    while(a+b<number):      
        delta = a**2 - number
        b = math.sqrt(delta)
        if math.floor(b)==b:
            factors.add(a+b)
            factors.add(a-b)
        #print("a=" , a)
        #print("delta=" , delta)
        #print("b=" , b)
        a+=1
    print(factors)
    return 0

def factorize(number):
    n = number
    factors = []
    i = 2
    while (n>1):
        if n % i == 0:
            factors.append(i)            
            while(n % i == 0):            
                n/= i

        i+=1

    print (max(factors))

    return 0
###############################
def factorize3(number):
    factors = []
    maxDivisor = math.floor(math.sqrt(number))
    
    for divisor in range(2,maxDivisor):
        if(number!=divisor and number%divisor==0):
            number = number/divisor
            factors.append(divisor)

    
    factors.reverse()
    print(factors)
    return 0
    for factor in factors:
        if isPrime(factor):
            return factor
    
###############################
def factorize2(number):
    factors = []
    divisor = number
    
    while(divisor>=2):
        if(number%divisor==0 and isPrime(divisor)):
            return divisor
        
        divisor-=1
        


###############################
def isPrime(number):
    maxDivisor = math.floor(math.sqrt(number))
    
    for i in range(2,maxDivisor+1):
        if(number%i)==0: return False

    return True

###############################
n = 26 
divisors = [2,3,5,7,11]
stopWatch = time.clock()
result = factorize(n)

print(result)
print (time.clock()- stopWatch)



factors = []
i = 2
while (n>1):
    if n % i == 0:
        factors.append(i)            
        while(n % i == 0):            
            n/= i

    i+=1

print (max(factors))
