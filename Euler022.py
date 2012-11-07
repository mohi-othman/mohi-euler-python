from functools import reduce
file = open("Euler022.txt")
text = file.readline()
names = text.split(",")
names= list(map(lambda x:(x.replace("\"","")), names))
names.sort()
s=0

for i in range(0,len(names)):
    s+=(i+1) * reduce(lambda x,y: x+y, map(lambda x:ord(x)-64,names[i]))

print(s)
