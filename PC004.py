import re

file = open('PC004.txt')
text = ''.join(file.readlines())
result = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]",text)
for x in result:
    print(x)
