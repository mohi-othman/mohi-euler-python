from decimal import *



def nth_root(num, n, digits):
	getcontext().prec = digits
	a = Decimal(num)
	oneOverN = 1 / Decimal(n)
	nMinusOne = Decimal(n) - 1
	curVal = Decimal(num) / (Decimal(n) ** 2)
	if curVal <= Decimal("1.0"):
		curVal = Decimal("1.1")
	lastVal = 0
	while lastVal != curVal:
		lastVal = curVal
		curVal = oneOverN * ( (nMinusOne * curVal) + (a / (curVal ** nMinusOne)))
	return curVal

