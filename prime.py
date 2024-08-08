num=int(input("enter a number="))
# if num==1:
#     print("number is not prime")
 if num>1:
        for i in range (2,num):
            if num % i == 0:
                print("number is not a prime number ")
                break
             else :
         print("number is a prime number") 
else:
    print("number is not a prime number")
       