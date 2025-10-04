'''
1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
here we used a basic if else statement to carry out marks and all.
'''
score=int(input("Enter your score: "))
grade=""
if score >= 90:
    grade="A"
elif score >= 80 and score <=89:
    grade="B"
elif score >= 70 and score <=79:
    grade="C"
elif score >= 60 and score <=69:
    grade="D"
else:
    grade="F"
print("Your grade is : " + grade)

'''
Output:
Enter your score: 60
Your grade is : D     

Enter your score: 59
Your grade is : F     

Enter your score: 91
Your grade is : A
'''