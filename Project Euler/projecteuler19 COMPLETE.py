'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1901 was a Tuesday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
months = [31,28,31,30,31,30,31,31,30,31,30,31]	
days = ['Tuesday','Wednesday', 'Thursday','Friday','Saturday', 'Sunday', 'Monday'] # 1st Jan 1901 was a tuesday (365 mod 7 is 1 dum dum)
sunday_count = 0 
day_count = 0

def leap_year(year):
	if (year%100 == 0):
		if (year%400 == 0):
			return True
		else:
			return False	
	else:
		if (year%4 == 0):
			return True	
		else:
			return False					

for year in range(1901,2001):
	for m in range(0,12): 
		dayName = days[day_count%7] # after adding a certain nunber of days, find the dayName by taking mod 7
		if dayName == 'Sunday':
			sunday_count += 1
		day_count += months[m] # as we only need to look at the first day of the month
		if (leap_year(year)):  # then add on the right number of days for a February in a leap year  
			if (months == 'February'): 
				day_count += 1
print(sunday_count)				


