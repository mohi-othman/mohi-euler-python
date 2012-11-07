size = 1001
area = size**2

grid = []
for y in range(0,size):
    row = []
    for x in range(0,size): row.append(0)
    grid.append(row)

center = int(size/2)

x = center
y = center
grid[y][x] = 1
fillCount = 1
index = 2
direction = 0   #0:up
                #1:right
                #2:down
                #3:left
while(fillCount<area):   

    if direction == 0:
        y-=1
        if grid[y][x+1]==0:
            direction = 1
            
    elif direction == 1:
        x+=1
        if grid[y+1][x]==0:
            direction = 2
            
    elif direction == 2:
        y+=1
        if grid[y][x-1]==0:
            direction = 3
                    
    elif direction == 3:
        x-=1
        if grid[y-1][x]==0:
            direction = 0

    grid[y][x] = index
    #print("x=",x,"y=",y,"number=",index, "direction=",direction)
    fillCount += 1
    index+=1

sumDiag = 0
for i in range(0,size):
    if i==center:
        sumDiag+=grid[center][center]
    else:
        sumDiag+=grid[i][i]
        sumDiag+=grid[i][size-i-1]

print(sumDiag)

            
    

        
