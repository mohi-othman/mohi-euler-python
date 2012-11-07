#Problem 89
#18 February 2005
#The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

#For example, the following represent all of the legitimate ways of writing the number sixteen:

#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI

#The last example being considered the most efficient, as it uses the least number of numerals.

#The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

#Find the number of characters saved by writing each of these in their minimal form.

#Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.




romanDenominations = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

def romanToDecimal(numeral):
    n = 0
    result = 0
    while True:
        if n==len(numeral):
            break
        for r in romanDenominations:
            if numeral[n:n+len(r[0])] == r[0]:
                result += r[1]
                n+=len(r[0])-1                
                break
        n+=1
    return result

def decimalToRoman(n):
    result = ''    
    for r in romanDenominations:
        if n>=r[1]:
            x = n // r[1]
            result += x * r[0]
            n -= x * r[1]
    return result
        
def solve():
    file = open('Euler089.txt')
    lines = file.readlines()
    numerals = [x.strip() for x in lines]
    savings = 0
    for numeral in numerals:
        decimal = romanToDecimal(numeral)
        reduced = decimalToRoman(decimal)
        savings += len(numeral) - len(reduced)
    return savings
