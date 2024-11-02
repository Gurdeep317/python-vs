# program for simple attendance tracker
# using class,def function,object
# using while
# using if ,elif,else statement
# using for loop
# using count
# taking some inputs from user
class AttendanceTracker:
  def __init__(self):
    self.attendance={}

  def mark_attendance(self,student_name):
    if student_name in self.attendance:
      self.attendance=student_name+1
    else:
      self.attendance=student_name
      print(f"Attendance marked for {student_name}.")

  def view_attendance(self):
       print("attendance records:")
       for student,count in self.attendance.items():
           print(f"{student}:{count} times")

def main():
    tracker=AttendanceTracker() 
    while True:
        print("\n1. Mark attendance")     
        print("2. View attendance")
        print("3. Exit attendance")
        choice=input("choose an option:")

        if choice=="1":
           name=input("enter student name:")
           tracker.mark_attendance(name)

        elif choice=="2":
           tracker.view_attendance()

        elif choice=="3":
           print("exiting the program.")
           break

        else:
           print("invalid choice,please try again.")
           
if __name__=="__main__":
    main()



    
    
     

      

