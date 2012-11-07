upperlimit = 1000
sum = 0
for num in range(0,upperlimit):
    if num%3 == 0 or num%5 == 0:
        sum += num

    
print (sum)
