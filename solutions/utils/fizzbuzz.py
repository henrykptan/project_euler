# fizzbuzz 

nums = []

for i in range(1, 100):
    output = ''
    if i % 3 == 0:
        output += 'fizz'
    if i % 5 == 0:
        output += 'buzz'
    if output == '':
        output += str(i)
    nums.append(output)

print(nums)
