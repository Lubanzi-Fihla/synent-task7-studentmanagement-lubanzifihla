import json

students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")

        students.append({
            "name": name,
            "age": age
        })

        save_data()
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter student name to delete: ")

        students[:] = [
            s for s in students
            if s["name"] != name
        ]

        save_data()
        print("Student deleted successfully!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
