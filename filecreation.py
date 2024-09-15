import os,pathlib,time
file=pathlib.Path("C:\\Users\\lenovo\\PycharmProjects\\pythonProject\\.venv")
print("the creation date time:",time.ctime(os.path.getctime(file)))
print("the modification date time:",time.ctime(os.path.getmtime(file)))