# Name : Rudresh Kumbhare
# PRN : 125B1B213
# Batch : D1

students = []

def add(studentsList, id, name, age, marks):
    student = {'ID': id, 'Name': name, 'Age': age, 'Marks': marks}
    studentsList.append(student)

def update(studentList, id, key, value):
    for student in studentList:
        if student['ID'] == id:
            student[key] = value
            print("Updated successfully...\n")
            return True
    print("ID not found.\n")
    return False

def delete(studentList, id):
    for i, student in enumerate(studentList):
        if student['ID'] == id:
            del studentList[i]
            print("Deleted successfully...\n")
            return True
    print("ID not found.\n")
    return False

def displayStudents(studentList):
    n = 1
    print("\n----- STUDENTS -----\n")
    for i in studentList:
        print("Student ", n, ":", end = " ")
        print(i)
        n = n + 1
    print("\n")

def toppers(studentList):
    if not studentList:
        print("Student not in the list.\n")
        return []
    maxMarks = max(student['Marks'] for student in studentList)
    return [student for student in studentList if student['Marks'] == maxMarks]

def averageMarks(studentList):
    if not studentList:
        return 0
    total = sum(student['Marks'] for student in studentList)
    return total / len(studentList)

while True:
    print("\n----- Student List -----\n")
    print("1. Add student data")
    print("2. Update student data")
    print("3. Delete student data")
    print("4. Display student data")
    print("5. Display maximum marks")
    print("6. Display average marks")
    print("7. Exit\n")
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        age = int(input("Enter student age: "))
        marks = int(input("Enter student marks: "))
        add(students, id, name, age, marks)

    elif (choice == 2):
        id = input("Enter student ID to update: ")
        key = input("Enter what do you want to update (ID, Name, Age, Marks): ")
        
        if key in ["Age", "Marks"]:
            val = int(input("Enter the new value: "))
        else:
            val = input("Enter the new value: ")
        update(students, id, key, val)

    elif (choice == 3):
        id = input("Enter student ID you want to delete: ")
        delete(students, id)

    elif (choice == 4):
        displayStudents(students)

    elif (choice == 5):
        topperStudents = toppers(students)
        print(f"Top scorer(s): {topperStudents}")

    elif (choice == 6):
        avg = averageMarks(students)
        print(f"Average Marks: {avg:.2f}")

    elif (choice == 7):
        print("Exiting...\n")
        break

    else:
        print("Invalid choice. Try again!\n")

