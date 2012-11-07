coins = [1,2,5,10,20,50,100,200]
count = 0

def breakIntoCoins(amount, coin, usedCoins):
    global count
    myAmount = amount
    myUsedCoins = list(usedCoins)
    
    if coin > 0:        
        myAmount -= coin
        myUsedCoins.append(coin)

    if myAmount == 0:
        count+=1
        text = ""
        for c in coins:
            text += str(myUsedCoins.count(c))
            text += " x "
            text += str(c)
            text += "p, "
        print(text[:-2])
    else:
        for newCoin in [c for c in coins if c<=amount and c>=coin]:
            breakIntoCoins(myAmount, newCoin, myUsedCoins)

breakIntoCoins(200,0,[])
print("Final count = ",count)
