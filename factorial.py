# to take the input from the user
num=int(input("enter a number="))
factorial=1
# check if the number is positive,negative or zero
if num<0:
    print("factorial of negative numbers does not exist")
elif num == 0:
    print("factorial of zero is 1")
else :
    for i in range(1,num+1):
      factorial = factorial*i
    print("the factorial of", num,"is",factorial)
      

