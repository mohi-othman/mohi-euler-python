import math

def isPrime(n):
    flag = True
    if n == 1:
        flag = False
    elif n in [2,3,5,7]:
        flag = True
    elif n%2==0:
        flag = False
    elif n%3 == 0:
        flag = False
    else:  
        r = math.floor(math.sqrt(n))
        f = 5
        while (f<=r):
            if n%f==0:
                flag = False                
                break
            if n%(f+2)==0:
                flag = False                
                break
            f+=6

    return flag

singleDigits = [1,2,3,5,7,9]
primes = [2,3,5,7]
result = [2,3,5,7]
digits = 2
while(True):    
    leftHalf = [x for x in primes if x>=10**(digits-2) and x<10**(digits-1)]
    digits+=1
    newResult = []
    for number in leftHalf:
        for digit in singleDigits:
            x = number*10 + digit
            if isPrime(x):
                primes.append(x)
                flag = True
                txt = str(x)
                for i in range(1,len(txt)):                    
                    if not isPrime(int(txt[i:])):
                        flag = False
                        break
                    
                if flag:
                    newResult.append(x)
                    print(x)
                
    if len(result) == 11+4:
        break
    else:
        result.extend(newResult)
        print(digits,len(result))
result.remove(2)
result.remove(3)
result.remove(5)
result.remove(7)
print(result, "=",len(result))
print(sum(result))
