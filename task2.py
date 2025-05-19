students = {}

while True:
    print("Student menu")
    print("1. Add student")
    print("2. Show all student")
    print("3. Search student by NIM")
    print("4. Delete student by NIM")
    print("5. Exit)")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        nim = input("Enter NIM: ")
        name = input("Enter name: ")
        major = input("Enter major: ")
        gpa = input("Enter GPA: ")
        students[nim] = {"Name": name, "Major": major, "GPA": gpa}
        print("Your student is added.")

    elif choice == "2":
        if len(students) == 0:
            print("No students detected.")
        else:
            for nim in students:
                print("NIM: ", nim)
                print("Name: ", students[nim]["Name"])
                print("Major: ", students[nim]["Major"])
                print("GPA: ", students[nim]["GPA"])

    elif choice == "3":
        nim = input("Enter NIM to search: ")
        if nim in students:
            print("Name: ", students[nim]["Name"])
            print("Major: ", students[nim]["Major"])
            print("GPA: ", students[nim]["GPA"])
        else:
            print("Not found!")

    elif choice == "4":
        nim = input("Enter NIM to delete! ")
        if nim in students:
            del students[nim]
            print("Student deleted! ")
        else:
            print("Student not found. Please type it correctly.")

    elif choice == "5":
        print("EXITING PROGRAM.")
        break

    else:
        print("Please type the number you need like in the description.")