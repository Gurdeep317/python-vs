# program to get line count of a file
# using len()function
f=open("kilo.py","r")
print(len(f.readlines()))
f.close()

lines=sum(1 for i in open("index.py"))
print(lines)