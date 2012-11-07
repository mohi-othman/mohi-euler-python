class Combo:
    def __init__(_self):
        _self.CurrentString = ""
        _self.UsedNodes = set()
        _self.RemainingNodes = set()

    def __init__(_self, CurrentString, UsedNodes, RemainingNodes):
        _self.CurrentString = CurrentString
        _self.UsedNodes = UsedNodes
        _self.RemainingNodes = RemainingNodes

    def Length(_self):
        return len(_self.CurrentString)



def shorten(node1, node2):
    length = min((len(node1),len(node2)))
    result = node1 + node2
    for i in range(length,0,-1):
        if node1[-i:]==node2[:i]:
            result = node1[:len(node1)-i] + node2
            break    
    return result

def Solve():
    file = open('Euler079.txt')

    lines = file.readlines()
    nodes = set()
    
    #Read from file
    for line in lines:
        if len(line.strip())>0:
            node = line.strip()
            nodes.add(node)

    comboDict = dict()
    combos = []
    for i in range(0, len(nodes)+1):
        comboDict[i] = []

    for node in nodes:
        remainingNodes = set(nodes)
        remainingNodes.remove(node)
        for otherNode in remainingNodes:
            newString = shorten(node,otherNode)
            newRemainingNodes = set(remainingNodes)
            newRemainingNodes.remove(otherNode)
            #newRemainingNodes = set([x for x in remainingNodes if not x in newString])
            newCombo = Combo(newString, {node,otherNode}, newRemainingNodes)
            combos.append(newCombo)

    comboDict[2] = combos        

    i = 1
    while True:
        newCombos = []
        for combo in combos:
            for node in combo.RemainingNodes:
                newString = shorten(combo.CurrentString,node)
                #newRemainingNodes = set([x for x in combo.RemainingNodes if not x in newString])
                newRemainingNodes = set(combo.RemainingNodes)
                newRemainingNodes.remove(node)
                
                newUsedNodes = set(combo.UsedNodes)
                newUsedNodes.add(node)

                newCombo = Combo(newString,newUsedNodes,newRemainingNodes)
                newCombos.append(newCombo)                        
                comboDict[len(newUsedNodes)].append(newCombo)


        #newShortLength = min(map(lambda x:x.Length(), newCombos))
        #combos = [x for x in newCombos if x.Length() == newShortLength]
        combos = newCombos
        
        if i >= len(nodes)/2:
            break
        i+=1
            
    newCombos = []
    for combo in combos:
        otherCombo = [x for x in comboDict[len(combo.RemainingNodes)] if x.UsedNodes==combo.RemainingNodes]
        if len(otherCombo)>0:
            newCombos.append(shorten(combo.CurrentString, otherCombo[0].CurrentString))
    
    shortestLength = min(map(lambda x:len(x),newCombos))
    result = [x for x in newCombos if len(x)==shortestLength]
    print(result[0], shortestLength)




    