'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
def factorial(n):
	if n == 0:
		return 1
	if n>=1: 
		return n*factorial(n-1)	


def factorial_sum(n):
	N = str(n)
	total = 0
	for i in range(0, len(N)):
		total += factorial(int(N[i]))
	return(total)	

sum = 0
for n in range(3, 1000000):
	if factorial_sum(n) == n:
		sum += n
		print(n)
print(sum)