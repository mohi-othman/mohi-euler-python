a=0
b=1
cutOff = 1000
index = 1
while(True):
    a, b = b, a + b
    index+=1
    if len(str(b)) == cutOff:
        break

print(b)
print(index)
    
