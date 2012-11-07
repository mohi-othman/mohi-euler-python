from math import *

def solve(L):
    limit = int(sqrt(L))    
    for n in range(1, limit+1):
        for m in range(1, n):
            if n*(n+m)==500:
                a = n**2 - m**2
                b = 2 * m * n
                c = n**2 + m**2
                return (a,b,c)

a, b, c = solve(500)
print(a*b*c)
