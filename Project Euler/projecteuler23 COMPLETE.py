'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
				

from math import sqrt
import time
start = time.time()
def is_abundant(n):
    '''
    We keep a count of the number of factors s , then check if s>n
    '''
    t = sqrt(n)
    s = -t+1 if t == int(t) else 1 # if n is a square, we need to minus the repeated root (note always count 1)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i # only need to work up to sqrt, then add both factors --> faster
    return s>n
    

abn = set() # note sets have a smaller memory complexity than lists 
L, s = 28123, 0

for n in range(1, L+1):
    if is_abundant(n): abn.add(n) # create a set of abundant numbers
    if not any( (n-a in abn) for a in abn ): # then if (n - abundant) is not in the set for all abundants we sum (by necessity in the range of the set)
        s+= n

print("answer is {}, found in time {}".format(s, time.time()-start))
