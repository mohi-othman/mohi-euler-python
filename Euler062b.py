import time

t = time.clock()

roof = 10000
target = 5

cubes = [x**3 for x in range(1,roof+1)]
digits = [list(str(x)) for x in cubes]

for d in digits:
    d.sort()

result = [x for x in digits if digits.count(x)==target]

if len(result)==0:
    print('fail')
else:
    print(cubes[digits.index(result[0])])

print(time.clock() - t)
