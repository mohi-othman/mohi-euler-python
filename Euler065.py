import time



def add(integer,fraction):
    if fraction == (0,0): return (integer,1)
    newFraction=(integer * fraction[1], fraction[1])
    return (newFraction[0]+fraction[0],fraction[1])

def flip(fraction):
    return (fraction[1],fraction[0])

def solve(cutOff):
    e = [2]
    for n in range(1,cutOff//3+1):
        e.append(1)
        e.append(2*n)
        e.append(1)    
    u = e[:cutOff]
    u.reverse()
    past = (0,0)
    for member in u:
        past=flip(past)
        past=add(member,past)

    return past

print('***********')
x=solve(100)
print(x)
print(sum([int(x) for x in list(str(x[0]))]))


    

