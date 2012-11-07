#Problem 90
#04 March 2005

#Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

#For example, the square number 64 could be formed:


#In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

#For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

#However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

#In determining a distinct arrangement we are interested in the digits on each cube, not the order.

#{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

import itertools

# set all 9's in squares to 6's    
squares = [format(x**2,'02d').replace('9','6') for x in range(1,10)]

def getFirstCubes():
    result = [[n] for n in range(0,10)]
    for f in range(1,7):
        newResult = []
        for combo in result:            
            for x in range(max(combo)+1, 10):
                newCombo = list(combo)
                newCombo.append(x)
                newResult.append(newCombo)
        result = newResult
    return result

def fillOutCube(cube):
    result = [cube]
    for index in range(len(cube)+1, 7):
        newResult = []
        for c in result:                        
            for newNumber in [str(x) for x in range(0,10) if str(x) not in c]:
                newCube = list(c)
                newCube.append(newNumber)
                newResult.append(newCube)
        result = newResult
    return result
                   

def findSecondCubeCandidate(cube):
    tempCube = list(cube)
    if '9' in tempCube:
        tempCube.remove('9')
        if '6' not in tempCube:
            tempCube.append('6')
    valid = True # to check if its a valid cube
    requiredFaces = set()    
    for square in squares:        
        candidates = set()
        if square[0] not in tempCube and square[1] not in tempCube:
            valid = False
            break
        if square[0] in tempCube:
            candidates.add(square[1])
        if square[1] in tempCube:
            candidates.add(square[0])
        if '6' in candidates:
            candidates.add('9')
        requiredFaces.add(tuple(candidates))
    
    requiredFaces = list(requiredFaces)
    
    if valid:
        essentialCubes = [x for x in requiredFaces[0]]
        index = 1
        while index <= len(requiredFaces)-1:
            newEssentialCubes = []
            for cube in essentialCubes:
                for n in [x for x in requiredFaces[index] if x not in cube]:
                    newCube = list(cube)
                    newCube.append(n)                    
                    newEssentialCubes.append(newCube)
            essentialCubes = newEssentialCubes
            index+=1

        essentialCubes = [sorted(x) for x in essentialCubes if len(x)<=6]

        result = list()

        for c in essentialCubes:
            result.extend(fillOutCube(c))
                    
        return set([tuple(sorted(x)) for x in result])
    else:
        return []
                      
    

def solve2():   

    # all possible first cubes
    firstCubes = [[str(digit) for digit in cube] for cube in itertools.combinations(range(0,10),6)]    
    firstCubes = set([tuple(sorted(x)) for x in firstCubes])

    pairs = set()
    
    for cube in firstCubes: 
        secondCubes = findSecondCubeCandidate(cube)
        for cube2 in secondCubes:
            pairs.add((tuple(cube),tuple(cube2)))
                
    result = set()
    for pair in pairs:
        if (pair[1],pair[0]) not in result:
            result.add(pair)
    
    result = list(result)
    result.sort(key=lambda x:x[1])
    result.sort(key=lambda x:x[0])
    
    #for i in range(0, len(result)):
    #    print(result[i])
    #    if (i+1)%20==0:
    #        input()

    return len(result)

def solve():
    result = list()
    firstCubes = [sorted([str(digit) for digit in cube]) for cube in itertools.combinations(range(0,10),6)]    
    for cube in firstCubes:
        secondCubes = [sorted([str(digit) for digit in cube]) for cube in itertools.combinations(range(0,10),6)]
        for cube2 in secondCubes:
            tempCube = list(cube)
            if '9' in tempCube:
                tempCube.remove('9')
                if '6' not in tempCube:
                    tempCube.append('6')
            tempCube2 = list(cube2)
            if '9' in tempCube2:
                tempCube2.remove('9')
                if '6' not in tempCube2:
                    tempCube2.append('6')
            valid = True
            for square in squares:
                if (square[0] in tempCube and square[1] in tempCube2) or (square[1] in tempCube and square[0] in tempCube2):
                    pass
                else:
                    valid = False
                    break
            if valid:
                result.append((tuple(cube),tuple(cube2)))
    final = set()
    for cube in result:
        if (cube[1],cube[0]) not in final:
            final.add(cube)
    return len(final)



                        


