import sys

year = int(input('year : '))
print(year % 400 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 != 0)