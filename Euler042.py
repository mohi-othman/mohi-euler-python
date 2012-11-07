from functools import reduce

def getWordValue(word):
    letters = list(word.upper())
    return sum(map(lambda x:ord(x)-64, letters))
    
file = open('Euler042.txt')
lines = file.readlines()
bigString = ''.join(lines)
words = bigString.split(',')
values = list(map(lambda x:getWordValue(x.replace('"','')), words))

triangles = []
maxValue = max(values)
index = 1
triangle = 1

while(triangle<=maxValue):
    triangles.append(triangle)
    index += 1
    triangle += index

count = 0

for t in triangles:
    count += values.count(t)

print(count)
