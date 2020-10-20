'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

def digitsum(x):
	summ=0
	while x > 0:
		summ+= x%10
		x//=10
	return summ	
 
print(digitsum(2**1000))

