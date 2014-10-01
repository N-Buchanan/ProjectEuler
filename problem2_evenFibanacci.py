sum = 0
fibOne = 0
fibTwo = 1

while fibTwo < 40:
	if fibTwo % 2 == 0:
		sum = sum + fibTwo
	temp = fibTwo
	print temp
	fibTwo = fibTwo + fibOne
	fibOne = temp

print sum