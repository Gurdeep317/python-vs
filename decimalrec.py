def convertdecimal(n):
    if n>1:
        convertdecimal(n//2)
    print(n%2,end="")
n=int(input("enter a number:"))
print("the binary of a given number")

convertdecimal(n)


