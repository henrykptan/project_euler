'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
# notes 
# 1. can't have just the sum of one prime /
# 2. need to be odd - must have an odd number of odd numbers /
# 3. only need to search up to 500,000 as any consecutive sum afterwards will exceed 1 mil /
# 3i. AND ofc once our sum for a certain starting number exceeds 100 we can stop searching /
# 4. dont need to keep searching if current longest sequence is longer than the number of primes left to search 
# 5. IMPORTANT search from longest to shortest, as then when prime sum less than the limit is found we can stop for a given starting number n, KEEPING TRACK OF THE END NUMBER m
#    THIS MEANS for the next starting number (ie n+1) we will only need to search starting with end num m+1 
# 6. and we only need to search for sum lengths longer than previous


from math import ceil, sqrt
import time

start = time.time()

def sieve(n):
    '''
    Creates a list of primes up to a certian number n
    '''
    is_prime = [True]*n
    is_prime[0] = False 
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2 
        while index < n:
            is_prime[index] = False
            index = index+i 
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime
    
def max_consec_prime_sum(limit): # the number the sum has to be less than

        cap = ceil(limit/2) # where we can stop searching, as the sum will exceed the limit ( by 3. )

        primes = sieve(limit)   # used to test if out sum is prime         
        test_primes = [prime for prime in primes if prime < cap] # primes we are using to sum (no need to go over cap)

        longest_seq = []

        max_index = len(test_primes) - 1

        for start_index in range(len(test_primes)): # starting from the smallest prime
            for end_index in range(max_index + 1, len(longest_seq), -1): # (note final_index +1 by 5.) start from the end 
                sequence = test_primes[start_index:end_index]
                total = sum(sequence)
                if total > limit: # if our running sum is greater than the limit
                    max_index = end_index # set the max index to be our current end
                elif total in primes: # if the total is prime then we break
                    if len(sequence) > len(longest_seq): # and if the sequence is longer than out current longest we replace
                        longest_seq = sequence
                    break        
        return longest_seq
                    
ans = max_consec_prime_sum(1000000)



if __name__ == "__main__":
    
    print("sum = {}, longest sequence = {}, sequence length = {}, time taken = {}".format(sum(ans), ans, len(ans), time.time()-start))
