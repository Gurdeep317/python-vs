def findHCF():
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    
    if x > y:
        smaller = y
    else:
        smaller = x

    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    
    print("The HCF of the two numbers is:", hcf)

# Call the function
findHCF()