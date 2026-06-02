import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        student = {
            "id": student_id,
            "name": name,
            "marks": marks
        }

        students.append(student)
        save_students(students)

        print("Student Added Successfully!")

    elif choice == "2":

        if not students:
            print("No student records found.")

        for student in students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['marks']}"
            )

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
