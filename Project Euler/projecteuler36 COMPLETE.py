'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
import math
def highest_power_of_2(n):
	i = 1
	while n/(2**i) >= 1:
		i += 1
	return (i-1)

def binary_converter(n):
	num = []
	total = n	
	for i in range(0, highest_power_of_2(n)+1):
		power_i = (highest_power_of_2(n) - i) # to go in order of power increasing 
		num.append(str(int(total/(2**power_i)))) # int used as a floor function, adding the value to the array 
		total -= (2**power_i)*int(total/(2**power_i)) # remaining total after minusing the contribution from 2^(power_i)
	return("".join(num)) 


def palindrome_test(n):
	N = str(n)
	if N == N[::-1] and str(binary_converter(n)) == str(binary_converter(n))[::-1]:
		return True
	else:
		return False	

ans = 0
for n in range(0,1000000):
	if palindrome_test(n):
		print(n, binary_converter(n))
		ans += n
print(ans)		