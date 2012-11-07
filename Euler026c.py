import math
import time

multiplier = 3

def findPrimes(minimum, maximum):
    primes = [2,3,5,7,11]
    for n in range(max(primes)+2, maximum+1,2):
        flag = True
        for p in primes:
            if n%p == 0:
                flag = False
                break

        if flag: primes.append(n)
    
    return [n for n in primes if n>=minimum]

def findRecurring(numberString, maxSlice):
    result = findFirstSlice(numberString, maxSlice)                       

    return len(result)

def findFirstSlice(numberString, maxSlice):
    result = 0

    for s in range(min(maxSlice,len(numberString)),0,-1):
        text = numberString     
        firstSlice = text[-s:]
        text = text[:-s]

        count = 0

        while(len(text)>=s):

            if firstSlice!=text[-s:]:
                break

            text = text[:-s]
            count+=1
               
        if count>0:
            
            result = s
            return findFirstSlice(firstSlice, maxSlice//2)

    if result==0:
        return numberString
        
def getDecimalPart(d, maxDigit):
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
    
    return result[:maxDigit]

def removePowers(n, numberList, cutOff):
    p = 1
    lastRemoved = 0
    while(n**p<=cutOff):
        try:
            lastRemoved = n**p
            numberList.remove(lastRemoved)
        except:
            pass
        p+=1

    return lastRemoved
   
t = time.clock()

#######################
cutOff = 1000
######################


recurring = dict()
primes = findPrimes(7, cutOff)
print("Primes found: ", time.clock()-t)

numbers = list(range(2,cutOff+1))

#known none recurring
excludeList = [2,4,5,8,10]

#exclude 1/n**x
for n in excludeList:
    removePowers(n, numbers, cutOff)

maxSlice = 1000
cutOffSlice = 1000000
resultSlice = 0
resultNumber = 0

while(maxSlice<cutOffSlice and len(numbers)>1):
    maxDigit = maxSlice * multiplier + 1
    print("max slice: ",maxSlice)
    print("number count: ",len(numbers))
    print("biggest slice so far:",    resultSlice )
    print("for number: ",resultNumber)
    print("-------------------------------------")

    for d in numbers:
        decimal = getDecimalPart(d, maxDigit)
    
        if len(decimal)<maxDigit:
            removePowers(d, numbers, cutOff)

        recurrCount = findRecurring(decimal, maxSlice)

        if d == 7:
            print("7--> ", recurrCount)
        
        if recurrCount > resultSlice:
            recurring[d] = recurrCount
            removePowers(d, numbers, cutOff)

    resultSlice = max(recurring.values())

    for k in recurring:
        if recurring[k]==resultSlice: resultNumber=k
        try:
            numbers.remove(k)
        except:
            pass

    maxSlice*=2
    
    
print("Largest slice:",resultSlice," belongs to ", resultNumber)
print("Done: ", time.clock()-t)        
            
                




