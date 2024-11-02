import sqlite3

class AttendanceTracker:
    def __init__(self):
        try:
            # Connect to the database (creates 'attendance.db' if it doesn't exist)
            self.conn = sqlite3.connect('attendance.db')
            self.cursor = self.conn.cursor()
            # Create table if it doesn't already exist
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                                    student_name TEXT PRIMARY KEY,
                                    count INTEGER DEFAULT 1)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during initialization: {e}")
        except Exception as e:
            print(f"Unexpected error during initialization: {e}")

    def mark_attendance(self, student_name):
        try:
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
        except sqlite3.Error as e:
            print(f"Database error when marking attendance: {e}")
        except Exception as e:
            print(f"Unexpected error when marking attendance: {e}")

    def view_attendance(self):
        try:
            # Fetch all attendance records from the database
            self.cursor.execute("SELECT student_name, count FROM attendance")
            records = self.cursor.fetchall()

            if records:
                print("Attendance records:")
                for student, count in records:
                    print(f"{student}: {count} times")
            else:
                print("No attendance records found.")
        except sqlite3.Error as e:
            print(f"Database error when viewing attendance: {e}")
        except Exception as e:
            print(f"Unexpected error when viewing attendance: {e}")

    def close_connection(self):
        # Explicitly close the database connection
        try:
            if self.conn:
                self.conn.close()
                print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")
        except Exception as e:
            print(f"Unexpected error when closing connection: {e}")

def main():
    tracker = AttendanceTracker()
    try:
        while True:
            print("\n1. Mark attendance")
            print("2. View attendance")
            print("3. Exit attendance")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter student name: ").strip()
                if name:
                    tracker.mark_attendance(name)
                else:
                    print("Invalid input: Student name cannot be empty.")
            elif choice == "2":
                tracker.view_attendance()
            elif choice == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    finally:
        # Ensure the database connection is closed before exiting
        tracker.close_connection()

if __name__ == "__main__":
    main()
