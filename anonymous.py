# program using anonymous function 
# we use here list, map function ,lambda and for loop
# taking input from user
nterms=int(input("enter number of terms:"))
result=list(map(lambda x:2**x,range(nterms+1)))
for i in range(nterms+1):
    print("the value of 2 raised to power",i,"is",result[i])