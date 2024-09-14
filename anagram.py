a=input("enter first string:")
b=input("enter second string:")
c=sorted(a.lower())
d=sorted(b.lower())
if c==d:
 print("the two strings are anagram")
else:
 print("these are not anagram")