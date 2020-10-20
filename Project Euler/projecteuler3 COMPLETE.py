'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
n = 600851475143 
i = 2
while (i*i < n): # once i becomes large enough then there can be no larger prime factors
	if (n%i == 0): 
		n  = n/i # dividing through by each prime factor
		i = i+1
	else:
		i = i+1
print(int(n))	