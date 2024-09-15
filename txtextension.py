# program to find all file with .txt extension present inside a dictionary
# using os module
# using for loop
# using if condition
import os
for file in os.listdir("C:\\Users\\lenovo\\OneDrive"):
   if (file.endswith(".txt")):
    print(file)
