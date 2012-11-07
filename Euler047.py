import time
import math

pastFactors = dict()

def getPrimeFactors(n):
    number = n
    result = []
    if number%2 == 0:
        result.append(2)
        while number%2 == 0:
            number/=2            

    f = 3
    while f<=number:
        if number in pastFactors:
            result.extend(pastFactors[number])
            break
        
        if number%f == 0:
            result.append(f)
            while number%f == 0:
                number/=f             
        f+=2

    pastFactors[n] = result
    return result

count = 4
n = 2
t = time.clock()
while True:
    flag = True
    for i in range(0,count):
        if len(getPrimeFactors(n+i)) != count:
            n += i+1
            flag = False
            break

    if flag:
        print(n)
        print(time.clock()-t)
        break
