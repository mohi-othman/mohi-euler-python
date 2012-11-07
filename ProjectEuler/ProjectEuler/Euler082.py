# Euler 82

# NOTE: This problem is a more challenging version of Problem 81.
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

#   131	673	234	103	18
#   201	96	342	965	150
#   630	803	746	422	111
#   537	699	497	121	956
#   805	732	524	37	331

# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

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

    prevColumn = [matrix[row][0] for row in range(0, dimension)]
    
    for column in range(1, dimension):
        #print(prevColumn)
        newColumn = [matrix[row][column] for row in range(0, dimension)]
        resultColumn = []
        for newIndex in range(0, len(newColumn)):
            possibles = []            
            for prevIndex in range(0, len(prevColumn)):
                if newIndex==prevIndex:
                    possibles.append(prevColumn[prevIndex] + newColumn[newIndex])
                elif prevIndex < newIndex:
                    possibles.append(prevColumn[prevIndex] + sum([newColumn[i] for i in range(prevIndex,newIndex)])+ newColumn[newIndex])
                    possibles.append(sum([prevColumn[i] for i in range(prevIndex,newIndex+1)]) + newColumn[newIndex])
                elif prevIndex > newIndex:
                    possibles.append(sum([prevColumn[i] for i in range(newIndex,prevIndex+1)]) + newColumn[newIndex])
                    possibles.append(prevColumn[prevIndex] + sum([newColumn[i] for i in range(newIndex+1,prevIndex+1)])+ newColumn[newIndex])
                
            resultColumn.append(min(possibles))

        prevColumn = resultColumn

    #print(prevColumn)

    return min(prevColumn)

    