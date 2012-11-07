def Eratosthenes(roof):
    candidates = [x for x in range(2, roof)]
    strikeOut = {x: False for x in candidates}
   
    while True:
        p = min(candidates)
        if p**2 > roof:
            break
        m = 2
        x = p*m
        while x<roof:
            strikeOut[x] = True
            m+=1
            x= p*m
       
        candidates = [x for x in candidates[1:] if not strikeOut[x]]
       
    return [x for x in strikeOut.keys() if not strikeOut[x]]

primes = Eratosthenes(5000)

print(primes)
