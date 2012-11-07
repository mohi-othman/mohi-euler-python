number = int(input("Enter the size: "))

half = number//2
length = number + half
center = length // 2

getTriangleWidth1 = lambda row: row * 2 + 1 if row<=(length-1)/2 else 0
getTriangleWidth2 = lambda row: getTriangleWidth1(number-row-1)
getTriangleWidthMax = lambda row: max(getTriangleWidth1(row), getTriangleWidth2(row))
isStar = lambda x,y: '*' if abs(x - center)*2 + 1 <= getTriangleWidthMax(y) else ' '
isRowEnd = lambda x: '\n' if x==length-1 else ''
string = [isStar(index%length,index//length) + isRowEnd(index%length) for index in range(0, length*number)]

print(''.join(string))
