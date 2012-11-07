def getFactorial(n):
    result = 1
    for i in (range(n,1,-1)):
        result*=i

    return result

def getSumOfNumbers(n):
    return(sum(map(lambda x:int(x),list(str(n)))))

number = 100
print(getSumOfNumbers(getFactorial(number)))
