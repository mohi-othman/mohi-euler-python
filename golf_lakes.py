f=input().split("\n")
a=[list(x) for x in f]
t=''.join(f)
h=len(a)    
w=len(a[0])
def s(n,x,y,r):    
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i!=0 and j!=0) and 0<x+i<w and 0<y+j<h and (x+i, y+j) not in r and int(t[(y+j)*w+x+i])<=n :
                    r.add((x+i, y+j))
                    s(n, x+i,y+j, r)  
for i in range(0,len(t)):                
        x=i-((i//w)*w)
        y=i//w                
        z={(x,y)}
        s(int(t[i]),x,y,z)        
        f = 1
        for x in z:
            if x[0]<1 or x[0]>w-1 or x[1]<1 or x[1]==h-1:            
                f=0                
        if f:
            for x in z:
                a[x[1]][x[0]]='*'         

for i in a:print(''.join(i))

        




        
