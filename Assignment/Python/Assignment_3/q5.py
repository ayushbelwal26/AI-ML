students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print("MENU")
print("A:Add a student" , "\nB:Update marks","\nC:Search" , "\nD:Display all students and marks" , "\nE: To exit")

while True:
    choice = input("Enter your choice: ")
    if(choice == 'A'):
        a = input("Enter student name: ")
        b = int(input("Enter marks: "))
        students.update({a:b})
        print(students)

    elif(choice == 'B'):
        a = input("Enter student whose marks to update: ")
        b = int(input("Give marks of student: "))
        students[a] = b
        print(students)

    elif (choice == 'C'):
        a = input("Student to search: ")
        if(students.get(a) == None):
            print("Not found")
        else:
            print("Found")

    elif(choice == 'D'):
        print(students.items())

    elif(choice == 'E'):
        break

    else: 
        print("Enter valid choice")

print("Program exited......")