'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''	
'''
import math


def divisorCount(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil((n)**(1/2))+1)):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors

n = 0
ans = 0
while n>=0:
	n += 1
	ans += n	
	if (divisorCount(n) > 10):
		break
	else:
		continue 	

print(ans)

#lol wont run for 500 divisors 

'''

def num_divisors(n):
    '''
    First we find the divisibility by 2, adding 1 to our factor count each time 
    '''
    if n % 2 == 0: 
        n = n/2
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = (count + 1) # count just gives the number of times you divide by two
    p = 3 # we then test the odds
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1 
            n = n/p
        divisors = divisors * (count + 1) # this time the count gives the number of times you divide by a certain ODD number (then plus one for 1)
        p += 2
    return divisors
 
def find_triangular_index(factor_limit): #  this is finding the number n for which the product of the number of divisors of 
    n = 1                                #  the nth and n+1th triangular numbers is greater than or equal to 500
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < factor_limit:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n
 
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2 # we then take the value above and do this because math
 
print(triangle)
		
print(num_divisors(8))




