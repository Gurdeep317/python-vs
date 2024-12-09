# program to make a calender means find date,month,year
# import calendar

import calendar

year=int(input("enter a year:"))
month=int(input("enter a month:"))

calendar = calendar.month(year,month)
print(calendar)