# Global variables: 
# Block scope/local variables

# Speed test:
# Create a tuple containing the names of the seven days of the week, print the first day and the last day
# Create a tuple of five favorite foods/scriptures or book titles. Use a for loop to print each food/Scripture or book title.
# Create a tuple of numbers: print the largest number, the Smallest number, the total and the number of items in the tuple.

# solution:
# week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(week_days[0])
# print(week_days[-1])

# favourite_foods = ("Pizza", "Burger", "Pasta", "fiesta Rice", "Ice Cream")
# for food in favourite_foods:
#     print(food)

# numbers = (1, 2, 3, 4, 5)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers))

# Set
# Introduction:
# unique_items = fork, spoon, gas cooker, pot, pan, mortar, pestle, knife, plate, cup, glass, bowl etc

# What is a Set? This is a collection of unordered, unindexed, and unique items. A set is a data structure that stores multiple items in a single variable. Sets are used to store multiple items in a single variable, and they are useful when you want to store a collection of unique items. A set does not acccept duplicate values.

kitchen_items = {"fork", "glass","fork", "spoon", "plate", "gas cooker", "pot", "pan", "mortar", "pestle", "knife", "plate", "cup", "glass", "bowl"}

# print(kitchen_items)

# Why do we need Set?
# Characteristics of Sets
# Creating a Set

# Empty Set: The correct way to create an empty set in python
empty_set = set()
print(type(empty_set))

# wrong way to create an empty set in Python
empty_set1 = {} 
print(type(empty_set1))

# items in a set cannot be indexed or accessed via index position in python
# print(kitchen_items[3])

# # Implication of duplicate values in a Set
# Nature of a Set
# Accessing Items in a Set
# for items in kitchen_items:
#     print(kitchen_items)

# for items in kitchen_items:
#     print(items)

# Adding items to a Set (add and update)
# Adding items to a set using the .add() method
# syntax for using the .add()
# Call the variable, then use the .add and in the bracket, specify the item you want to add, making sure to use the correct data type structure.
# kitchen_items.add("Dish washer")
# kitchen_items.add(10)
# kitchen_items.add(100.05)
# kitchen_items.add(True)
# print(kitchen_items)

#.update() method allows more than one or multiple items or values to be added to a set.
# Adding items to a set using the .update() method
# syntax for using the .update()
# Call the variable, then use the .update and in the bracket, specify the item you want to add, making sure to use the correct data type structure.

# kitchen_items.update("Sugar", [10, 20, 30, 40, 50])
# print(kitchen_items)

# The correct way to update a set using the update method
# kitchen_items.update(["sugar", 1000, False, "umbrella", 50.5])
# print(kitchen_items)

# Removing Items in a Set (remove, pop, discard, clear)

# .remove() method removes one item from a set.
# removing items from a set using the .remove() method
# syntax for using the .remove()
# Call the variable, then use the .remove and in the bracket, specify the item you want to remove, making sure to use the correct data type structure.

# kitchen_items.remove("sugar")
# print(kitchen_items)
# print(kitchen_items.remove("basket"))

# .discard method: This method also removes an item from a set.
# removing items from a set using the .discard() method
# syntax for using the .discard()
# Call the variable, then use the .discard and in the bracket, specify the item you want to remove, making sure to use the correct data type structure.

# kitchen_items.discard("fork")
# print(kitchen_items)
# print(kitchen_items.discard("basket"))


# pop() method: This method removes a random because remember a set is an unordered collection data type.
# removing items from a set using the .pop() method
# syntax for using the .pop()
# Call the variable, then use the .pop and in the bracket, specify the item you want to remove, making sure to use the correct data type structure.

# print(kitchen_items)
# kitchen_items.pop()
# print("\n")
# print(kitchen_items)

# clear() method: This method removes all items or values in a set
# removing items from a set using the .clear() method
# syntax for using the .clear()
# Call the variable, then use the .clear and in the bracket, specify the item you want to remove, making sure to use the correct data type structure.

# print(kitchen_items)
# kitchen_items.clear()

# print("\n")
# print(kitchen_items)

# Membership Operator (in)
# This returns a boolean result

# print("plate" in kitchen_items)
# print("Plate" in kitchen_items)

# Length
print(len(kitchen_items))

# Looping through a Set
# for items in kitchen_items:
#     print(kitchen_items)

# for items in kitchen_items:
#     print(items)


# Set Operations (union, intersection, difference, symmetric difference): The few powerful things you can do with set 

# Union: This combines all unique items from amongst two or more sets to be unified.

# syntax for unifying sets in python is either use the union() or *|*.

ccf_fe_students = {"Sammy", "LindaGift", "Jonathan", "Michael"}
ccf_python_student = {"LindaGift", "Ezinne", "Emmanuel", "Michael", "Jethro"}
ccf_uiux = {"RitaMary", "Kingsley", "Michael"}

result = ccf_fe_students | ccf_python_student | ccf_uiux
print(result)

ans = ccf_python_student.union(ccf_fe_students).union(ccf_uiux)
print(ans)

# Insecting sets using the Intersection operation. This operation returns common items in the sets in comparison.

# syntax for finding common items in sets in python is either use the intersection() or *&*.

result = ccf_fe_students & ccf_python_student & ccf_uiux
ans = ccf_python_student.intersection(ccf_fe_students).intersection(ccf_uiux)
print(result)
print(ans)

# Difference Operation: This operation helps to collate items in the first set but not in the second

# syntax for finding common items in sets in python is either use the difference() or *-*.

result = ccf_fe_students - ccf_python_student - ccf_uiux
ans = ccf_fe_students.difference(ccf_python_student).difference(ccf_uiux)
print(result)
print(ans)

# Symmetric Difference Operation: This operation allows items that are in one set or the other, but not the both.

# syntax for finding common items in sets in python is either use the symmetric_difference() or *^*.

result = ccf_python_student ^ ccf_fe_students ^ ccf_uiux
ans = ccf_python_student.symmetric_difference(ccf_fe_students).symmetric_difference(ccf_uiux)

print(result)
print(ans)

# Short Assignment:
# Create a set containing five fruits and print the set
# Create a set of programming languages. Add "Python" and "Java" after creating, print the updated set
# Create a set containing cities in the world, remove one city, and print the remaining cities
# Ask a user to enter a fruit, check whether the fruit exists in a set you created. If it exists, print: "Fruit found!" otherwise, print: "Fruit not found!"

# solution

fruits = {"Dragon", "Kiwi", "Grape", "Watermelon", "Strawberry"}
print(fruits)

for fruit in fruits:
    print(fruit)

prog_languages = {"JS", "Go", "Rust", "Kothlin", "C", "Sql", "C#", "Jquery", "Cobol", "Fortran"}

prog_languages.add("Python")
prog_languages.add("Java")
prog_languages.update(["Python", "Java"])

print(prog_languages)

world_cities = {"Lisbon", "Uppsala", "Stolkholme", "Malmo", "Lagos", "Ibadan", "New York", "Ilesha"}

world_cities.remove("Stolkholme")
print(world_cities)
world_cities.pop()
print(world_cities)
world_cities.discard("Ibadan")
print(world_cities)
world_cities.clear()
print(world_cities)

user_input = input("Enter a fruit name: ")
print(user_input in fruits)

if user_input in fruits:
    print("Fruit found!")
else:
    print("Fruit not found")
