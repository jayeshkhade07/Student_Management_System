import json
import os

FILE_NAME = "students.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r")as file:
        students = json.load(file)
else:
    students = []


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students,file, indent=4)



def add_student():
    student_id = input("Enter student ID:")
    for student in students:
        if student.get("student_id") == student_id:
            print("Student ID already exists!")
            return
    name = input("Enter student name:")
    age = input("Enter student age:")
    course = input("Enter student course:")
    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    save_students()
    print("Student added successfully!")

    
def view_students():
    print("\nStudent List")
    print("---------------")
    if len(students) == 0:
        print("No student found.")
    else:
        for student in students:
            print("Student ID:",student.get("student_id", "Not assigned"))
            print("name:",student["name"])
            print("age:",student["age"])
            print("course:",student["course"])
            print("--------------")


def search_student():
    student_id = input("Enter student ID to search:")
    for student in students:
        if student.get("student_id") == student_id:
            print("Student found!")
            print("Student ID:",student.get("student_id", "Not assigned"))
            print("Name:", student["name"])
            print("age:", student["age"])
            print("course:", student["course"])
            return
    print ("Student not found.")


def update_student():
    student_id = input("Enter student ID to update:")
    for student in students:
        if student.get("student_id") == student_id:
            print("Student found!")
            student["name"] = input("Enter new name:")
            student["age"] = input("Enter new age:")
            student["course"] = input("Enter new course:")
            save_students()
            print("Student updated successfully!")
            return
    print("Student not found")       


def delete_student():
    student_id = input("Enter student ID to delete")
    for student in students:
        if student.get("student_id") == student_id:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return
    print("Student not found.")




while True:
    print("\nStudent Management System")
    print("--------------------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice:")
    if choice =="1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student() 
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Studant Management System!")
        break
    else:
        print("Invalid choice. Please try again.")






                          

                    
                      
