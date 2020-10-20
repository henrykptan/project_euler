'''
Project Euler 56

a, b < 100, what is the maximal digital sum of a**b


'''

def digital_sum(n):
	return sum([int(i) for i in str(n)])

L = 100

max_sum = 0
pair = (0,0)
for i in range(L):
	for j in range(L):
		if digital_sum(i**j)>max_sum:
			max_sum = digital_sum(i**j)
			pair = (i,j)
print(max_sum, pair)





