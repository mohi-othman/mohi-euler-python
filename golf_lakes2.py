a=dict()
def s(n,x,y,R):
 R.add((x,y))
 r=range(-1,2)
 m=set([(x+i,y+j)for i in r for j in r if(i,j)!=(0,0)and(x+i,y+j)not in R])
 z=m-set(a.keys())
 if len(z)>0:return 1
 else:return sum(s(n,k[0],k[1],R)for k in[d for d in m-z if a[(d[0],d[1])]<=n])
i=[list(x)for x in input().strip().split('\n')]
h=len(i)
w=len(i[0])
e=range(0,w)
j=range(0,h)
for c in[(x,y)for x in e for y in j]:a[c]=int(i[c[1]][c[0]])
for y in j:print(''.join([('*',str(a[(x,y)]))[s(a[(x,y)],x,y,set())>0] for x in e]))


