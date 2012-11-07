import time

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parents = [] 

    def addChild(self, node):
        self.children.append(node)
        node.parents.append(self)
        
def populateTree(fileName):
    file = open(fileName)
    lines = file.readlines()
    preProcess = []
    for line in lines:
        newLevel = []
        for item in line.strip().split(" "):
            newLevel.append(TreeNode(int(item)))
        preProcess.append(newLevel)

    for level in range(0, len(preProcess)-1):
        index = 0
        for node in range(0, len(preProcess[level])):
            preProcess[level][node].addChild(preProcess[level+1][index])
            index+=1
            preProcess[level][node].addChild(preProcess[level+1][index])

    return preProcess[0][0]

def collapseLevel(nodes):
    nextLevel = set()
    for node in nodes:
        for child in node.children:            
            nextLevel.add(child)
            
    if len(nextLevel)==0:
        print('done')
        return nodes   
    
    for newNode in nextLevel:
        newNode.value += max([x.value for x in newNode.parents])
    
    return collapseLevel(nextLevel)


def solve():
    headNode = populateTree('Euler067.txt')
    level = {headNode}
    result = collapseLevel(level)
    
    return max([x.value for x in result])

    
t = time.clock()
print(solve())
print(time.clock()-t)

    
