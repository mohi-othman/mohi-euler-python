#Problem 88
#04 February 2005

#A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1  a2  ...  ak.

#For example, 6 = 1 + 2 + 3 = 1  2  3.

#For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

#k=2: 4 = 2  2 = 2 + 2
#k=3: 6 = 1  2  3 = 1 + 2 + 3
#k=4: 8 = 1  1  2  4 = 1 + 1 + 2 + 4
#k=5: 8 = 1  1  2  2  2 = 1 + 1 + 2 + 2 + 2
#k=6: 12 = 1  1  1  1  2  6 = 1 + 1 + 1 + 1 + 2 + 6

#Hence for 2k6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

#In fact, as the complete set of minimal product-sum numbers for 2k12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

#What is the sum of all the minimal product-sum numbers for 2k12000?

import math
import itertools
import functools

def findLowestForTwoTerms(n):
    # find minimum for two numbers x and y, and the rest are ones. y is known. This is the upper limit for the rest.
    # xy = x + y + (n-2)
    # xy-x = y+n-2
    # (y-1)x = y+n-2
    # x = (y+n-2)/(y-1)
        
    # y=2
    lowest = (2+n-2) * 2
    y = 3
    while True:
        x = (y+n-2)/(y-1)            
        if x*y > lowest:
            break
        elif int(x)==x:
            lowest = x * y                
        y+=1
    return lowest

def solve(roof):
    result = set()
    for n in range(2, roof+1):        
        lowest = findLowestForTwoTerms(n) 
        
        # try combination of other numbers:
        for terms in range(3, n+1):
            # if all twos is larger than current lowest value then that means no more possible solutions. Exit the loop
            if 2**terms >= lowest:
                break

            # get all possible combos for terms-1 that don't exceed current lowest number
            combos = list()
            # start with a list of numbers from 2 to largest possible number N where N**terms doesn't exceed current lowest number
            for x in range(2, math.ceil(lowest / ((terms - 1) ** 2)) + 1):
                combos.append([x])

            for i in range(2, terms):
                newCombos = list()
                for combo in combos:
                    mult = functools.reduce(lambda x,y:x*y, combo)
                    rest = 2 ** (terms - len(combo) - 1)
                    upperLimit = int(lowest / (mult * rest))
                    #start range with the max number in the combo (to avoid duplicates) and end with upperLimit to avoid going over current lowest number
                    for newN in range(max(combo), upperLimit+1):
                        newCombo = list(combo)
                        newCombo.append(newN)
                        newCombos.append(newCombo)
                combos = newCombos
            
            # calculate last term to satisfy problem the same way we did in findLowestForTwoTerms
            for combo in combos:
                sums = sum(combo)
                mult = functools.reduce(lambda x,y:x*y, combo)
                x = (sums + n-terms) / (mult - 1)                            
                if int(x)==x:
                    newLowest = x * mult
                    if newLowest<lowest:
                        lowest = newLowest
                        change = True
            

        print(n,lowest)
        result.add(lowest)
    
    return sum(result)


########### ARCHIVED SOLUTIONS ###########
def solve3(roof):
    result = set()
    for n in range(2, roof+1):        
        lowest = findLowestForTwoTerms(n) 
        
        # try combination of other numbers:
        for terms in range(3, n+1):
            upperLimit = math.ceil(lowest / ((terms - 1) ** 2))
            if upperLimit < 2:
                break
            #get combos for all but the last number
            combos = list(itertools.combinations_with_replacement(range(2,upperLimit+1),terms-1))
            for combo in combos:
                sums = sum(combo)
                mult = functools.reduce(lambda x,y:x*y, combo)
                x = (sums + n-terms) / (mult - 1)                            
                if int(x)==x:
                    newLowest = x * mult
                    if newLowest<lowest:
                        lowest = newLowest

        print(n,lowest)
        result.add(lowest)
    
    return sum(result)
       
def solve2(roof):
    result = set()
    for n in range(2, roof+1):        
        lowest = findLowestForTwoTerms(n) 
        
        # try combination of other numbers:
        for terms in range(3, n+1):
            #get all possible combos for terms-1 that don't exceed current lowest number
            combos = list()
            for x in range(2, math.ceil(lowest / ((terms - 1) ** 2)) + 1):
                combos.append([x])

            for i in range(2, terms):
                newCombos = list()
                for combo in combos:
                    mult = functools.reduce(lambda x,y:x*y, combo)
                    rest = 2 ** (terms - len(combo) - 1)
                    upperLimit = int(lowest / (mult * rest))
                    for newN in range(2, upperLimit+1):
                        newCombo = list(combo)
                        newCombo.append(newN)
                        newCombos.append(newCombo)
                combos = newCombos
            #calculate last term to satisfy problem
            for combo in combos:
                sums = sum(combo)
                mult = functools.reduce(lambda x,y:x*y, combo)
                x = (sums + n-terms) / (mult - 1)                            
                if int(x)==x:
                    newLowest = x * mult
                    if newLowest<lowest:
                        lowest = newLowest
        print(n,lowest)
        result.add(lowest)
    
    return sum(result)
       

       
