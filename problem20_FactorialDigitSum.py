product = 1
for i in range(1, 100):
	product = product * i

myStr = str(product)

sum = 0

for i in myStr:
	sum = sum + int(i)

print sum