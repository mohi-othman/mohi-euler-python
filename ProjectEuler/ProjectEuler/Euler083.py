#Problem 83
#19 November 2004

#NOTE: This problem is a significantly more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


#   131	673	234	103	18
#   201	96	342	965	150
#   630	803	746	422	111
#   537	699	497	121	956
#   805	732	524	37	331

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

import math

class node:
    def __init__(self, coordinates, pathCost, hCost, parent):
        self.coordinates = coordinates
        self.pathCost = pathCost
        self.hCost = hCost
        self.parent = parent

def solve():
    file = open('Euler081.txt')
    lines = file.readlines()
    matrix = []    
    for line in lines:
        if len(line.strip())>0:
            row = [int(x) for x in line.split(',') if x!='']
            matrix.append(row)

    if len(matrix)!=len(matrix[0]):
        return 'invalid matrix'

    dimension = len(matrix)       

    # A* algorithm with h=0 (Djikstra)
    
    # Build cost dict
    costDict = dict()
    for x in range(0,dimension):
        for y in range(0,dimension):
            costDict[(x,y)] = matrix[x][y]

    # Average value of node to use in heuristic cost estimate function. NOT USED
    avg = sum([matrix[x][y] for x in range(0,dimension) for y in range(0,dimension)]) / (dimension*dimension)       
    H = lambda a,b: math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) * avg

    start = (0,0)
    finish = (dimension-1,dimension-1)
    
    startNode = node(start, costDict[start], H(start,finish), None)
    
    offsets = [(1,0),(0,1),(-1,0),(0,-1)]
    openSet = [startNode]
    closedSet = set()
    chosen = None
    
    while len(openSet)>0:
        openSet.sort(key=lambda x:x.pathCost )
        
        chosen = openSet[0]
        
        if chosen.coordinates == finish:
            break

        openSet.remove(chosen)
        closedSet.add(chosen.coordinates)

        endPoint = chosen.coordinates                
        neighbours =[newPoint for newPoint in [(endPoint[0]+offset[0],endPoint[1]+offset[1]) for offset in offsets]]

        for n in neighbours:
            if n not in costDict.keys() or n in closedSet:
                continue 
            elif n not in [x.coordinates for x in openSet]:
                newNode = node(n, chosen.pathCost + costDict[n], H(n,finish), chosen)
                openSet.append(newNode)
            else:
                existingNode=[x for x in openSet if x.coordinates == n][0]
                newCost = chosen.pathCost + costDict[n] 
                if newCost < existingNode.pathCost:
                    newNode = node(n, newCost, H(n,finish), chosen)
                    openSet.remove(existingNode)
                    openSet.append(newNode)
    
    
    print(chosen.pathCost)
    #while chosen!=None:
    #    print(chosen.coordinates)
    #    chosen = chosen.parent
        


        