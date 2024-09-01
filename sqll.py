import sqlite3
conn=sqlite3.connect("sqlite.db")
ins='''
      insert into student(st_name,st_class,st_email)
      VALUES('ram','12th','ravi@gmail.com')
      '''
conn.execute(ins)
conn.commit()
conn.close()