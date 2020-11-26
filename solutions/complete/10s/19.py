"""
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
"""
days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_names = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
# 1st Jan 1901 was a tuesday (365 mod 7 is 1)


def is_a_leap_year(year_input):
    if year_input % 100 == 0:
        return year_input % 400 == 0
    else:
        return year_input % 4 == 0


if __name__ == '__main__':
    sunday_count = 0
    day_count = 0

    # Iterate through the first day of each month of each year
    for year in range(1901, 2001):
        for month in range(0, 12):
            # after adding a certain number of days, find the dayName by taking mod 7
            dayName = day_names[day_count % 7]
            if dayName == 'Sunday':
                sunday_count += 1
            day_count += days_in_each_month[month]  # as we only need to look at the first day of the month
            if is_a_leap_year(year):  # then add on the right number of days for a February in a leap year
                if days_in_each_month == 'February':
                    day_count += 1
    print(sunday_count)
