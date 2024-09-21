# Python Program to Extract Extension From the File Name
# using os module
import os
file=os.path.splitext("filename.py")
print(file)
print(file[0])
print(file[1])
