maximum = 1
maximumSequence = 1


def collatzNum(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + collatzNum(n/2)
	else:
		return 1 + collatzNum(3*n + 1)

for i in range(1,1000000):
	n = collatzNum(i)
	if n > maximumSequence:
		maximumSequence = n
		maximum = i

print maximum