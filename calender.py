# program to make a calender means find date,month,year
# import calendar
# taking inputs of year and month
import calendar
year=int(input("enter a year:"))
month=int(input("enter a month:"))
calendar = calendar.month(year,month)
print(calendar)