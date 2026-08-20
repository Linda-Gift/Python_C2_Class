# conditional is a condition that is either true or false.
# Comparison
# Comparison Operators
# ==
# print(5 == "5")
# print (5 == 5)

# # !=
# print(5 != 0)

# # >
# print(20 > 10)
# print(20 > 20)

# # <
# print(4 < 2)

# # >=
# print (10 >= 15)

# # <=
# print(6 <= 3)
# print(3 <= 3)

# #Task: use all of the the above comparison operators to compare any values of your choice.

# # Logical Operators
# # and
# age = 20
# print(age > 18 and age < 30)

# weather = "rainy"
# weekday = "Thursday"

# if weather == "rainy" and weekday == "Saturday":
#     print("I will go out to enjoy the weekend")
# else: 
#     print("please stay indoors")


# # or
# print(age < 12 or age == 20)

# # not
# is_raining = False
# print(not is_raining)
print(5 != 5)
print(not 5 == 5)

#Task: use the logical operators to combine or reverse conditions

# age = 15
# is_christian = True
# is_student = False

# print(age >= 18 and is_student)
# print(age < 18 or is_student)
# print(not is_christian)


# student_age = 20
# weather = "sunny"
# is_adult = False
# is_raining = True
# print(student_age  18 or student_age == 20 and weather == "sunny" and not is_adult == False)

# age = 16  
# salary = 30000  
# is_switch_on = True 
# print(age == 16 and salary == 30000) 
# print(age == 16 or salary == 30000)  
# print(not is_switch_on)

# Syntax for writing a statement
# if condition:
#     code

# Elements needed to write statments: if, elif, else

# if
# if age >= 18:
#     print("You can vote")

# elif
# else
# if age < 18:
#     print("You are not eligible to vote in Nigeria")
# else:
#     print("You can vote")

#Task: write a program that allows drivers to make decision depending on the color of a traffic light.

traffic_light = "maroon"


if traffic_light == "green":
    print("Go")
elif traffic_light == "Yellow":
    print("Slow down")
else:
    print("Stop")


