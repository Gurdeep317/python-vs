# program to find factorial using recursion
# using def function
# taking n as a input from user
# using if,elif,else condition
def fact(n):
    if n==1:
        return n
    else:
        return (n* fact(n-1))
n=int(input("enter a number:"))
if n<0:
    print("factorial of negative numbers does not exist")
elif n==0:
    print("factorial of zero = 1")
else:
    print("the factorial is:",fact(n))