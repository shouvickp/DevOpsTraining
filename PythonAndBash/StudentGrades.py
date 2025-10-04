'''
2. Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
'''
studentRecords = {}

while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        roll = int(input("Enter the student's roll number: "))
        if roll in studentRecords:
            print(f"roll number {roll} already exists in system. Use option 2 to update the grade.")
        else:
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            studentRecords[roll] = {"name": name, "grade": grade}
            print(f"Added roll number {roll} with grade {grade}.")

    elif choice == "2":
        roll = int(input("Enter student's roll to update: "))
        if roll in studentRecords:
            grade = input("Enter new grade: ")
            studentRecords[roll]["grade"] = grade
            print(f"Updated roll number {roll}'s grade to {grade}.")
        else:
            print(f"roll number {roll} not found in system. Use option 1 to add the student.")

    elif choice == "3":
        if not studentRecords:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for roll, info in studentRecords.items():
                print(f"Roll: {roll}, Name: {info['name']}, Grade: {info['grade']}")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

'''
Output:
Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 1
Enter the student's roll number: 1
Enter student name: Shouvick Paul
Enter grade: 84
Added roll number 1 with grade 84.

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 1
Enter the student's roll number: 1
roll number 1 already exists in system. Use option 2 to update the grade.

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 1
Enter the student's roll number: 2
Enter student name: Ankur Ghosh
Enter grade: 90
Added roll number 2 with grade 90.

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 3

Student Records:
Roll: 1, Name: Shouvick Paul, Grade: 84
Roll: 2, Name: Ankur Ghosh, Grade: 90

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 2
Enter student's roll to update: 2
Enter new grade: 81
Updated roll number 2's grade to 81.

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 3

Student Records:
Roll: 1, Name: Shouvick Paul, Grade: 84
Roll: 2, Name: Ankur Ghosh, Grade: 81

Choose an option:
1. Add a new student and grade
2. Update an existing student's grade
3. Print all student grades
4. Exit
Enter your choice (1-4): 4
Exiting program. Goodbye!
'''