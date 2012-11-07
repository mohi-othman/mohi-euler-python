import math

def IsPalindorme(number):
    string = str(number)
    halfLength = math.floor(len(string)/2)
    left = list(string[0:halfLength])
    right = list(string[len(string)-halfLength:len(string)])
    right.reverse()
    return(left==right)

def Test(minN, maxN):
    palindormes = dict()
    for x in range(maxN,minN,-1):
        for y in range(maxN,minN,-1):
            if IsPalindorme(x*y):
                palindormes[x*y]=(x,y)

    maxPal = max(palindormes.keys())
    return(maxPal, palindormes[maxPal])

print(Test(111,999))
