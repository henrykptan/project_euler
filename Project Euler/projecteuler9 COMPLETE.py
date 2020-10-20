'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def tripletTest(a,b,c) :
	if a**2 + b**2 == c**2:
		return True
	else:
		return False 

n = 1000

for i in range(1, n):
	for j in range (i+1, n):
		k = n - i - j
		if tripletTest(i, j, k):
			print(i,j,k)
			print(i*j*k)
			break
        



