import math

#Euler 80
#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

# Find root using digit by digit calculation
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def longRoot(n, precision):
    result = '0'
    c= 0
    number = str(n)
    if len(str(math.floor(n))) % 2 != 0:
        number = '0' + number

    while len(result)<=precision+3:
        if len(number)>0:
            c = c * 100 + int(number[:2])
        else:
            c = c * 100

        for x in range(9,-1,-1):            
            y = (20 * int(result) + x) * x
            if y<=c:
                result += str(x)
                c -= y
                if len(number)>0:
                    number = number[2:]

                break
    
    return result[1:]





def solve(roof):    
    squares = [x**2 for x in range(1,int(math.sqrt(roof))+1)]
    solveSet = [x for x in range(1,roof+1) if x not in squares]
    s = 0
    for n in solveSet:
        s += sum([int(x) for x in longRoot(n,roof)[:roof]])
    
    return s
