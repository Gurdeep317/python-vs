# program to convert decimal to binary using recursion
# using def function
# taking n as a input from user 
# using floor division
# using modulus for remainder
# using if condition
def convertdecimal(n):
    if n>1:
        convertdecimal(n//2)
    print(n%2,end="")
n=int(input("enter a number:"))
print("the binary of a given number")

convertdecimal(n)


