import time
from functools import reduce
size = 20
count = 0
countDict=dict()

def move(location,direction): #0: right, 1:down
    global count
    #print(location,direction)
    if direction == 0:
        location = (location[0]+1,location[1])
    elif direction == 1:
        location = (location[0],location[1]+1)

    #print("=",location)
    if location == (size,size):
        count += 1
        return
    else:
        if location[0]<size: move(location,0)
        if location[1]<size: move(location,1)

def moveTowards(source, location, target, direction): #0: right, 1:down
    global countDict
    if direction == 0:
        location = (location[0]+1,location[1])
    elif direction == 1:
        location = (location[0],location[1]+1)

    if location == target:
        if source in countDict.keys():
            countDict[source]+=1
        else:
            countDict[source]=1
            
        return
    else:
        if location[0]<target[0]: moveTowards(source, location,target,0)
        if location[1]<target[1]: moveTowards(source, location,target,1)
    
def solve():
    global count
    points = []
    for i in range(0,size+1):
        points.append((size-i,i))

    print(points)
    count = 0
    for point in points:
        if point[0]<size: moveTowards(point, point,(size,size),0)
        if point[1]<size: moveTowards(point, point,(size,size),1)

    print(countDict)
    
    count = reduce(lambda x,y: x + y, map(lambda x:x*x, countDict.values()))

        
t = time.clock()
#move((0,0),0)
#move((0,0),1)
solve()

print(count)
print(time.clock() - t)

