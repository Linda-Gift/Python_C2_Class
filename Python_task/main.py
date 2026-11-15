from mathematics import add
from mathematics import subtract
from mathematics import multiply
from mathematics import divide
import student_utils
from student_utils import calculate_average, check_grade, display_student_result 
from shopping import calculate_total, calculate_discount, display_receipt

# first_num = int(input("Enter a positive numbers: "))
# second_num = int(input("Enter a positive numbers: "))

# add(first_num, second_num)
# subtract(first_num, second_num)
# multiply(first_num, second_num)
# divide(first_num, second_num)


# first_score = int(input("Enter a positive numbers: "))
# second_score = int(input("Enter a positive numbers: "))
# third_score = int(input("Enter a positive numbers: "))


# print(calculate_average(first_score, second_score, third_score))


# result = check_grade
# print(result)

# if check_grade > 70 or check_grade == 100:
#     print("Student grade = A") 
# elif check_grade >= 60 or check_grade == 69:
#     print("Student grade = B")
# elif check_grade >= 50 or check_grade == 59:
#     print("Student grade = C")
# elif check_grade >= 45 or check_grade == 49:
#     print("Student grade = D")
# elif check_grade < 45:
#     print("Student grade = F")

item_name = (input("Enter the name of the item: "))
item_price = int(input("Enter the price of the item: "))
item_quantity = int(input("Enter the quantity of item: "))
item_discount_percentage = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

total_amt = calculate_total(item_price, item_quantity)

discount_saved = calculate_discount(total_amt, item_discount_percentage)


print(discount_saved)
print(total_amt)
display_receipt(item_name,  item_quantity, item_price, item_discount_percentage)



