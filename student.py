students = []

def display_students():
    print("\nStudent Management System")
    print("-------------------------")
    
    if not students:
        print("No students registered.")
    else:
        for student in students:
            print(student)

display_students()
def mark_attendance():
    student_id = input("Enter Student ID: ")
    date = input("Enter Date: ")
    status = input("Enter Attendance (Present/Absent): ")

    print(f"Attendance for {student_id} on {date}: {status}")
