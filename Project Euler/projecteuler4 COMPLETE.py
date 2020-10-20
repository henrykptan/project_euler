'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time
start = time.time()

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def largest_palin_prod(min, max):
	''' We test every product of i and j in the range (99,999), then save if it's higher than the current
	'''
	max_ans = 0 
	for i in range(min, max):
		for j in range(i, max):
			if i*j > max_ans and is_palindrome(i*j):
				max_ans = i*j
	return max_ans

print("ans is {} found in time {}".format(largest_palin_prod(99, 999), time.time()-start))
