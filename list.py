# Lists:
# What is a List in Python? 
# Explain why we use lists
# Identify the data type of a list
# Create a list
# Access items in a list
# Modify a list
# Perform common list operations
# Use important List Methods

ccf_python_students = ["Ezinne", "LindaGift", "Emmanuel", "Jethro", "RitaMary", "Eziefula", "Samuel", "Lucky", "Kingsley", "Samuel", "Lucky", "Feyi", "Arisnatha", "Michael", "Soledad"]

score_sheet = [45, 98, 100, 24, 56, 78, 70, 45, 86, 100, 74, 84, 86, 100, 56]

discount_list = [2.5, 0.05, 100.5, 98.4, 10.2]

items = [True, "book", 38, 5.5]

# print("Ezinne" in ccf_python_students)


# Changing items in a list:

#syntax for changing items in a list
# call the variable
# specify the index position of the item to be changed
# then specify what you want it changed to

# items[0] = "False"
# print(items)

# ccf_python_students[-1] = "Ronaldo"
# print(ccf_python_students)


#Adding items to a list:
# To add, you need to use the .append() method. This adds the item(s) to the end of the list

# call the variable that is variable of the list you want to add to
# use the .append

# score_sheet.append("LindaGift")
# score_sheet.append(100)
# print(score_sheet)


# inserting an item into a list
# This allows you to insert an item into a list in a specific position

#  call the variable
# use the .insert()
# then specify the index position and the item


# print("\n")
# discount_list.insert(2, True)
# print(discount_list)

# extend a list:
# create the lists
# add items in each list, it is also possible to have an empty list
# call the list you want to extend and in the extend bracket add the list you want to add.
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["Pawpaw", "Grapes", "Dragon fruit", "Kiwi"]
list3 = [True]

list1.extend(list2)
# print(list1)
# list1.extend(list3)
# print(list1)


# Removing items:
# The .remove() method removes an item by its value and you use this method if you know what or the value you want to remove

# syntax:
# call the variable
# then use the .remove() method and insert the item in the bracket
# list2 = ["Pawpaw", "Grapes", "Dragon fruit", "Kiwi"]
# list2.remove("Pawpaw")
# print(list2)

# poping items:
# The .pop() method removes the last item from a list. The pop method also allows us to specify the index position of an item to be removed/popped and you use this method if you want to remove the last items or you want to remove an item at a specific position.

# syntax:
# call the variable
# then use the .pop() method and insert the item in the bracket
list1 = [1, 2, 3, 4, 5, 6]
list1.pop(3)
# print(list1)

# deleting items:
# The del method removes the an item from a list or even an entire list. The del method allows us to specify the index position of an item to be removed/delected and you use this method if you want to remove an item or you want to delete an entire list.

# syntax:
# call the del method
# then use the variable method and insert the index position of the item to be deleted in a square bracket
list3 = [True]
del list3
# print(list3)


# clear items
# The clear() method removes the entire item(s) from a list but keeps the list. use this method if you want to remove all items in a list.

# syntax:
# call the clear method
# then use the variable method and insert the index position of the item to be deleted in a square bracket
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["Pawpaw", "Grapes", "Dragon fruit", "Kiwi"]
list3 = [True]
list1.clear()
list2.clear()
list3.clear()
# print(list1)
# print(list2)
# print(list3)


# .index:
# the .index() method allows us find and return the index postion of an item in a list. you use this method to know where an item is stored in a list

# syntax:
# call the variable
# then use the .index() method and insert the index position of the item to be deleted in a square 

list2 = ["Pawpaw", "Grapes", "Dragon fruit", "Kiwi"]
# print(list2.index("Dragon fruit"))


# count items in a list: 
# the .count() method allows us find out how many times an item(s) occurs or appears in a list. you use this method to know if duplicates or how many duplicates item is stored in a list

# syntax:
# call the variable
# then use the .count() method to check number of occurence(s).Specify the item whose occurence you wish to find in the bracket

ccf_python_students = ["Ezinne", "LindaGift", "Emmanuel", "Jethro", "RitaMary", "Eziefula", "Samuel", "Lucky", "Kingsley", "Samuel", "Lucky", "Feyi", "Arisnatha", "Michael", "Soledad"]

score_sheet = [45, 98, 100, 24, 56, 78, 70, 45, 86, 100, 74, 84, 86, 100, 56]

print(ccf_python_students.count("Samuel"))
print(score_sheet.count(100))



# sorting a list in reverse order or in a chronological order:
#The .sort() method is use to organize a list in an ascending order. eg abcd, 123 etc.

# syntax:
# call the variable
# then use the .sort() method to organize the list. you use this method if you want to organize a list in ascending order.

