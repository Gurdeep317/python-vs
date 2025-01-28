total_sum = 0
print("Enter 50 numbers:")


for i in range(50):
    number = float(input(f"Enter number {i+1}: "))
    total_sum += number

print("The sum of the 50 numbers is:", total_sum)