# largest continuous sum of a list, for our example we should get 29

l1  = [1, 2, -1, 3, 4, 10, 10, -10, -1]

# brute force is to test every single sequence, using a double for loop, O(n^2)
def max_sum1(l):
	
	output = 0
	for i in range(len(l)):
		for j in range(len(l)-i):
			if sum(l[i:j]) > output:
				output = sum(l[i:j])
	return output			

# RECURSION iterate through, set initial largest_previous_seq to l[0], then test if (next element) or (largest_previous_seq + next element) is bigger 
# (ie if largest_previous_seq is positive), O(n)

def max_sum2(l):
	
	if len(l1) == 0:
		return 0 

	else:
		output = current_sum = l[0]

		for num in l[1:]:
			current_sum = max(current_sum + num, num)

			output = max(output, current_sum)

		return output


