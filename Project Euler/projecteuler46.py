'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import time

start = time.time()

def sieve(n):
    is_prime = [True]*n  # create an list of n trues
    is_prime[0] = False 
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated (when we generate)
    for i in range(3, int(n**0.5+1), 2): # so we check the odds 
        index = i*2 
        while index < n: # we now go through every prime up to sqrt(n)+1, and remove its multiples 
            is_prime[index] = False
            index = index+i 
    primes = [2]
    for i in range(3, n, 2): # we then generate our set of primes (note no need to check evens after 2)
        if is_prime[i]:
            primes.append(i)
    return primes

total = 1000

primes = sieve(total)    

squares = []
j = 1
while j**2<total:
	squares.append(j**2)
	j+=1

composite_odds = []
k = 1
while k <= total:
	composite_odds.append(k)
	k+=2
for x in composite_odds:
	if x in primes:
		composite_odds.remove(x)	

possibles = []
for i in primes:
	for j in squares:
		if (i + 2*j) not in possibles:
			possibles.append(i+2*j)

for i in possibles:
	if i in composite_odds:
		composite_odds.remove(i)
Goldbach_counter = composite_odds

print("Goldbach counterexample = {}, found in time {}, )