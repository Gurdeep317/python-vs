# program to sort words in alphabetic order
# taking string from user
# using split
# using sort
# using for loop

a=input("enter anything here:")
b=a.split()
for i in range (len(b)):
     b[i]=b[i].lower()
print(b)
b.sort()
print(b)