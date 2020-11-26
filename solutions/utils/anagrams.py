# largest continuous sum of a list, for our example we should get 29

l1 = [-5, 1, 2, -1, 3, 4, 10, 10, -10, -1]


# brute force is to test every single sequence, using a double for loop, O(n^2)
def max_sum1(test_list):
    output = 0
    for i in range(len(test_list)):
        for j in range(len(test_list) - i):
            if sum(test_list[i:j]) > output:
                output = sum(test_list[i:j])
    return output


# RECURSION iterate through, set initial largest_previous_seq to l[0], then test if (next element) or
# (largest_previous_seq + next element) is bigger
# (ie if largest_previous_seq is positive), O(n)

def max_sum2(test_list):
    if len(l1) == 0:
        return 0

    else:
        output = current_sum = test_list[0]

        for num in test_list[1:]:
            current_sum = max(current_sum + num, num)

            output = max(output, current_sum)

        return output


if __name__ == '__main__':
    print(max_sum2(l1))
