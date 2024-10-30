import sqlite3

class AttendanceTracker:
    def __init__(self):
        # Connect to the database (creates a file 'attendance.db' if it doesn't exist)
        self.conn = sqlite3.connect('attendance.db')
        self.cursor = self.conn.cursor()
        # Create table if it doesn't already exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                                student_name TEXT PRIMARY KEY,
                                count INTEGER DEFAULT 1)''')
        self.conn.commit()

    def mark_attendance(self, student_name):
        # Check if student already has an attendance record
        self.cursor.execute("SELECT count FROM attendance WHERE student_name = ?", (student_name,))
        result = self.cursor.fetchone()
        if result:
            # If student exists, increment their attendance count
            new_count = result[0] + 1
            self.cursor.execute("UPDATE attendance SET count = ? WHERE student_name = ?", (new_count, student_name))
        else:
            # If student doesn't exist, insert a new record
            self.cursor.execute("INSERT INTO attendance (student_name, count) VALUES (?, 1)", (student_name,))
        self.conn.commit()
        print(f"Attendance marked for {student_name}.")

    def view_attendance(self):
        # Fetch all attendance records from the database
        self.cursor.execute("SELECT student_name, count FROM attendance")
        records = self.cursor.fetchall()
        print("Attendance records:")
        for student, count in records:
            print(f"{student}: {count} times")

    def __del__(self):
        # Close the database connection when the object is destroyed
        self.conn.close()

def main():
    tracker = AttendanceTracker()
    while True:
        print("\n1. Mark attendance")
        print("2. View attendance")
        print("3. Exit attendance")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            tracker.mark_attendance(name)
        elif choice == "2":
            tracker.view_attendance()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()