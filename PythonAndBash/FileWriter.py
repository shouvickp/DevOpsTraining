'''
3.Write to a File
Write a program to create a text file and write some content to it.

Using file functions like write and open.
'''
# Open the file in write mode ('w')
file = open("student_notes.txt", "w")

# Write some content to the file
file.write("Student Grades Record\n")
file.write("Roll: 91, Name: Rahul, Grade: A\n")
file.write("Roll: 89, Name: Priya, Grade: B\n")
file.write("Roll: 93, Name: Arjun, Grade: A\n")

# Close the file
file.close()

print("Content written to student_notes.txt successfully.")

'''
Output:
Content written to student_notes.txt successfully.
PS D:\DevOpsTraining> ls                                   
Directory: D:\DevOpsTraining
Mode                 LastWriteTime         Length Name                                           
----                 -------------         ------ ----                                           
d-----        04-10-2025     18:00                PythonAndBash                                  
-a----        04-10-2025     18:00            122 student_notes.txt
PS D:\DevOpsTraining> cat .\student_notes.txt
Student Grades Record
Roll: 91, Name: Rahul, Grade: A
Roll: 89, Name: Priya, Grade: B
Roll: 93, Name: Arjun, Grade: A
'''