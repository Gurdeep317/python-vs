# program for simple attendance tracker
class AttendanceTracker:
  def __init__(self):
    self.attendance={}
  def mark_attendance(self,student_name):
    if student_name in self.attendance:
      self.attendance=student_name+1
    else:
      self.attendance=student_name
      print(f"Attendance marked for {student_name}.")
      
