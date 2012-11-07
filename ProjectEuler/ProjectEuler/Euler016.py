def solve():
    number = [2]
    power = 1000
    
    for n in range(1, power):
        result = []
        carryOver = 0
        for digit in number:
            resultDigit = digit * 2 + carryOver
            if resultDigit > 9:
                carryOver = (resultDigit - resultDigit % 10) // 10
                resultDigit = resultDigit % 10                
            else:
                carryOver = 0
            result.append(resultDigit)
        if carryOver > 0:
            result.append(carryOver)
        number = result
    
    return sum(number)




class digit:
    def __init__(self, number):
        self.number = number
        self.next = None

    def addDigit(self, number):
        newDigit = digit(number)
        self.next = newDigit

def solve2():
    number = digit(2)
    power = 1000

    for n in range(1, power):
        carryOver = 0
        pointer = number
        while True:
            pointer.number *= 2
            pointer.number += carryOver
            if pointer.number > 9:
                pointer.number -= 10
                carryOver = 1
            else:
                carryOver = 0
            if pointer.next == None:
                break
            else:
                pointer = pointer.next
        if carryOver > 0:
            pointer.addDigit(carryOver)

    sum = 0
    pointer = number
    while True:
        sum += pointer.number
        if pointer.next == None:
            break
        else:
            pointer = pointer.next
    
    return sum