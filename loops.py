

# as long as count is < 20:
# print("Yes, count is less than 20")

# while condition:
#     code


count = 1

while count <= 100:
    print(count)
    count = count + 1


# Task: write to print numbers 1 to 20 using the while loop.
# Ask a user to enter a starting number, count down to 0. when the countdown finishes, print "blast off"

# solution

user_number = int(input("Enter a starting number: "))

while user_number >= 0:
    print(user_number)
    user_number = user_number - 1
print("Blast off")



# For Loop 

name = "LindaGift"
for a in name:
    print(a)


# syntax:
# for = start of a for loop
# a = a temporary variable
# in = look inside
# range = the boundary between  or saying repeat so and so times
# : = The loop is starting
# indented code = what should be done


student_name = input("Enter a student name: ")

for character in student_name:
    print(character)


for x in range(13):
    print()


# start, end, step

# Task: Print all even numbers between 2 and 50.
# print all odd numbers between 1 and 50
# ask a user for a number, prints its mulplication table from 1 to 12

for i in range(2, 50, 2):
    print(i)

for j in range(1, 50, 2):
    print(j)


for x in range(1, 13):
    print(f"{x} * {user_number} = ", x * user_number)


