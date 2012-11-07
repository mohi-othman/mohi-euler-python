count = 0

def breakIntoCoins(amount, coin, usedCoins):
    return breakIntoSmallerBits(amount, coin, usedCoins, [1,2,5,10,20,50,100,200])

def breakIntoSmallerBits(amount, coin, usedCoins, smallerBits):        
    global count
    myAmount = amount
    myUsedCoins = list(usedCoins)
    
    if coin > 0:        
        myAmount -= coin
        myUsedCoins.append(coin)

    if myAmount == 0:
        count+=1        
    else:
        for newCoin in [c for c in smallerBits if c<=amount and c>=coin]:
            breakIntoSmallerBits(myAmount, newCoin, myUsedCoins, smallerBits)
    
    return count

def countBreaks(amount, smallerBits):
    global count 
    count = 0
    breakIntoSmallerBits(amount,0,[],smallerBits)
    return count

#count = breakIntoCoins(200,0,[])
#print("Final count = ",count)
