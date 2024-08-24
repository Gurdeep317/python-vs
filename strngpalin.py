# program to check a string is palindrome or not
# taking a string from user
# find reverse of that string
# using if , else condition 
a=input("enter any word:")
rev=a[ : :-1]
if a==rev:
    print("it is a palindrome")
else:
    print("it is not a palindrome")