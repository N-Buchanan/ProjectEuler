MIN_DIVISORS =500
sum = 1

def countDivisors(number):
	divisorsCount = 0
	for i in range(1,number/2):
		if number % i == 0:
			divisorsCount = divisorsCount + 1
	if divisorsCount > MIN_DIVISORS:
		return True
	return False

n = 1

while not countDivisors(sum):
	n = n + 1
	sum = sum + n

print sum