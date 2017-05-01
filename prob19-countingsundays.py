"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeap(year):
    if year % 4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def enumerateYearsAnd1Jan(start, end):
    def addDayInYear(yr, m, month, start):
        end = 0
        m[month] = start
        if month == 'sep' or month == 'apr' or month == 'jun' or month == 'nov':
            end = start + 30
        elif month == 'feb':
            end = start + (29 if isLeap(yr) else 28)
        else:
            end = start + 31
        return end
    yr = {}
    yrm = {}
    day = 0
    for i in range(start, end + 1):
        dayinyear = day + 0
        yr[i] = day
        m = {}
        dayinyear = addDayInYear(i, m, 'jan', dayinyear)
        dayinyear = addDayInYear(i, m, 'feb', dayinyear)
        dayinyear = addDayInYear(i, m, 'mar', dayinyear)
        dayinyear = addDayInYear(i, m, 'apr', dayinyear)
        dayinyear = addDayInYear(i, m, 'may', dayinyear)
        dayinyear = addDayInYear(i, m, 'jun', dayinyear)
        dayinyear = addDayInYear(i, m, 'jul', dayinyear)
        dayinyear = addDayInYear(i, m, 'aug', dayinyear)
        dayinyear = addDayInYear(i, m, 'sep', dayinyear)
        dayinyear = addDayInYear(i, m, 'oct', dayinyear)
        dayinyear = addDayInYear(i, m, 'nov', dayinyear)
        dayinyear = addDayInYear(i, m, 'dec', dayinyear)
        yrm[i] = m
        day += 366 if isLeap(i) else 365
    return yr, yrm

yr, yrm = enumerateYearsAnd1Jan(1901, 2000)
count = 0
for ym in yrm:
    for m in yrm[ym]:
        daystart = yrm[ym][m]
        #print daystart, daystart%7
        if daystart%7 == 0:
            count += 1
print count
