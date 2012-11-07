from functools import *
number = int(input('Enter the desired size: '))
##width = 1
##increment = 2
##for i in range(0,number):
##    if width >= number:        
##        increment = -2
##    spaceCount = number - width + 2
##    print(' '*(spaceCount//2) + '*'*width + ' '*(spaceCount//2))
##    width = width + increment

from functools import *
number = int(input('Enter the desired size: '))

spaceCount = lambda width, number: number - width + 2     
drawLine = lambda width, number: ' '*(spaceCount(width, number)//2) + '*'*width + ' '*(spaceCount(width, number)//2)
widths = list(range(1, number+1, 2))
widths.extend(list(range(max(widths)-2,0,-2)))
lines = map(lambda width: drawLine(width, number),widths)
string = reduce(lambda x,y: x+'\n'+y, lines)

print(string)
