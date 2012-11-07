import time

cutOffNumber = 10000
cutOffIteration = 50
nonLychrels = []

def isPalindorme(number):
    text = str(number)
    leftHalf = list(text[:len(text)//2])
    rightHalf = list(text[-(len(text)//2):])
    rightHalf.reverse()
    return leftHalf == rightHalf

def isLychrel(number):   
    tempList = []    
    
    for i in range(0, cutOffIteration):
        if number in nonLychrels:
            return False
        
        reverseNumberText = list(str(number))
        reverseNumberText.reverse()
        reverseNumber = int(''.join(reverseNumberText))
        x = number + reverseNumber
        tempList.extend([number, reverseNumber])
        
        if isPalindorme(x):
            nonLychrels.extend(tempList)
            return False            
        else:            
            number = x
            
    return True

def solve():
    count = 0
    for n in range(1, cutOffNumber):
        if isLychrel(n): count+=1

    return count


t = time.clock()            
print(solve())
print(time.clock() - t)
