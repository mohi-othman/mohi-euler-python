import time
def breakNumber(number, listSoFar, result):
    for n in range(number, 0, -1):
        print(number,n)
        newList = list(listSoFar)
        newList.append(n)        
        if number-n==0:
            result.append(newList)
        else:
            breakNumber(number-n, newList, result)
    
t = time.clock()
combos = []
breakNumber(5 , [], combos)
print(len(combos))
print(time.clock()-t)
