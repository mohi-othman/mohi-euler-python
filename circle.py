from functools import reduce
r=int(input())//2
print(reduce(lambda a,b:''.join(a)+'\n'+''.join(b),[[' *' if x*x+y*y-r*r<9 else '  ' for x in range(-r,r+1)] for y in range(-r,r+1)]))
    
        

