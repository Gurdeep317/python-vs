# program to check if two strings are anagram
# taking two strings from user
# using sort
# using if , else condition
a=input("enter first string:")
b=input("enter second string:")
c=sorted(a.lower())
d=sorted(b.lower())
if c==d:
 print("the two strings are anagram")
else:
 print("these are not anagram")