import urllib.request
import math

def getNumber(text):
    num = ''
    for x in range(1, len(text)+1):
        letter = text[-x]
        if letter in "0123456789":
            num =letter+num
        else:
            break

    return int(num)

num = 92118#53522#50010#12345
allNumebrs = [num]
index = 0
while(True):
    index+=1
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(num)
    print(url)

    page = urllib.request.urlopen(url)
    
    text = page.read().decode("utf8")
    if num == 92118:
        num = num//2
    else:
        if text.find("and the next nothing is")!=0:
            print(text)
            break
    
        result = getNumber(text)

        if len("and the next nothing is ")+len(str(result)) != len(text):
            print(text)
            break
    
        if result>0: # and result not in allNumebrs: #and index<410:
            num = result
            allNumebrs.append(num)
            print(index)
            print(text)
        else:
            print(text)
            break
