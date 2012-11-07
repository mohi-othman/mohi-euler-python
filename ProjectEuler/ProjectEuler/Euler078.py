#http://pastebin.com/xpvYQept
#Uses Pentagonal Number Theorem
# http://en.wikipedia.org/wiki/Pentagonal_number_theorem
# http://blog.dreamshire.com/2009/04/19/project-euler-problem-78-solution/

def Solve(divisor):    
    q = []    
    for i in range(1,500):        
        x = i
        q.append(int(x*(3*x - 1)/2))
        x = -i
        q.append(int(x*(3*x - 1)/2))
    
    q.sort()

    n = 1
    P = [1]       
    r = 0
    while True:
        i = 0
        f = -1 
        r = 0
        while q[i]<=n:
            if i%2==0: f = -f
            r+= f * P[n-q[i]]
            i+=1
        P.append(r)
        if r % divisor == 0:
            break
        n+=1

    return (n,r)
        
