# program to check the file size
# using os module
import os
file=os.stat('arm.py')
print("file size:",file.st_size)