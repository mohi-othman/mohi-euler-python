import time

onesSpelling=dict()
onesSpelling[1]="one"
onesSpelling[2]="two"
onesSpelling[3]="three"
onesSpelling[4]="four"
onesSpelling[5]="five"
onesSpelling[6]="six"
onesSpelling[7]="seven"
onesSpelling[8]="eight"
onesSpelling[9]="nine"

teenSpelling=dict()
teenSpelling[10]="ten"
teenSpelling[11]="eleven"
teenSpelling[12]="twelve"
teenSpelling[13]="thirteen"
teenSpelling[14]="fourteen"
teenSpelling[15]="fifteen"
teenSpelling[16]="sixteen"
teenSpelling[17]="seventeen"
teenSpelling[18]="eighteen"
teenSpelling[19]="nineteen"

tensSpelling=dict()
tensSpelling[2]="twenty"
tensSpelling[3]="thirty"
tensSpelling[4]="forty"
tensSpelling[5]="fifty"
tensSpelling[6]="sixty"
tensSpelling[7]="seventy"
tensSpelling[8]="eighty"
tensSpelling[9]="ninety"

def parseNumber(number):
    result = ""
    numStr = str(number)
    if number>=1000000:
        result = parseNumber(int(numStr[:len(numStr)-6])) + " million " + parseNumber(int(numStr[-6:]))
    elif number>=1000:
        result = parseNumber(int(numStr[:len(numStr)-3])) + " thousand " + parseNumber(int(numStr[-3:]))
    elif number>=100:
        result = parseNumber(int(numStr[0])) + " hundred" 
        if  int(numStr[-2:]) > 0:
            result += " and " + parseNumber(int(numStr[-2:]))
    elif number>=20:
        result = tensSpelling[int(numStr[0])] 
        if int(numStr[1])>0:
            result += " "+ parseNumber(int(numStr[1]))
    elif number>=10:
        result = teenSpelling[int(number)]
    elif number>0:
        result = onesSpelling[int(number)]

    return result

sumVal = 0
cutOff = 1000
for i in range(1,cutOff + 1):
    text = parseNumber(i)
    print(text)
    sumVal += len(text.replace(" ",""))

print(sumVal)

