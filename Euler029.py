minA = 2
maxA = 100
minB = 2
maxB = 100
combos = set()

for a in range(minA,maxA+1):
    for b in range(minB,maxB+1):
        combos.add(a**b)

print(len(combos))
