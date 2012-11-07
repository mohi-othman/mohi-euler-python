import time

maximumSum = 0


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, node):
        self.children.append(node)

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

def traverseTree(node, sumSoFar):
    global maximumSum

    sumSoFar+=node.value
    
    if len(node.children) == 0:
        maximumSum = max(maximumSum, sumSoFar)
        return
    else:
        for child in node.children:
            traverseTree(child, sumSoFar)
       
headNode = populateTree('Euler018b.txt')
t = time.clock()
traverseTree(headNode,0)
print(maximumSum)
print(time.clock()-t)
