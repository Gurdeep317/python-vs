# taking input from user
# use if ,else condition and while loop
# if num is greater than zero than using while loop 
# initially taking sum is zero than add num into sum
# and then decreament of 1 from number 
num=int(input("enter a number:"))
if num<0:
    print("enter a positive number")
else:
    sum=0
    while num>0:
       sum +=num
       num -=1

    print(sum)