import time
import math

t = time.clock()
P = dict()
poly = list(range(3,9))
for p in poly:
    P[p]=[]

def getSequence(polysLeft, sequence, result, size):
    left = str(sequence[len(sequence)-1])[-2:]
    for right in range(11,100):
        #print (sequence[len(sequence)-1],left,right)
        newNumber = int(left+str(right))
        flag = True
        for p in polysLeft:
            if newNumber in P[p]:
                flag = False
                newPolys = list(polysLeft)
                newSeq = list(sequence)
                newPolys.remove(p)
                newSeq.append(newNumber)
                if len(newSeq)==size:
                    if str(newSeq[0])[:2] == str(newNumber)[-2:]:                        
                        result.append(newSeq)
                else:
                    getSequence(newPolys, newSeq, result, size)
                    
n = 1
while True:
    p3 = int(n*(n+1)/2)
    p4 = int(n**2)
    p5 = int(n*(3*n-1)/2)
    p6 = int(n*(2*n-1))
    p7 = int(n*(5*n-3)/2)
    p8 = int(n*(3*n-2)   )

    strikes = 0
    
    if p3>9999:
        strikes+=1
    elif p3>999:
        P[3].append(p3)
        
    if p4>9999:
        strikes+=1
    elif p4>999:
        P[4].append(p4)
        
    if p5>9999:
        strikes+=1
    elif p5>999:
        P[5].append(p5)
        
    if p6>9999:
        strikes+=1
    elif p6>999:
        P[6].append(p6)
        
    if p7>9999:
        strikes+=1
    elif p7>999:
        P[7].append(p7)
        
    if p8>9999:
        strikes+=1
    elif p8>999:
        P[8].append(p8)

    if strikes==6:
        break

    n+=1

print("polygonals generated")
print(time.clock()-t)
#poly = [3,4,5]
size = 6
result = []
for p in poly:
    polysLeft = list(poly)
    polysLeft.remove(p)
    for n in P[p]:        
        getSequence(polysLeft, [n], result, size)
        
print(result)
print(sum(result[0]))
print("done")
print(time.clock()-t)
