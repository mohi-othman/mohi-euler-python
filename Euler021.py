def d(n):
    s=0
    for f in range(2,n):
        if not n%f:
            s+=(f+n/f)/2
    return int(s)+1
a=0
for n in range(10000):
    x=d(n)
    if n!=x and n==d(x):
       a+=(n+x)/2
print(a)
    
    
