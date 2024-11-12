# program for prime interval
# taking lower and upper limit from user
# using for loop
# using if,else condition
lower=int(input("enter the value of lower="))
upper=int(input("enter the value of upper="))

for i in range (lower,upper+1):
    if i>1:
        for num in range(2,i):
           if i%num == 0:
               break
        else:
         print(i)
