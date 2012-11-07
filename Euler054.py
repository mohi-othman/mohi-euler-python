import time

valueRank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
fullHouse = ['K','Q','J','T','A']
fullHouse.sort()

class HandRank:
    RoyalFlush = 10
    StraightFlush = 9
    FourOfAKind = 8
    FullHouse = 7
    Flush = 6
    Straight = 5
    ThreeOfAKind = 4
    TwoPairs = 3
    OnePair = 2
    HighCard = 1

class Hand:
    def __init__(self, HandRank, WinningCards, RemainingCards):
        self.HandRank = HandRank
        self.WinningCards = WinningCards
        self.RemainingCards = RemainingCards
        
def stripValues(hand):
    return [card[0] for card in hand]

def stripSuits(hand):
    return [card[1] for card in hand]

def isSingleSuit(suits):
    return len(set(suits)) == 1

def numerateValues(values):
    return [valueRank.index(x)+1 for x in values]

def detectSequence(numbers):    
    numbers.sort()
    flag = True
    for index in range(0,4):
        if numbers[index] != numbers[index+1]-1:
            flag = False
            break    
    
    return flag

def detectStraight(values):
    numbers = numerateValues(values)
    result = detectSequence(numbers)
    if not result and 'A' in values:
        numbers.remove(valueRank.index('A')+1)
        numbers.insert(0,0)
        result = detectSequence(numbers)

    return result

def countRepeats(values):
    result = dict()
    for v in valueRank:
        count = values.count(v)
        if count > 1:
            result[v] = count

    return result

def sortValuesHighToLow(values):
    valueCard = [(valueRank.index(x), x) for x in values]
    valueCard.sort()
    valueCard.reverse()
    return [v[1] for v in valueCard]

def getStraightHighCard(values):
    
    if 'A' in values and 'K' not in values:
        return '5'
    else:
        return valueRank[max(numerateValues(values))-1]
    
def evaluateHand(hand):
    values = stripValues(hand)
    suits = stripSuits(hand)

    hand.sort()
    values.sort()
    suits.sort()
    
    myHand = Hand(HandRank.HighCard, [], sortValuesHighToLow(values))
    repeatDict = countRepeats(values)
    repeatCards = list(repeatDict.keys())
    repeatCount = [repeatDict[x] for x in repeatCards]

    #Check RoyalFlush
    if fullHouse == values: 
        myHand.HandRank = HandRank.RoyalFlush
        myHand.WinningCards = values
        myHand.RemainingCards = []
    #Check StraightFlush
    elif isSingleSuit(suits) and detectStraight(values): 
        myHand.HandRank = HandRank.StraightFlush
        myHand.WinningCards = [getStraightHighCard(values)]
        myHand.RemainingCards = []
    #Check FourOfAKind
    elif repeatCount.count(4) > 0: 
        myHand.HandRank = HandRank.FourOfAKind
        myHand.WinningCards = [repeatCards[0]]
        myHand.RemainingCards = [v for v in values if v != repeatCards[0]]
    #Check FullHouse
    elif repeatCount.count(3) > 0 and repeatCount.count(2) > 0: 
        myHand.HandRank = HandRank.FullHouse
        myHand.WinningCards = [v for v in values if v in repeatDict and repeatDict[v]==3]
        myHand.WinningCards.extend([v for v in values if v in repeatDict and repeatDict[v]==2])
        myHand.RemainingCards = []
    #Check Flush
    elif isSingleSuit(suits):
        myHand.HandRank = HandRank.Flush
        myHand.WinningCards = [sortValuesHighToLow(values)]
        myHand.RemainingCards = []
    #Check Straight
    elif detectStraight(values):
        myHand.HandRank = HandRank.Straight
        myHand.WinningCards = [getStraightHighCard(values)]
        myHand.RemainingCards = []
    #Check ThreeOfAKind
    elif repeatCount.count(3) > 0:
        myHand.HandRank = HandRank.ThreeOfAKind
        myHand.WinningCards = [v for v in values if v in repeatDict and repeatDict[v]==3]
        myHand.RemainingCards = sortValuesHighToLow([v for v in values if v not in myHand.WinningCards])
    #Check TwoPairs
    elif repeatCount.count(2) == 2:
        myHand.HandRank = HandRank.TwoPairs
        myHand.WinningCards = [v for v in values if v in repeatDict and repeatDict[v]==2]
        myHand.RemainingCards = sortValuesHighToLow([v for v in values if v not in myHand.WinningCards])
    #Check OnePair
    elif repeatCount.count(2) == 1:
        myHand.HandRank = HandRank.OnePair
        myHand.WinningCards = [v for v in values if v in repeatDict and repeatDict[v]==2]
        myHand.RemainingCards = sortValuesHighToLow([v for v in values if v not in myHand.WinningCards])

    return myHand
    
def doesPlayerOneWin(handOne, handTwo):
    handOneEval = evaluateHand(handOne)
    handTwoEval = evaluateHand(handTwo)

    if handOneEval.HandRank > handTwoEval.HandRank:
        return True
    elif handTwoEval.HandRank > handOneEval.HandRank:
        return False

    winOne = handOneEval.WinningCards
    winTwo = handTwoEval.WinningCards

    for i in range(0, len(winOne)):
        if valueRank.index(winOne[i]) > valueRank.index(winTwo[i]):
            return True
        elif valueRank.index(winTwo[i]) > valueRank.index(winOne[i]):
            return False
        
    remainOne = handOneEval.RemainingCards
    remainTwo = handTwoEval.RemainingCards

    for i in range(0, len(remainOne)):
        if valueRank.index(remainOne[i]) > valueRank.index(remainTwo[i]):
            return True
        elif valueRank.index(remainTwo[i]) > valueRank.index(remainOne[i]):
            return False

    return False
    
def solve():
    t = time.clock()
    count = 0
    file = open('Euler054.txt')
    lines = file.readlines()
    for line in lines:
        cards = line.split(" ")
        cards = [x.strip() for x in cards]
        one = cards[:5]
        two = cards[-5:]
        print(one,two,doesPlayerOneWin(one,two))
        if doesPlayerOneWin(one,two):
            count+=1
            

    print('Player one wins',count,'times')
    print(time.clock() - t)

solve()
