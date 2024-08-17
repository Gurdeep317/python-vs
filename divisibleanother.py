# program to find numbers divisible by another number
# using for loop is the first solution
# using for loop and if condition
print("the number is divisible by 13 is:")
for i in range(1,100):
    if i%13==0:
        print(i)

print()
# second solution of this program
# here we use list ,filter and lambda function 
# lambda function is a temporary and anonymous function
l=[66,39,48,98,26,87,67]
result=list(filter(lambda x:x%13==0,l))
print("the numbers divisible by 13 is:",result)
