students = []

def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    print("Student registered successfully.")

def display_students():
    print("\nRegistered Students")
    print("-------------------")

    for student in students:
        print(student)

register_student()
display_students()
