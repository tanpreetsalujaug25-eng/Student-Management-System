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
