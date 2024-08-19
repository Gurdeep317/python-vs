def findHCF():
    x=int(input("enter first value:"))
    y=int(input("enter second value:"))
    if x>y:
        smaller = y
    else:
        smaller = x
    hcf=1
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    print("the hcf of two numbers:",hcf)
    findHCF()