#Problem 93
#15 April 2005

#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, , *, /) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3)  1
#36 = 3 * 4 * (2 + 1)

#Note that concatenations of the digits, like 12 + 34, are not allowed.

#Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a  b < c  d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

import itertools

def getAllFormulas(numberSet):
    numberCombos = list(itertools.permutations(numberSet))
    ops = ('*','+','-','/')
    opsCombos = list(itertools.product(ops,ops,ops))
    parenthesisPlacement = ((0,3),(0,1),(1,2),(2,3),(0,2),(1,3))

    results = set()

    for nCombo in numberCombos:
        for opCombo in opsCombos:
            for placement in parenthesisPlacement:
                formula = ''
                for i in range(0,4):
                    if i > 0:
                        formula += opCombo[i-1]

                    if i == placement[0]:
                        formula += '('
                    
                    formula += str(nCombo[i])

                    if i == placement[1]:
                        formula += ')'
                try:
                    results.add(eval(formula))
                except:
                    pass

    return sorted(list(results))

def getLongestSeries(listOfNumbers):
    n = 0
    while True:        
        if n+1 not in listOfNumbers:
            break
        n+=1
    return n

def solve():    
    resultDict = dict()
    numberSets = list(itertools.permutations(range(0,10),4))    
    n = 1
    for ns in numberSets:
        resultDict[ns] = getLongestSeries(getAllFormulas(ns))
        print(n)
        n+=1
    result = sorted(resultDict, key=lambda x:resultDict[x], reverse=True)[0]
    return (result, resultDict[result])
