s=0
for a in range(1,10000):
    b = sum([i for i in range(1,a) if (a%i == 0)])
    c = sum([i for i in range(1,b) if (b%i == 0)])
    if(c == a and c != b): s=+a
print(s)
