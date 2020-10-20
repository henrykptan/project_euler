'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

import time 
start=time.time()

collatz_dict = {} # create a dictionary TO AVOID RECALCULATING T A K E N O T E 
def collatz(x):	
	count = 1 # create a count of the number of elements in the sequence 
	temp = x # define a temporary variable which keeps track of the current term 
	while temp > 1:
		if (temp%2 == 0):
			temp = int(temp/2)
			if temp in collatz_dict:
				count += collatz_dict[temp]
				break
			else:
				count += 1	
		else:
			temp = (3*temp + 1)
			if temp in collatz_dict:
				count += collatz_dict[temp]
				break
			else:
				count += 1	
	
	collatz_dict[x] = count
	return(count)



length = 0
ans = 0
for n in range(0,1000000):
	c = collatz(n)
	if c>=length: 
		length = c
		num = n


print('chain length = {}, number = {} in time {}'.format(length, num, time.time()-start))

