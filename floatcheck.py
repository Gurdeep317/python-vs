# Program to Check If a String Is a Number (Float)
# using def function
# using try and except
num=input("enter something here:")
def float_check (num):
    try:
        float(num)
        return True
    except:
        return False
    
print(float_check(num))