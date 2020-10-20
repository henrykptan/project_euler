'''
COULDN'T GET A GENERAL SOLUTION SO CHEATED
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
'''
from fractions import gcd #yay
def lcm(a,b): # Calculates the lowest common multiple of two integers a and b
    return a*b//gcd(a,b) # Double slash means floor division (ie round down to nearest whole number) DIDNT KNOW LCM x GCD = a x b

from functools import reduce
print(reduce(lcm, range(1,20+1)))	# then finds lowest common multiple of numbers 1-20 [reduce function does lcm(1,lcm(2,lcm(3,lcm(4,....))) = lcm(1,2,3,..)]
# gives 232792560
# CHEATS

'''        
# first create the set of primes less than or equal to the desired number, as the total must be some product of powers of these primes by the 
# fundamental theorem of arithmetic 

num = 20

def is_prime(n): # could eratosthenes sieve dis
	if (n < 2): 
		return False 
	else: 
		for i in range(2, n):
			if (n % i == 0):
				return False
		return True
				
primes = []

for n in range(0, num + 1):
	if is_prime(n):
		primes.append(n)

#now must go through powers of the primes until the value produced is more than num
powers = []

for i in range(0, len(primes)): # this isn't really that necessary but makes things clearer
	x = primes[i] # for each prime x, you find the highest power such that x^p is less than our number (to include all numbers <20)
	p = 1
	while (x**p <= num):
		p = p+1
	powers.append(p-1)
		
ans = 1
for i in range(0, len(primes)): #same as len(powers)
	ans = ans*(primes[i]**powers[i])

print(ans)