def isEvenMultiple(number):
	for x in range(1, 20):
		if number % x != 0:
			return False
	return True

num = 2520

while not isEvenMultiple(num):
	num = num + 20

print num