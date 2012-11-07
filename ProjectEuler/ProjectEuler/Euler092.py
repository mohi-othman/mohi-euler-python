#Problem 92
#01 April 2005

#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44  32  13  10  1  1
#85  89  145  42  20  4  16  37  58  89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

cache = dict()
backTrackCache = dict()

def getNextInSeries(series):    
    lastNumber = series[len(series)-1]
    if lastNumber in cache:
        series.append(cache[lastNumber]) 
        return 
    nextNumber = sum([int(digit)**2 for digit in str(lastNumber)])
    series.append(nextNumber)
    if nextNumber!=1 and nextNumber!=89:
        getNextInSeries(series)

def backTrackAndCache(number, cacheValue):
    if number==1 or number==89 or number not in backTrackCache:
        return
    else:
        for n in backTrackCache[number]:
            cache[n] = cacheValue
            backTrackAndCache(n, cacheValue)

def solve(roof):
    result1  = 0
    result89 = 0
    
    for i in range(1, roof+1):
        square = sum([int(digit)**2 for digit in str(i)])
        if square not in backTrackCache:
            backTrackCache[square] = [i]
        else:
            backTrackCache[square].append(i)

    for n in range(1, roof+1):
        series = [n]
        getNextInSeries(series)
        lastNumber = series[len(series)-1]
        for x in range(0,len(series)-2):
            cache[series[x]] = lastNumber
        
        backTrackAndCache(n, lastNumber)

        if lastNumber == 1:
            result1 += 1
        elif lastNumber == 89:
            result89 += 1
                
    return result89
