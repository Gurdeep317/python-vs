# program to find sum of natural number using recursion
# using def function
# using if,else condition 
# taking n as a input from user
def sum(n):
    if n<=1:
        return n 
    else:
        return n + sum(n-1)
n=int(input("enter a number:"))
if n<=0:
    print("enter a positive number")
else:
    print("the sum is:",sum(n))