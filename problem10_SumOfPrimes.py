r = range(2000001)
numbers = r[1::2]
sum = 1
def isPrime(n):
	for i in range(2,n/2):
		if n % i == 0:
			return False
	return True

for i in numbers:
	if isPrime(i):
		sum = sum + i
		print i

print sum