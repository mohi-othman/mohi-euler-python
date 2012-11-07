import time
from functools import reduce

def makeString(length):
    result = ''
    n = 1
    while len(result)<length:
        result += str(n)
        n+=1

    return result

def getDigit(string, place):
    return int(string[place-1])

t = time.clock()
bigString = makeString(1000000)
print('big string made')
print(time.clock() - t)
m = [1,10,100,1000,10000,100000,1000000]
result = reduce(lambda a,b:a*b, map(lambda x:getDigit(bigString, x),m))
print(result)
print('result found')
print(time.clock() - t)
