# program to create right angle triangle patterns
# taking number of rows from user as a input
# using a for loop for rows
# use another for loop for columns
num=int(input("enter number of rows:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()