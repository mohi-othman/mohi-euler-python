import math

maxP = 0
maxResults = []
for p in range(3,1000):
    results = []
    cutOff = math.floor(math.sqrt(2*((p//3)**2)))
    for x in range(1,cutOff):
        for y in range(1,cutOff):
            z = math.sqrt(x**2+y**2)
            if int(z)==z and x+y+z == p:
                results.append((x,y,z))
            if x+y+z > p:
                break
            
                

    if len(results)>len(maxResults):
        maxResults = results
        maxP = p
        print(p, len(maxResults))

print(maxP, len(maxResults))
