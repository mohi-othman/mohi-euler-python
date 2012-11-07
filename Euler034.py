def factorial(number):
    result = 1
    for x in range(2, number+1):
        result*=x

    return result

cutOff = factorial(9)
result = []
for n in range(3,cutOff+1):
    s = 0
    for digit in list(str(n)):
        s += factorial(int(digit))

    if s==n:
        print(s)
        result.append(s)

print(sum(result))
