# taking input from the user
# use if ,elif,else condition 
# leap year which is divisible by 400 and 100
# also leap year which is divisible by 4 but not by 100 
year=int(input("enter a year="))
if (year % 400 == 0) and (year % 100 == 0):
    print("year is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("year is leap year")
else:
    print("year is not a leap year")