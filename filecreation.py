# program to get file creation and modification date
# using os,pathlib and time module
# using ctime,mtime
import os,pathlib,time
file=pathlib.Path("C:\\Users\\lenovo\\PycharmProjects\\pythonProject\\.venv")
print("the creation date time:",time.ctime(os.path.getctime(file)))
print("the modification date time:",time.ctime(os.path.getmtime(file)))