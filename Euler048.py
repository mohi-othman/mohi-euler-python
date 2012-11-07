import time

digitLimit = 10
cutOff = 1000

def bigMultiply(a,b):
    c = a*b
    cText = str(c)
    if len(cText) > digitLimit:
        c = int(cText[-digitLimit:])

    return c

def bigAdd(a,b):
    c = a+b
    cText = str(c)
    if len(cText) > digitLimit:
        c = int(cText[-digitLimit:])

    return c

def bigPower(a,b):
    c = 1
    for i in range(0,b):
        c = bigMultiply(a,c)

    return c

result = 0
t = time.clock()
for n in range(1,cutOff+1):
    result = bigAdd(result, bigPower(n,n))

print (result)
print ( time.clock()-t)
