# program for finding the roots of a quadratic equation
# import math
# taking a,b,c as a input from user
import cmath
a=int(input("enter the value of a="))
b=int(input("enter the value of b="))
c=int(input("enter the value of c="))
d=(b*b) - (4*a*c)
sol1=(-b + cmath.sqrt(d)) / (2*a)
sol2=(-b - cmath.sqrt(d)) / (2*a)
print("the given roots are:",sol1 ,sol2)