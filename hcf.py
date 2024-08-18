def findHCF(x,y):
    # x=int(input("enter the value :"))
    # y=int(input("enter the another value:")) 
    # hcf=1   
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if (x%i==0 and y%i==0):
            hcf=i
    x=12
    y=30
    print("the hcf of two numbers is:",findHCF(12,30))