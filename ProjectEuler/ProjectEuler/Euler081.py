# Euler 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


#   131	673	234	103	18
#   201	96	342	965	150
#   630	803	746	422	111
#   537	699	497	121	956
#   805	732	524	37	331

# Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

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

    # Find diagonal and pascal triangles
    diagonal = []
    pascalLT = []
    pascalRB = []
        
    
    for i in range(0,dimension):
        diagonal.append(matrix[dimension-i-1][i])

    for level in range(0, dimension-1):
        row = []
        for count in range(0, level+1):
            row.append(matrix[level-count][count])
        pascalLT.append(row)

    for level in range(0, dimension-1):
        row = []
        for count in range(0, level+1):
            row.append(matrix[dimension-1-count][dimension-1-level+count])
        pascalRB.append(row)

    #Solve LT pascal triangle
    result = [pascalLT[0][0]]
    for level in range(1, dimension-1):
        row = pascalLT[level]
        newResult = []
        for x in range(0, len(row)):
            if x==0:
                newResult.append(row[0] + result[0])
            elif x==len(row)-1:
                newResult.append(row[len(row)-1] + result[len(result)-1])
            else:
                newResult.append(row[x] + min(result[x-1],result[x]))
        
        result = newResult
    
    
    # Add to diagonal 
    newResult = []
    for x in range(0, len(diagonal)):
        if x==0:
            newResult.append(diagonal[0] + (result[0]))
        elif x==len(diagonal)-1:
            newResult.append(diagonal[x] + (result[len(result)-1]))
        else:
            newResult.append(diagonal[x] + min(result[x-1] , result[x]))
    
    result = newResult

    

    #Solve RB pascal triangle        
    for level in range(len(pascalRB)-1,-1,-1):
        row = pascalRB[level]
        newResult = []

        for x in range(0, len(row)):
            newResult.append(row[x] + min(result[x],result[x+1]))
        
        result = newResult
    
    return result
    
    

