'''
4. Read from a File
We used open in read mode and file.read to read and print to display.
'''
# Open the file in read mode ('r')
file = open("student_notes.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content
print("File Content:\n")
print(content)

# Close the file
file.close()

'''
Output:
File Content:
Student Grades Record
Roll: 91, Name: Rahul, Grade: A
Roll: 89, Name: Priya, Grade: B
Roll: 93, Name: Arjun, Grade: A
'''
