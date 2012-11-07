import time
maxPlace = 10
permutations = []

def getPermutation(digit,soFar):
    soFar += str(digit)

    if len(soFar)==maxPlace:
        permutations.append(soFar)
        return
    
    for i in range(maxPlace):
        if str(i) not in soFar:
            getPermutation(i,soFar)


t = time.clock()
getPermutation("","")
permutations.sort()
print(len(permutations))
print(permutations[1000000-1])
print(time.clock() - t)

