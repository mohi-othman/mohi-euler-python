def isPalindorme(number):
    numString = str(number)
    halfLength = int(len(numString)/2)
    left = list(numString[:halfLength])
    right = list(numString[-halfLength:])
    right.reverse()
    return (left==right)

palindormes = []
minN = 111
maxN = 999
for x in range(maxN,minN,-1):
    for y in range(maxN,minN,-1):
        p = x*y
        if isPalindorme(p):
            palindormes.append(p)

print(max(palindormes))