ccf_python_students = ["Ezinne", "LindaGift", "Emmanuel", "Jethro", "RitaMary", "Eziefula", "Samuel", "Lucky", "Kingsley", "Samuel", "Lucky", "Feyi", "Arisnatha", "Michael", "Soledad"]

score_sheet = [45, 98, 100, 24, 56, 78, 70, 45, 86, 100, 74, 84, 86, 100, 56]

ccf_python_students.sort()
score_sheet.sort()
# 



# sorting a list in reverse order:
#The .reverse() method is use to organize a list in a descending order. eg dcba, 4321 etc.

# syntax:
# call the variable
# then use the .reverse() method to check number of occurence(s).use this method if you want to organize or reverse the order of a list

ccf_python_students = ["Ezinne", "LindaGift", "Emmanuel", "Jethro", "RitaMary", "Eziefula", "Samuel", "Lucky", "Kingsley", "Samuel", "Lucky", "Feyi", "Arisnatha", "Michael", "Soledad"]

score_sheet = [45, 98, 100, 24, 56, 78, 70, 45, 86, 100, 74, 84, 86, 100, 56]

print("\n")
ccf_python_students.reverse()
score_sheet.reverse()
# print(ccf_python_students)
# print(score_sheet)

# copying a list:
#The .copy() method is use to duplicate a list.

# syntax:
# call the variable
# then use the .copy() method to check number of occurence(s).use this method if you want to duplicate a list. whatever changes that is made in the original or the copy does not affect.

score_sheet = [45, 98, 100, 24, 56, 78, 70, 45, 86, 100, 74, 84, 86, 100, 56]

duplicate_copy = score_sheet.copy()
# print(duplicate_copy)

score_sheet.append(20)
# print(score_sheet)
# print(duplicate_copy)

print("\n")
duplicate_copy.append("Shinny")
# print(duplicate_copy)
# print(score_sheet)


#Built-in Functions for List
# len(): This is used to check the number of items in a list

# Syntax:
# call the len function first
# inside the bracket, specify the list you want to check

print(len(score_sheet))
print(len(ccf_python_students))


# max(): This function is used to find the largest value in a list. You use this function on a list that stores only int or float.

# Syntax:
# call the len function first
# inside the bracket, specify the list you want to check

# print(max(score_sheet))
# print(max(ccf_python_students))

ccf_python_students.append("zoe")
# print(max(ccf_python_students))

# min(): This function is used to find the smallest value in a list. You use this function on a list that stores only int or float.

# Syntax:
# call the len function first
# inside the bracket, specify the list you want to check

# print(min(score_sheet))
# print(min(ccf_python_students))

# print(min(ccf_python_students))


# sum(): This function is used to find the add values in a list together. You use this function on a list that stores only int or float.

# Syntax:
# call the len function first
# inside the bracket, specify the list you want to check

print(sum(score_sheet))


# The "in" operation checks whether an item exists in a list

print(12 in score_sheet)
ccf_python_students.append("zoe")
print("Zoe" in ccf_python_students)



# concatenating lists
# concatenation: This operation is used to join two list together.

# Syntax:
#create the two list
# then use the + operator to concatenate them

first_llist = ["Amina", "Abdulbasit", 1, 10, 20, 30, 40]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

concatenated_list = first_llist + second_list
print(concatenated_list)


# list repetition:
# Repetition: This operation is used to repeat a list together as many times as you want using the "*" operator.

# Syntax:
#create the list
# then use the * operator to repeat

simple_list = ["Apple", "Kiwi", "Soybean"]
print(simple_list * 5)

# slicing a list: This means taking a part of a whole. IT is possible to slice a part or even a whole list.

# Syntax:
#create the list
# then use the [:] to repeat. the slice has three parts. the first is the starting point, the second is the end, and the last is the step.

ccf_python_students = ["Ezinne", "LindaGift", "Emmanuel", "Jethro", "RitaMary", "Eziefula", "Samuel", "Lucky", "Kingsley", "Samuel", "Lucky", "Feyi", "Arisnatha", "Michael", "Soledad"]

# sliced_list = ccf_python_students[::]
# print(sliced_list)

# Looping through a List
for student in ccf_python_students:
    print(student)
 


# Nesting in a List

# Objective:
# Creating lists
# Adding items to list(Append, insert, extend)
# Removing items to list(remove, del, pop, clear)
# Searching a list(index, count, in)
# Organizing a list(sort, reverse, copy)
# Built-in functions(len, max, min, sum)
# Slicing a list
# Looping through a list(for loop)

# customer_details = []

# customer_name = str(input("Enter your name here: "))
# print(customer_name)

# customer_details.append(customer_name)

# print("\n")
# print("This is the updated list: ", customer_details)