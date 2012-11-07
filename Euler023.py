import math
cutOff = 28123 
abundants = []

for number in range(1,cutOff):
    factors = {i for i in range(1, int(math.sqrt(number))+1) if number%i==0}

    factors = factors.union(set(map(lambda x:number/x, factors)))
    sumD = sum(factors) - number

    if sumD > number:
        abundants.append(number)

twoAbundantSums = set()

for x in abundants:
    for y in abundants:
        twoAbundantSums.add(x+y)

allNumbers = set(range(1, cutOff))

result = allNumbers.difference(twoAbundantSums)

print("abundants ",len(abundants))
print("allNumbers ",len(allNumbers))
print("result ",len(result))
print(sum(result))

    
    
