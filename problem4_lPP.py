modulo = [100000, 10000, 1000, 100, 10, 1]

def is_palindrome(num):
	modulo1 = []
	modulo2 = []
	for a in modulo:
		if num >= a:
			modulo1.insert(len(modulo1), a)#s = modulo1 + [a]
			modulo2.insert(0, a)

	#print "num %d" % num
	#print modulo1
	#print modulo2
	for n in range(0, len(modulo1)):
		if num / modulo1[n] != num / modulo2[n]:
			return False

	return True

for x in range(999, 100, -1):
	for y in range(999, 100, -1):
		product = x * y
		if is_palindrome(product):
			print product
		
