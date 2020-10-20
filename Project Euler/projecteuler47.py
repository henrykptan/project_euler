'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

import math

def get_primes_less_than(n):
	is_prime = get_seive(n)
	primes = [2]
	for i in range(3, n, 2):
		if is_prime[i]:
			primes.append(i)
	return primes

def get_composites_less_than(n):
	is_prime = get_seive(n)
	composites = [1]
	for i in range(2, n):
		if not is_prime[i]:
			composites.append(i)
	return composites

def get_seive(n):
	is_prime = [True]*n
	is_prime[0] = False 
	is_prime[1] = False
	is_prime[2] = True
	for i in range(4, n, 2):
		is_prime[i] = False

	for i in range(3, int(n**0.5+1), 2):
		index = i*2 
		while index < n:
			is_prime[index] = False
			index +=i 
	return is_prime
    
def get_prime_factors(n, prime_list):
	prime_limit = n/2	
	index = 0
	factors_list = []
	while prime_list[index] <= prime_limit:
		prime = prime_list[index]
		while n% prime == 0:
			n = n / prime
			factors_list.append(prime)
		index += 1
	return factors_list

def have_four_distinct_prime_factors(a, b, c, d, prime_list):
	a_prime_factors = get_distinct_prime_factors(a, prime_list)
	if (len(a_prime_factors) == 4):
		b_prime_factors = get_distinct_prime_factors(b, prime_list)
		if (len(b_prime_factors) == 4):
			c_prime_factors = get_distinct_prime_factors(c, prime_list)
			if (len(c_prime_factors) == 4):
				d_prime_factors = get_distinct_prime_factors(d, prime_list)
				if (len(d_prime_factors) == 4):
					return True

def get_distinct_prime_factors(n, prime_list):
	return list(set(get_prime_factors(n, prime_list)))

def are_four_consecutive_numbers(a, b, c, d):
	return (b == a + 1) & (c == b + 1) & (d == c + 1)


if (__name__ == "__main__"):

	primes = get_primes_less_than(10000000)

	composites = get_composites_less_than(10000000)

	index = 0
	while True:
		a = composites[index]
		b = composites[index+1]
		c = composites[index+2]
		d = composites[index+3]
		if are_four_consecutive_numbers(a, b, c, d):
			if have_four_distinct_prime_factors(a, b, c, d, primes):
				print(a, b, c, d)
				break
		index = index + 1

