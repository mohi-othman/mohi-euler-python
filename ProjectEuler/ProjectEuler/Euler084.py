#03 December 2004

#In the game, Monopoly, the standard board is set up in the following way:

#   GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
#   H2	 	                                C1
#   T2	 	                                U1
#   H1	 	                                C2
#   CH3	 	                                C3
#   R4	 	                                R2
#   G3	 	                                D1
#   CC3	 	                                CC2
#   G2	 	                                D2
#   G1	 	                                D3
#   G2J F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

#A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

#In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

#At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

#Community Chest (2/16 cards):
#Advance to GO
#Go to JAIL
#Chance (10/16 cards):
#Advance to GO
#Go to JAIL
#Go to C1
#Go to E3
#Go to H2
#Go to R1
#Go to next R (railway company)
#Go to next R
#Go to next U (utility company)
#Go back 3 squares.
#The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

#By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

#Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

#If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
###################################################################################################

import random 

def getSquareNames():
    file = open('Euler084.txt')
    lines = file.readlines()
    result = []
    for square in [x for x in lines[0].strip().replace('\t',' ').split(' ') if x.strip() !='']:
        result.append(square)

    for i in range(1, len(lines)-1):
        result.append([x for x in lines[i].strip().replace('\t',' ').split(' ') if x.strip() !=''][1])

    bottom = [x for x in lines[len(lines)-1].strip().replace('\t',' ').split(' ') if x.strip() !='']
    bottom.reverse()
    for square in bottom:
        result.append(square)

    for i in range(len(lines)-2, 0, -1):
        result.append([x for x in lines[i].strip().replace('\t',' ').split(' ') if x.strip() !=''][0])

    return result

class square:
    def __init__(self, name):
        self.name = name
        self.visits = 0

class standardBoard():
    def __init__(self):
        self.squares = []
        for name in getSquareNames():
            self.squares.append(square(name))
        
        self.chanceCards = list(range(1,17))
        self.communityChestCards = list(range(1,17))

        random.shuffle(self.chanceCards)
        random.shuffle(self.communityChestCards)

    def indexOf(self, squareName):
        square = [x for x in self.squares if x.name == squareName][0]
        return self.squares.index(square)

    def size(self):
        return len(self.squares)
    
    def __applyMovement(self, location, steps):
        location += steps
        location = location % self.size()
        return location

    def moveBySteps(self, location, steps):
        location = self.__applyMovement(location, steps)
        return self.__resolveSquare(location)

    def moveTo(self, squareName):        
        location = self.indexOf(squareName)                      
        return self.__resolveSquare(location)

    def __resolveSquare(self, location):
        done = False
        while not done:
            if self.squares[location].name[:2] == 'CC':
                newLocation = self.applyCommunityChest(location)
                if newLocation==location:
                    done = True                
                location = newLocation
            elif self.squares[location].name[:2] == 'CH':
                newLocation = self.applyChance(location)
                if newLocation==location:
                    done = True
                location = newLocation
            elif self.squares[location].name == 'G2J':
                location = self.indexOf('JAIL')
                done = True
            else:
                done = True
        
        self.squares[location].visits += 1

        return location

    def applyCommunityChest(self, location):
        card = self.communityChestCards[0]
        
        self.communityChestCards.remove(card)

        if card == 1:
            location = self.moveTo('GO')
        elif card == 2:
            location = self.moveTo('JAIL')
        else:
            pass

        self.communityChestCards.append(card)

        return location

    def applyChance(self, location):
        card = self.chanceCards[0]

        self.chanceCards.remove(card)

        if card==1:
            location = self.moveTo('GO')
        elif card==2:
            location = self.moveTo('JAIL')
        elif card==3:
            location = self.moveTo('C1')
        elif card==4:
            location = self.moveTo('E3')
        elif card==5:
            location = self.moveTo('H2')
        elif card==6:
            location = self.moveTo('R1')
        elif card==7 or card==8:
            location = self.__applyMovement(location,1)            
            while self.squares[location].name[:1] != 'R':
                location = self.__applyMovement(location,1)                    
            
            location = self.__resolveSquare(location)

        elif card==9:
            location = self.__applyMovement(location,1)            
            while self.squares[location].name[:1] != 'U':
                location = self.__applyMovement(location,1)                    

            location = self.__resolveSquare(location)

        elif card==10:
            location = self.moveBySteps(location,-3)            
        else:
            pass
        
        self.chanceCards.append(card)

        return location

def isDoubleThrow(throw):
    isDouble = True
    for i in range(0, len(throw)-1):
        if throw[i]!=throw[i+1]:
            isDouble = False
            break
    return isDouble

def solve():
    random.seed()

    board = standardBoard()
    dice = [4,4]    # two four sided dice
    dice = [6,6]    # two six sided dice
    jailLimit = 3   # number of doubles that lands you in jail
    iterations = 20000000
    location = 0
    doubles = 0

    for i in range(0, iterations):        
        throw = [random.randrange(1,die+1) for die in dice]            
        isDouble = isDoubleThrow(throw)                  
        
        if isDouble:
            doubles += 1            
        else:
            doubles = 0                  
                        
        if doubles == jailLimit:
            doubles = 0
            location = board.moveTo('JAIL')            
        else:
            location = board.moveBySteps(location, sum(throw))
        
    
    sortedSquares = sorted(board.squares, key=lambda x:x.visits, reverse=True)

    for sq in sortedSquares:
        print(sq.name, sq.visits)
    
    result = ''
    for i in range(0,3):
        result+=format(board.indexOf(sortedSquares[i].name),'02d')
    return result

    





