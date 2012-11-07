import time
#A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, 
#they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

def Solve():
    file = open('Euler079.txt')
    lines = file.readlines()
    nodes = set() #Using set to accept only unique values
    
    #Read from file
    for line in lines:
        if len(line.strip())>0:
            node = line.strip()
            nodes.add(node)
    
    #Get discrete digits and 
    digits = set()
    for node in nodes:
        for index in range(0,len(node)):
            digits.add(node[index])

    #Initiate weighting dict
    weights = dict()
    for digit in digits:
        weights[digit] = set()

    #Go through data 
    for node in nodes:        
        for index in range(1,len(node)):
            digit = node[index]
            for index2 in range(0,index):
                weights[digit].add(node[index2])
                
    result = ''
    first = [x for x in weights if len(weights[x])==0]
    result += first[0]
    previous = set(first)
    for index in range(1, len(digits)):
        candidates = [x for x in weights if x not in previous and len(previous.intersection(weights[x])) >= 0]        
        candidates.sort(key = lambda x: len(weights[x]))
        result += candidates[0]
        previous.add(candidates[0])

    return result
            





def twoLetterLeft(str):
    return str[:2]

def oneLetterLeft(str):
    return str[:1]

def twoLetterRight(str):
    return str[-2:]

def oneLetterRight(str):
    return str[-1:]








    