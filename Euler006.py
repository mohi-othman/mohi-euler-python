import math

def SquareOfSums(count):
    return (sum(range(1,count+1)))**2

def SumOfSquares(count):
    return sum(map(lambda x:x**2, list(range(1,count+1))))

a=SquareOfSums(100)
b=SumOfSquares(100)
print(a,b,a-b)
