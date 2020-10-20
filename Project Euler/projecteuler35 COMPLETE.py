'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def isPrime(n):
    if n < 2: return False	 # not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 

# all(interable) will return true if all elements of the iterable are True, else False (also any(iterable))

def circular_test(n):
	N = str(n)
	A = [] #we create a string and then a list of the digits in the prime
	for i in range(0, len(N)):
		A.append(N[i])
	if all(isPrime(int("".join([A[i - j] for i in range(len(A))]))) for j in range(len(A))): # all('some condition' for i in range), "".join(array) makes a string 
			return True
	return False		
		
#Sieving to create a list of primes as our iterable makes things a bit quicker

def sieve(n):
	is_primes = [True]*n
	is_primes[0] = False
	is_primes[1] = False
	is_primes[2] = True
	for i in range(3, int(n**(1/2)+1), 2):
		index = 2*i
		while index < n:
			is_primes[index] = False
			index += i
	primes = [2]
	for i in range(3, n, 2): 
		if is_primes[i] == True:
			primes.append(i)
	return primes		

count = 0
for i in sieve(1000000):
	if circular_test(i):
		print(i)
		count+=1
print(count)		
