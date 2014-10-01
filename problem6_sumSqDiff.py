def sumSquares(number):
	sum = 0
	for x in range(1, number):
		sum = sum + number * number
	return sum

def squareSum(number):
	sum = 0
	for x in range(1, number):
		sum = sum + number
	return sum * sum

result = squareSum(100) - sumSquares(100)

print result