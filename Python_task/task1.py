def greet_user():
   print("Hello Julien, you are welcome to join me in CodeCraft-Forge")

greet_user()
greet_user()
greet_user()

def display_bio():
   age = 18
   name = "LindaGift"
   fav_lang = "JavaScript"
   goal = "to become a reknowned Frontend Engineer and an Interaction Design Engineer"
   print(f"This is {name}, she is {age} years old, her favourite programming language is {fav_lang} and she desires {goal}")

display_bio()

def add():
   num1 = 5
   num2 = 20
   print(num1 + num2)

def subtract():
   num1 = 5
   num2 = 20
   print(num1 - num2)

def multiply():
   num1 = 5
   num2 = 20
   print(num1 * num2)

def divide():
   num1 = 5
   num2 = 20
   print(int(num2 / num1))

add()
subtract()
multiply()
divide()

def welcome_message():
   print("CodeCraft-Forge is an Ed-Tech, established to teach practical and real world knowledge programming languages such as Python amongst others. Students have good things to say about our python classes")

welcome_message()

def convert_to_fahrenheit():
   f = 9/5 + 69
   print(f)

convert_to_fahrenheit()

def greet(name):
   print(f"Hello {name}! welcome to Python")

greet("Julien")
greet("Anselm")
greet("Youssef")
greet("Judith")
greet("Olamilekan")

def add_numbers(a, b):
   sum = a + b
   print(sum)

add_numbers(10, 20)
add_numbers(6, 20)
add_numbers(2, 100)

def calculate_area(length, width):
   area = length * width
   print(area)

calculate_area(100, 200)
calculate_area(16, 20)
calculate_area(24, 40)
calculate_area(10, 258)

def check_result(name, score):
   print(f"Hello {name}, you scored {score} in this examination")
   if score >= 50:
      print(f"Congratulations{name} you pass")
   else:
      print(f"Hi {name}, you can always try again. You failed this time.")

check_result("Emmanuella", 89)
check_result("Ella", 49)
check_result("Breila", 74)

def calculate_bill(item, price, quantity, discount):
   total_cost = price * quantity
   disc = total_cost * discount / 100
   after_disc = total_cost - disc
   print(f"Dear customer, you purchased {quantity} packs of {item}, each costs {price}. The total cost of {quantity} after {disc} is {after_disc}")

calculate_bill("Strawberry", 5000, 6, 5)

def check_even_odd(number):
   

   if number % 2 == 0:
      print(f"{number} is an even number")
   else:
      print(f"{number} is an odd number")

check_even_odd(5)
check_even_odd(10)
check_even_odd(55)
check_even_odd(1000)

def check_voting_eligibility(age):
   if age >= 18:
      print("You are eligible to vote")
   elif age < 0:
      print("This is an invalid number")
   else:
      print("You are not eligible to vote")

check_voting_eligibility(21)
check_voting_eligibility(-6)
check_voting_eligibility(11)

def find_largest(a, b, c):
   if a > b and a > c:
      print(f"{a} is the largest number")
   elif b > a and b > c:
      print(f"{b} is the largest number")
   elif c > b and c > a:
      print(f"{c} is the largest number")
   elif a == b:
      print(f"{c} is the largest number")
   elif a == c:
      print(f"{b} is the largest number")
   elif a == b and a == c:
      print("All numbers are equal")
   elif b == a and b == c:
      print("All numbers are equal")
   elif c == a and c == b:
      print("All numbers are equal")
   else:
      print("All numbers are equal")

find_largest(10, 30, 5)
find_largest(100, 30, 10)
find_largest(3, 3, 5)
find_largest(1, 1, 1)

def multiplication_table(number):
   multiple = 1
   while multiple < 13:
      print(f"{number} * {multiple} = ", multiple * number)
      multiple += 1
      

multiplication_table(4)
multiplication_table(5)
multiplication_table(6)

def check_balance(balance):
   print(balance)

def deposit(balance, amount):
   acct_balance = balance + amount
   if amount <= 0:
      print("Enter a positive amount")
   else:
      print(acct_balance)

def withdraw(balance, amount):
   acct_balance = balance - amount
   if balance < amount:
      print("You have insufficient balance for this transaction")
   elif amount <= 0:
      print("Enter a positive amount")
   else:
      print(acct_balance)

check_balance(12000)
deposit(3000, -2000)
deposit(4000, 2000)
deposit(4000, 0)
withdraw(5000, -100)
withdraw(6000, 0)
withdraw(5000, 3000)