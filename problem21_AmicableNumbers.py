MAX = 10000
total = 0

numbers = range(2,MAX)

def findDivisorsSum(num):
	sum = 0
	if num == 2:
		return 1
	for i in range(1,num/2 + 1):
		if num % i == 0:
			sum = sum + i
	return sum

for i in numbers:
	divisorsSum = findDivisorsSum(i)
	#print numbers[i], divisorsSum
	if divisorsSum < 10000 and i == findDivisorsSum(divisorsSum) and not i == divisorsSum:
		total = total + i

print total