'''
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

# clearly for any base number a greater than 10, a**b will be longer than b digits --> so we only need to test the numbers a = 1-9
# -- once we get a power 9^a longer than 9 digits then there will be no larger number that satisfies the problem


ans = 0
for i in range(1,100): #our exponent number
	if len(str(9**i)) < i : # ie any larger exponents will not satisfy the problem (above)
		break 
	for base in range(1, 10): # our base number
		# we need to find the smallest base such that the claim holds, then we know it works up to 9 (10**n is exactly n+1 digits long)
		if len(str(base**i)) == i:
			break
	
	ans += (10 -base) 

print(ans)

