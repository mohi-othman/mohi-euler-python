class SudokuCell:
    def __init__(self):
        self.Value = None
        self.Candidates = [x for x in range(1,10)]

    def Solve(self, value):
        self.Value = value
        self.Candidates = list()

    def RemoveCandidate(self, value):
        if value in self.Candidates:
            self.Candidates.remove(value)
            if len(self.Candidates)==1:
                self.Solve(self.Candidates[0])

class SudokuSquare:
    def __init__(self):
        self.Cells = dict()
        for x in range(0,3):
            for y in range(0,3):
                self.Cells[(x,y)] = None    

    def CellsAsList(self):
        return [self.Cells[key] for key in self.Cells.keys()]

    def IsValid(self):
        checkSet = set()
        success = True
        for cell in self.CellsAsList():
            if cell.Value != None:
                if cell.Value not in checkSet:
                    checkSet.add(cell.Value)
                else:
                    success = False
                    break
        return success

    def Solve(self):
        success = False
        for current in self.CellsAsList():
            other = [cell.Value for cell in self.CellsAsList() if cell != current]
            for n in other:
                if n in current.Candidates:
                    success = True
                    current.RemoveCandidate(n)
        return success

class SudokuLine:
    def __init__(self):
        self.Cells = list()
        

    def IsValid(self):
        checkSet = set()
        success = True
        for cell in self.Cells:
            if cell.Value != None:
                if cell.Value not in checkSet:
                    checkSet.add(cell.Value)
                else:
                    success = False
                    break
        return success

    def Solve(self):
        success = False
        for current in self.Cells:
            other = [cell.Value for cell in self.Cells if cell != current]
            for n in other:
                if n in current.Candidates:
                    success = True
                    current.RemoveCandidate(n)
        return success

class SudokuBoard:
    def __init__(self,Name):
        self.Name = Name.replace("\n","")
        self.Cells = dict()
        for x in range(0,9):
            for y in range(0,9):
                self.Cells[(x,y)] = SudokuCell()
        # Setup Squares
        self.Squares = dict()
        for x in range(0,3):
            for y in range(0,3):
                square = SudokuSquare()
                for subX in range(0,3):
                    for subY in range(0,3):
                        square.Cells[(subX,subY)] = self.Cells[(x * 3 + subX, y * 3 + subY)]
                self.Squares[(x,y)] = square
        # Setup Lines
        self.Lines = list()
        for row in range(0,9):
            newRow = SudokuLine()
            for x in range(0,9):
                newRow.Cells.append(self.Cells[(x,row)])
            self.Lines.append(newRow)
        for column in range(0,9):
            newColumn= SudokuLine()
            for y in range(0,9):
                newColumn.Cells.append(self.Cells[(column,y)])
            self.Lines.append(newColumn)

    def Key(self):
        return int(str(self.Cells[(0,0)].Value)+str(self.Cells[(1,0)].Value)+str(self.Cells[(2,0)].Value))

    def Populate(self,textLines):
        y = 0
        for line in textLines:
            if len(line)>=9:                
                for x in range(0,9):
                    if line[x] != "0":
                        self.Cells[(x,y)].Solve(int(line[x]))
                y+=1

    def CellsAsList(self):
        return [self.Cells[key] for key in self.Cells.keys()]

    def IsValid(self):
        sets = list()
        sets.extend([self.Squares[key] for key in self.Squares.keys()])
        sets.extend(self.Lines)
        success = True
        for s in sets:
            if not s.IsValid:
                success = False
                break
        return success

    def IsSolved(self):
        success = True
        for cell in self.CellsAsList():
            if cell.Value == None:
                success = False
                break
        return success

    def Solve(self):
        sets = list()
        sets.extend([self.Squares[key] for key in self.Squares.keys()])
        sets.extend(self.Lines)
        flag = False
        while True:
            for s in sets:
                flag = flag or s.Solve()
            if not flag or self.IsSolved():
                break
            else:
                flag = False

    def __str__(self):
        result = ""
        for y in range(0,9):            
            for x in range(0,9):
                c = self.Cells[(x,y)]
                if c.Value == None:
                    result+="0"
                else:
                    result+=str(c.Value)
            result+="\n"
        return result
    
    def Copy(self):
        copy = SudokuBoard(self.Name)
        lines = str(self).split("\n")
        copy.Populate(lines)
        return copy


