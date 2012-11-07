cutOff = 1000000
results = []

def isPalindorme(number):
    if len(number) == 1:
        return True
    
    leftHalf = ''
    rightHalf = ''
    halfPoint = len(number)//2
    leftHalf = number[:halfPoint]
    rightList = list(number[-halfPoint:])
    rightList.reverse()
    rightHalf = ''.join(rightList)

    return (leftHalf==rightHalf)
        
for n in range(0,cutOff):
    tenText = str(n)
    binText = bin(n)[2:]
    if isPalindorme(tenText) and isPalindorme(binText):
        results.append(n)

for n in results:
    print(n, bin(n)[2:])
print(sum(results))
