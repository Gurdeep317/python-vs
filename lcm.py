# taking two numbers from user
# find which is greater
# if greater number is divisible by both numbers and remainder is zero than greater number is the lcm of two numbers
a=int(input("enter a number:"))
b=int(input("enter a another number:"))
maxnum=max(a,b)
while(True):
    if (maxnum%a==0 and maxnum%b==0):
        break
    maxnum=maxnum+1
print("the lcm of two numbers is:",maxnum)