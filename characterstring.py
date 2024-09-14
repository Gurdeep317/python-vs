# program to count the number of occurence of a character in a string
a="wscubetech"
char="b"
count=0
for i in a:
    if i==char:
        count=count+1
        print(count)