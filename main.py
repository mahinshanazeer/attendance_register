from models import Student, Teacher
from attendance_manager import AttendanceManager

def print_menu():
    """Prints the main menu options."""
    print("\nAttendance Management System")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Mark Attendance")
    print("4. View Attendance by Person")
    print("5. View Attendance by Date")
    print("6. Exit")

def main():
    """Runs the main CLI loop."""
    manager = AttendanceManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                student = Student(student_id=student_id, name=name)
                manager.add_student(student)
                print(f"Student '{name}' added successfully.")
            elif choice == '2':
                teacher_id = input("Enter teacher ID: ")
                name = input("Enter teacher name: ")
                teacher = Teacher(teacher_id=teacher_id, name=name)
                manager.add_teacher(teacher)
                print(f"Teacher '{name}' added successfully.")
            elif choice == '3':
                person_id = input("Enter person ID (student or teacher): ")
                date = input("Enter date (YYYY-MM-DD): ")
                status = input("Enter status (present/absent): ").lower()
                manager.mark_attendance(person_id, date, status)
                print(f"Attendance marked for ID {person_id} on {date} as {status}.")
            elif choice == '4':
                person_id = input("Enter person ID to view attendance: ")
                records = manager.get_attendance_by_person(person_id)
                if not records:
                    print(f"No attendance records found for ID {person_id}.")
                else:
                    print(f"\nAttendance for ID {person_id}:")
                    for record in records:
                        print(f"  Date: {record.date}, Status: {record.status}")
            elif choice == '5':
                date = input("Enter date to view attendance (YYYY-MM-DD): ")
                records = manager.get_attendance_by_date(date)
                if not records:
                    print(f"No attendance records found for date {date}.")
                else:
                    print(f"\nAttendance for Date {date}:")
                    for record in records:
                        person_info = ""
                        student = manager.get_student(record.person_id)
                        if student:
                            person_info = f" (Student: {student.name})"
                        else:
                            teacher = manager.get_teacher(record.person_id)
                            if teacher:
                                person_info = f" (Teacher: {teacher.name})"
                        print(f"  Person ID: {record.person_id}{person_info}, Status: {record.status}")
            elif choice == '6':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
