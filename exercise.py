#Task: 
# Student Grades Tracker
# Write a simple Python program that helps teachers track student grades and calculate averages.
  
# Requirements:
# Accept multiple student names and grades
# Calculate average grade
# Determine pass/fail status
# Display summary report
 
# HINT:

# Ask the teacher how many students they want to enter grades for
# For each student:
# a. Ask for the student's name
# b. Ask for their test score

# Check if each score is valid (between 0 and 100)
# Calculate the average of all scores

# Tell the teacher:
# a. Who passed (score ≥ 60)
# b. Who failed (score < 60)
# c. The class average
# d. The highest and lowest scores

# Solution:
num_of_student = input("Enter number of Students: ")

# if num_of_student.isnumeric():
#     num_of_student = int(num_of_student)

#     student1_name = input("Enter first student's name: ")
#     student1_score = float(input("Enter first student's score: "))
#     student2_name = input("Enter second student's name: ")
#     student2_score = float(input("Enter second student's score: "))
#     student3_name = input("Enter third student's name: ")
#     student3_score = float(input("Enter third student's score: "))



#     print("First student's name: ", student1_name)
#     print("First student's score: ", student1_score)
#     print("Second student's name: ", student2_name)
#     print("Second student's score: ", student2_score)
#     print("Third student's name: ", student3_name)
#     print("Third student's score: ", student3_score)
    
#     print("\n")
              
#     print(total_score)
#     print(score_average)

#     print("\n")
    
#     print(max(student1_score, student2_score, student3_score))
#     print(min(student3_score, student2_score, student1_score))

# else:
#     print("Enter a valid number between 0 and 100")


# if student1_score >= 85 and student1_score <=100 :
#     print("Score grade is: A")

# elif student1_score >= 70 and student1_score < 85 :
#     print("Score grade is: B")

# elif student1_score >= 55 and student1_score < 70 :
#     print("Score grade is: C")

# elif student1_score >= 45 and student1_score < 55 :
#     print("Score grade is: D")

# elif student1_score >= 30 and student1_score < 45 :
#     print("Score grade is: E")

# else:
#     print("Score grade is: F")


# if student2_score >= 85 and student2_score <=100 :
#     print("Score grade is: A")

# elif student2_score >= 70 and student2_score < 85 :
#     print("Score grade is: B")

# elif student2_score >= 55 and student2_score < 70 :
#     print("Score grade is: C")

# elif student2_score >= 45 and student2_score < 55 :
#     print("Score grade is: D")

# elif student2_score >= 30 and student2_score < 45 :
#     print("Score grade is: E")

# else:
#     print("Score grade is: F")


# if student3_score >= 85 and student3_score <=100 :
#     print("Score grade is: A")

# elif student3_score >= 70 and student3_score < 85 :
#     print("Score grade is: B")

# elif student3_score >= 55 and student3_score < 70 :
#     print("Score grade is: C")

# elif student3_score >= 45 and student3_score < 55 :
#     print("Score grade is: D")

# elif student3_score >= 30 and student3_score < 45 :
#     print("Score grade is: E")

# else:
#     print("Score grade is: F")



# print("First student's name: ", student1_name)
# print("Second student's name: ", student2_name)
# print("Third student's name: ", student3_name)
# print("First student's score: ", student1_score)
# print("Second student's score: ", student2_score)
# print("Third student's score: ", student3_score)
# print(total_score)
# print(score_average)


if num_of_student.isnumeric():
    num_of_student = int(num_of_student)

    student1_name = input("Enter first student's name: ")
    student1_score = float(input("Enter first student's score: "))
    student2_name = input("Enter second student's name: ")
    student2_score = float(input("Enter second student's score: "))
    student3_name = input("Enter third student's name: ")
    student3_score = float(input("Enter third student's score: "))

    print("First student's name: ", student1_name)
    print("First student's score: ", student1_score)
    print("Second student's name: ", student2_name)
    print("Second student's score: ", student2_score)
    print("Third student's name: ", student3_name)
    print("Third student's score: ", student3_score)

    if student1_score >= 85 and student1_score <=100 :
        print("Score grade is: A")

    elif student1_score >= 70 and student1_score < 85 :
        print("Score grade is: B")

    elif student1_score >= 55 and student1_score < 70 :
        print("Score grade is: C")

    elif student1_score >= 45 and student1_score < 55 :
        print("Score grade is: D")

    elif student1_score >= 30 and student1_score < 45 :
        print("Score grade is: E")

    else:
        print("Score grade is: F")


    if student2_score >= 85 and student2_score <=100 :
        print("Score grade is: A")

    elif student2_score >= 70 and student2_score < 85 :
        print("Score grade is: B")

    elif student2_score >= 55 and student2_score < 70 :
        print("Score grade is: C")

    elif student2_score >= 45 and student2_score < 55 :
        print("Score grade is: D")

    elif student2_score >= 30 and student2_score < 45 :
        print("Score grade is: E")

    else:
        print("Score grade is: F")


    if student3_score >= 85 and student3_score <=100 :
        print("Score grade is: A")

    elif student3_score >= 70 and student3_score < 85 :
        print("Score grade is: B")

    elif student3_score >= 55 and student3_score < 70 :
        print("Score grade is: C")

    elif student3_score >= 45 and student3_score < 55 :
        print("Score grade is: D")

    elif student3_score >= 30 and student3_score < 45 :
        print("Score grade is: E")

    else:
        print("Score grade is: F")

else:
    print("Enter a valid number between 0 and 100")

print("\n")

total_score = student1_score + student2_score + student3_score
score_average = total_score / num_of_student
              
print(total_score)
print(score_average)

print("\n")
    
print(max(student1_score, student2_score, student3_score))
print(min(student3_score, student2_score, student1_score))

