'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

s = []
for n in range(0,1000000):
	s.append(str(n))

dec = "".join(s)

product = int(dec[1])*int(dec[10])*int(dec[100])*int(dec[1000])*int(dec[10000])*int(dec[100000])*int(dec[1000000])
print(product)