# taking input from user 
# using if statement and for loop 
# if num is 1 so that is not a prime number
# if num is greater than one than check it using for loop
num=int(input("enter a number="))
if num == 1:
    print("no is not a prime number")
if num>1:
    for i in range(2,num):
        if num% i == 0:
            print("no is not a prime number")
            break
    if num%i!=0:
            print("no is a prime no")
            