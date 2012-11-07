number = int(input("Enter the size: "))
half = number//2
length = number + half
for index in range(0, length*number):
    row = index//length
    column = index%length
    getTriangleWidth = lambda level: level * 2 + 1
    triangle1Width = getTriangleWidth(row)
    triangle2Width = getTriangleWidth(number - row - 1)

    if triangle1Width>length: triangle1Width=0
    if triangle2Width>length: triangle2Width=0

    width = max(triangle1Width, triangle2Width)
    center = length // 2

    if (abs(column - center)*2 + 1) <= width:
        print("*", end="")
    else:
        print(" ", end="")

    if column == length-1:
        print("\n", end="")
    
    
