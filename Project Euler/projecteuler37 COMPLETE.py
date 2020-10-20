'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def is_prime(n):
	if (n < 2):
		return False
	else:
		for i in range(2, int(n**(1/2))+1):
			if (n%i == 0):
				return False
	return True

def trucatable_prime(n): # not sure on the issue with the Booleans, at the end always return true then if there is a single false 
	if (n < 10):
		return False
	N = str(n)
	# first: left to right truncatable	
	for i in range(0, len(N)):
		if not is_prime(int(N[i:])):
			return False	
	# then: right to left truncatable
	for j in range(1, len(N)+1):
		if not is_prime(int(N[:j])):
			return False
	return True

count = 0
ans = 0
for n in range(0,10000):
	if trucatable_prime(n):
		print(n)
		count += 1
		ans += n

print('The total sum is {x}'.format(x = ans))	

