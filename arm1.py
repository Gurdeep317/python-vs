# taking input from the user
# initially sum is zero
num=int(input("enter a number="))
sum=0
temp=num
# using while loop and if, else condition
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp//=10
if sum==num:
        print("it is an armstrong number")
else:
     print("it is not an armstrong number")