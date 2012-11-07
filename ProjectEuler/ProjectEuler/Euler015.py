import time

class node:
    def __init__(self):
        self.children = []
            
class network:
    def __init__(self, firstNode, targetNodes):
        self.firstNode = firstNode
        self.targetNodes = targetNodes

    def getFreshResultDict(self):
        result = dict()
        for target in self.targetNodes:
            result[target] = 0
        
        return result

def move(destination, targets, resultDict):
    if destination in targets:
        resultDict[destination]+=1
    else:
        for newDestination in destination.children:
            move(newDestination, targets, resultDict)

def buildSquare(dimension):
    grid = []
    for i in range(0, dimension+1):
        row = []
        for j in range(0, dimension+1):
            newNode = node()
            row.append(newNode)
        grid.append(row)

    for i in range(0, dimension+1):
        for j in range(0, dimension+1):
            if j<dimension:
                grid[i][j].children.append(grid[i][j+1])
            if i<dimension:
                grid[i][j].children.append(grid[i+1][j])

    result = network(grid[0][0], [grid[dimension][dimension]])
    return result

def buildTriangle(dimension):
    tree = []
    for i in range(0, dimension+1):
        level = []
        for j in range(0, i+2):
            newNode = node()
            level.append(newNode)
        tree.append(level)

    for i in range(0, dimension):
        for j in range(0, i+2):
            tree[i][j].children.append(tree[i+1][j])
            tree[i][j].children.append(tree[i+1][j+1])

    result = network(tree[0][0], tree[dimension])
    return result

def buildPartialTriangle(dimension):
    if (dimension)%2==0:
        halfPoint = (dimension + 2) // 2
    else:
        halfPoint = (dimension + 1) // 2

    tree = []
    for i in range(0, dimension+1):
        level = []
        for j in range(0, (i+2,halfPoint)[i+2 > halfPoint]):
            newNode = node()
            level.append(newNode)
        tree.append(level)

    for i in range(0, dimension):
        for j in range(0, (i+2,halfPoint)[i+2 > halfPoint]):
            tree[i][j].children.append(tree[i+1][j])
            if j < halfPoint - 1:
                tree[i][j].children.append(tree[i+1][j+1])

    result = network(tree[0][0], tree[dimension])
    return result 

def solve():
    dimension = 20
    
    squareNetwork = buildSquare(dimension)
    gridResultDict = squareNetwork.getFreshResultDict()
    
    triangleNetwork = buildTriangle(dimension)
    treeResultDict = triangleNetwork.getFreshResultDict()
    
    partialTriangleNetwork = buildPartialTriangle(dimension)
    smallTreeResultDict = partialTriangleNetwork.getFreshResultDict()

    t = time.clock()    
    move(triangleNetwork.firstNode, triangleNetwork.targetNodes, treeResultDict)    
    print("Triangle network result is:", sum([x**2 for x in treeResultDict.values()]))
    print("Triangle network done in:",time.clock() - t)
    
    t = time.clock()    
    move(partialTriangleNetwork.firstNode, partialTriangleNetwork.targetNodes, smallTreeResultDict)    
    if dimension%2==0:
        result = 2 * sum([x**2 for x in smallTreeResultDict.values() if x < max(smallTreeResultDict.values())]) + max(smallTreeResultDict.values())**2
    else:
        result = 2 * sum([x**2 for x in smallTreeResultDict.values()])
    print("Partial triangle result is:", result)
    print("Partial triangle network done in:",time.clock() - t)
        
    t = time.clock()    
    move(squareNetwork.firstNode, squareNetwork.targetNodes, gridResultDict)
    print("Square network result is:", sum(gridResultDict.values()))
    print("Square network done in:",time.clock() - t)
    
    
####################################################################################

def solvePascalTriangle(dimension):
    t = time.clock()    
    level = [1,1]
    for i in range(2, dimension+1):
        newLevel = [1]
        for j in range(0, len(level)-1):
            newLevel.append(level[j]+level[j+1])
        newLevel.append(1)
        level = newLevel
    print("Result is:", sum([x**2 for x in level]))
    print("Pascal triangle done in:",time.clock() - t)
    
