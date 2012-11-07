from functools import *
   
file = open("Euler011.txt")
grid = []
for line in file.readlines():
    grid.append([int(x) for x in line.split(' ')])

N = [(0,0), (0,-1), (0,-2), (0,-3)]
S = [(0,0), (0,1), (0,2), (0,3)]
W = [(0,0), (-1,0), (-2,0), (-3,0)]
E = [(0,0), (1,0), (2,0), (3,0)]

NE = [(0,0), (1,-1), (2,-2), (3,-3)]
NW = [(0,0), (-1,-1), (-2,-2), (-3,-3)]
SE = [(0,0), (1,1), (2,2), (3,3)]
SW = [(0,0), (-1,1), (-2,2), (-3,3)]

getLine = lambda point, direction: [grid[d[1]+point[1]][d[0]+point[0]] for d in direction]
getProduct = lambda valueList: reduce(lambda x,y:x*y, valueList)

products = []
for x in range(0, len(grid[0])):
    for y in range(0, len(grid)):        
        if x<=16:
            products.append(getProduct(getLine((x,y),E)))
        if x>=3:
            products.append(getProduct(getLine((x,y),W)))
        if y<=16:
            products.append(getProduct(getLine((x,y),S)))
        if y>=3:
            products.append(getProduct(getLine((x,y),N)))
        if x<=16 and y<=16:
            products.append(getProduct(getLine((x,y),SE)))
        if x>=3 and y>=3:
            products.append(getProduct(getLine((x,y),NW)))
        if x>=3 and y<=16:
            products.append(getProduct(getLine((x,y),SW)))
        if x<=16 and y>=3:
            products.append(getProduct(getLine((x,y),NE)))
                        
print(max(products))
