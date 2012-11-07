import time

def factorial(n):
	s = 1
	for i in range(1,n+1):
		s*=i
	return s


t = time.clock()
maxSlice = 1000
#maxDigit = factorial(maxSlice)
maxDigit = maxSlice*(maxSlice-1)
print("Factorial found: ", time.clock()-t)

cutOff = 1000
fractionDict = dict()
recurring = dict()

for d in range(2,cutOff+1):
    result = ""
    number = 10

    while(len(result)<maxDigit):
        factor = 1

        while number<d:
            factor+=1
            number = number * 10**factor
            
        result += str(int(number/d))
        number = number%d
        if number == 0: break
    
    fractionDict[d] = result[:maxDigit]

print("Division completed: ", time.clock()-t)
      
for fraction in fractionDict:
    for slice in range(1,maxSlice+1):        
        text = fractionDict[fraction]
        if len(text)<maxDigit:
            break
        
        flag = True            
        firstSlice = text[:slice]
        text = text[slice:]
        while(len(text)>0):          
            if firstSlice!=text[:slice]:
                flag = False
                break

            text = text[slice:]

        if flag:
            recurring[slice] = (fraction, firstSlice)
            break

slices = list(recurring.keys())
slices.sort()
slices.reverse()
print(slices[0], recurring[slices[0]])
print(time.clock()-t)

        

