#Problem 94
#29 April 2005

#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

########## ANALYSIS ########## 
# Half of the almost equilateral triangle must be a pythagoran triangle.
# Find all primitive pythagoran triples that satisfy the problem

import HelperMath
import math

def solve(roof):
    side = roof/3
    small = side/2
    hyp = side
    big = math.sqrt(side**2 - (side/2)**2)
    maxP = small+big+hyp
    triplesGenerator = HelperMath.findAllPrimitivePythagoranTriples(maxP)    
    count = 0       
    
    for triple in triplesGenerator:
        sTriple = sorted(triple)
        a = sTriple[0]
        b = sTriple[1]
        c = sTriple[2]
        if math.fabs(2*a-c)<=1 or math.fabs(2*b-c)<=1:
            print(triple)    
            p = 0      
            if math.fabs(2*a-c)<=1:
                p = 2*c + 2*a
            else:
                p = 2*c + 2*b
            count += p
                
    return count

# Brute force function for comparing results
def solve2(roof):
    result = 0
    max = roof//3
    for n in range(6, max+1, 2):
        #print(n)
        small = n//2
        for d in range(-1,2):
            big = n+d
            med = math.sqrt(big**2-small**2)
            if int(med)==med:
                result+= small*2 + big * 2
    return result