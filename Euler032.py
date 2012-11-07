from functools import reduce

def isPanDigital(number, digitCount):
    if len(str(number)) != digitCount:
        return False
    pattern = reduce(lambda a,b: str(a)+str(b), range(1,digitCount+1))
    numString = list(str(number))
    numString.sort()
    if pattern == ''.join(numString):
        return True
    else:
        return False
    

digitCount = 9
maxNumber = 10**(digitCount//2) - 1
resultSet = set()

for x in range(1,maxNumber+1):
    for y in range(1,maxNumber+1):
            z = x * y
            number = str(x) + str(y) + str(z)
            if isPanDigital(number, digitCount):
                print(x,y,z)
                resultSet.add(z)
            else:
                if len(number)>digitCount:
                    break

print(resultSet)
print(reduce(lambda a,b: a+b, resultSet))
