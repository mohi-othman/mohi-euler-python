from math import *
import fractions 

def factorizeWithPrimes(number,primes):
    factors = set()
    factors.add(1)
    
    limit = int(sqrt(number))+1
    for d in primes:
        if d>limit:
            break        
        if number%d==0:
            for f in range(1, int(sqrt(number//d+1))+1):
                div = d*f          
                if number%div==0:      
                    factors.add(div)
                    factors.add(number//div)
                
                
    factors.add(number)        
    return factors


def Eratosthenes(roof):
    candidates = [x for x in range(2, roof)]
    strikeOut = {x: False for x in candidates}
   
    while True:
        p = min(candidates)
        if p**2 > roof:
            break
        m = 2
        x = p*m
        while x<roof:
            strikeOut[x] = True
            m+=1
            x= p*m
       
        candidates = [x for x in candidates[1:] if not strikeOut[x]]
       
    return [x for x in strikeOut.keys() if not strikeOut[x]]

def isPrime(number):
    if number < 2:
        return False
    elif number < 4:
        return True
    elif number%2==0:
        return False
    elif number<9:
        return True
    elif number%3==0:
        return False
    
    r = int(sqrt(number))
    f = 5
    while f<=r:
        if number%f == 0:
            return False
        if number%(f+2) == 0:
            return False
        f+=6

    return True

def NextPrime(number):
    if number%2==0:
        number-=1
    while True:
        number+=2
        if isPrime(number):
            return number

PartitionPCache = dict()
def PartitionP(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if n in PartitionPCache:
        return PartitionPCache[n]
    
    result=0    
    for k in range(1, int(n)+1):
        n1 = n - k * (3 * k - 1) / 2
        n2 = n - k * (3 * k + 1) / 2
        p1 = PartitionP(n1)
        p2 = PartitionP(n2)

        if k%2==1:
            result += p1 + p2
        else:
            result += - p1 - p2
        
    PartitionPCache[n] = result
    
    return result

def GetPentagonal(i):
    return int(i*(3*i-1)/2)

pents = []
def GeneratePents():
    global pents
    p = [0,1]
    while len(p)<500:
        if p[len(p)-1]>0:
            p.append(-p[len(p)-1])
        else:
            p.append(-p[len(p)-1]+1)

    pents = list(map(GetPentagonal, p))

def PartitionPentagonal(n):
    global pents
    if len(pents)==0:
        GeneratePents()
    
    r = 0
    f = -1
    i = 0
    while True:        
        k = pents[i+1]
        if k > n:
            break
        if i%2==0: f = -f
        r += f* PartitionPentagonal(n - k)
        i += 1
    return r

def findAllPrimitivePythagoranTriples(maxLength):    
    for n in range(1, int(sqrt(maxLength)/2)+1):
        for m in range(1, n):
            if fractions.gcd(m,n)==1  and (m+n)%2 == 1:
                a = n**2 - m**2
                b = 2*m*n
                c = n**2 + m**2
                if a+b+c<=maxLength:
                    yield (a,b,c)
        
def gen75(a,b,c,roof):    
    for t in [(a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c),
              (a+2*b+2*c,2*a+b+2*c,2*a+2*b+3*c),
              (2*b+2*c-a,b+2*c-2*a,2*b+3*c-2*a)]:
        if (sum(t) < roof):
            yield t
            for y in gen75(t[0],t[1],t[2],roof):
                yield y

