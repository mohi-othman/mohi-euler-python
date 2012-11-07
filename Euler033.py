from functools import reduce

maxNumber = 98
minNumber = 10
result = []
for d in range(minNumber, maxNumber+1):
    for n in range(minNumber, d):
        if d%10 == 0 and n%10 == 0:
            continue
        else:
            nSet = set(list(str(n)))
            dSet = set(list(str(d)))
            common = nSet.intersection(dSet)
            if len(common)!=1:
                continue
            else:
                r = n/d
                newN = int(common.pop())
                newD = newN
                common.add(str(newN))
                if len(nSet.difference(common))>0:
                    newN = int((nSet.difference(common)).pop())
                if len(dSet.difference(common))>0:
                    newD = int((dSet.difference(common)).pop())
                if newD == 0:
                    continue
                
                newR = newN/newD

                if newR == r:
                    print(n,"/",d," = ",newN,"/",newD)
                    result.append((n,d))

print(result)

dList = []
nList = []
product = 1
for x in result:
    nList.append(x[0])
    dList.append(x[1])
    product*=x[0]/x[1]

bigD = reduce(lambda a,b:a*b, dList)
bigN = reduce(lambda a,b:a*b, nList)


print(bigN,bigD)
print(product)

for i in range(bigD,bigN-1,-1):
    if bigN%i == 0 and bigD%i == 0:
        print(bigN/i, "/", bigD/i)

            
            
