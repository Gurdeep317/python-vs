import pymysql as mq
myobj=mq.connect("localhost","root"," ")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")
except:
    print("database error")