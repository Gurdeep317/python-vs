# code to display fibonacci sequence using recursion
# using def function
# taking n as a input from user
# using if ,else condition 
# using for loop
def fibo(n):
    if n<=1:
        return n 
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter a number:"))
if n<=0:
    print("enter a positive numbe:")
else:
    print("fibonacci sequence")
    for i in range(n):
        print(fibo(i))