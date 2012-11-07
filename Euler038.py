maxFound = 123456789
startPoint = 9999
p = startPoint
while(True):
    product = str(p)
    if p<int(str(maxFound)[:len(product)]):
        break

    print(p)
    
    n = 2    
    while(len(str(n*p))+len(product)<10):
        product += str(n*p)

        if '0' in product:
            break

        if int(product)<int(str(maxFound)[:len(product)]):
            break

        if len(product) == 9 and int(product)>maxFound and len(set(list(product))) == 9:
            maxFound = int(product)
            print(maxFound, p, n)
        else:
            break

    p-=1

print(maxFound)
            
        
