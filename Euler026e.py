cutOff = 1000
size = 1
numbers = list(range(2,cutOff))
maxSize = 0
maxNum = 0

while(True):
    nines = int("9"*size)

    for divisor in numbers:
            
        if nines%divisor==0 and len(str(int(nines/divisor)))==size:
            numbers.remove(divisor)
            print("size: ",size," number: ",divisor)

    size+=1
            

        
