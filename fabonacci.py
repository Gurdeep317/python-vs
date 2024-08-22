# profram to print fabonacci sequence
# taking a number for sequence from user as input
# using if , else condition
# using for loop with range 2 to num
a=0
b=1
num=int(input("enter a number for fabonacci sequence:"))
if num==1:
    print(a)
else:
    print(a)
    print(b)
    
    for i in range (2,num):
        c=a+b
        a=b
        b=c
        print(c)