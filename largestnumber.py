# taking num1,num2,num3 as a input from user
#using if ,elif,else condition 
num1=float(input("enter the num1="))
num2=float(input("enter the num2="))
num3=float(input("enter the num3="))
if (num1>num2) and (num1>num3):
    print("num1 is a largest number")
elif (num2>num3) and (num2>num1):
    print("num2 is a largest number")
else:
    print("num3 is a largest number")