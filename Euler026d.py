cutOff = 10

size = 1
maxSize = 0
result = 0
while(size < 5):
    n = int("9"*size)
    d = int("1" + ("0"*(size-1)))
    r = n / d

    if r > cutOff:
        break
    if r==int(r):
        maxSize = max(maxSize,size)

    print(n, d, r, size)
    size+=1

print(maxSize)
        
