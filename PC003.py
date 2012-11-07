file = open('PC003.txt')
lines = file.readlines()
characDict=dict()

for line in lines:
    for c in line:
        if c in characDict:
            characDict[c]+=1
        else:
            characDict[c]=1

print(characDict)
            
