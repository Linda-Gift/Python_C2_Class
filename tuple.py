# Tuples:
# Introduction
# What is a Tuple in Python: A tuple is a built-in collection data type in Python that is used to store multiple items in a single variable. Tuples are ordered, immutable (cannot be changed after creation), and allow duplicate values.

# Why do we use Tuples? We use tuples when we want to group related data together and ensure that the data cannot be modified. They are also more memory efficient than lists and can be used as keys in dictionaries.

# What type of data type is a Tuple?A tuple is a  built-in collection data type.

#  Characteristics of Tuples:
# it is immutable, can contain duplicate values, can contain different data types, ordered, can be nested.

# Difference between a List and a Tuple:
# Lists are mutable, meaning their elements can be changed, while tuples are immutable. Lists are defined using square brackets [], while tuples are defined using parentheses (). Lists have more built-in methods than tuples. You can add items to a list while you cannot to a tuple. you can remove items from a list while you cannot in a tuple. Items can be changed in a list while you cannot in a tuple. Lists are generally used for collections of items that may need to be modified, while tuples are used for collections of items that should remain constant.

# Creating Tuples: The syntax for creating a tuple is to use parentheses () and separate the items with commas. For example, my_tuple = (1, 2, 3) creates a tuple with three items.

ccf_python_students = ("John", "Jane", "Bob", "Alice")
score_sheet = (90, 85, 95, 80)
discount_float = (0.1, 0.2, 0.3, 0.4)
truthy_values = (True, False, True, False)
mixed_tuple = (1, "Hello", 3.14, True, [1, 2, 3], (4, 5, 6))

quiz_scores = ("Lindagift",)

print(type(quiz_scores))


# Accessing items in Tuples: You can access items in a tuple using indexing. The index starts at 0 for the first item, 1 for the second item, and so on. You can also use negative indexing to access items from the end of the tuple.
# syntax:
# the name of the tuple variable, followed by the index position of the item you want to access in square brackets []. 

mixed_tuple = (1, "Hello", 3.14, True, [1, 2, 3], (4, 5, 6))
print(mixed_tuple[4])
print(mixed_tuple[-1])


# Slicing Tuples: You can slice a tuple to access a range of items. The syntax for slicing is tuple_name[start:end:step], where start is the index of the first item to include, end is the index of the last item to include, and step is the interval between items.
# syntax:
# the name of the tuple variable, followed by the start index position, end index position and step in square brackets [].

mixed_tuple = (1, "Hello", 3.14, True, [1, 2, 3], (4, 5, 6))

print(mixed_tuple[0:4:2])

# Looping through Tuples: The same way you can loop through a list, is the same way you can loop through a tuple. You can use a for loop to iterate over the items in a tuple.

for item in mixed_tuple:
    print(item)

# Checking to see if an item exists in a Tuple: You can use the in keyword to check if an item exists in a tuple. This will return True if the item is found and False if it is not found.
print("yes" in mixed_tuple)

# checking the length of a tuple: Checking to see how many items are in a tuple is done using the len() function. The len() function returns the number of items in a tuple.

# syntax: call the variable, then use the len() function to check the length of the tuple.
print(len(mixed_tuple))


# Tuple Methods: use common Tuple methods
# .count() method: The count() method returns the number of times a specified value appears in a tuple. The syntax for using the count() method is tuple_name.count(value), where value is the item you want to count.
# syntax: call the variable first, then use the .count() method and specify the item you want to count in the bracket.

mixed_tuple = (1, "Hello", 3.14, True, 3.14, [1, 2, 3], [1, 2, 3],  (4, 5, 6), "Hello", True)
print(mixed_tuple.count(True))

# .index() method: The index() method returns the index of the first occurrence of a specified value in a tuple. The syntax for using the index() method is tuple_name.index(value), where value is the item you want to find the index of.
# syntax: call the variable first, then use the .index() method and specify the item you want to find the index of in the bracket.

print(mixed_tuple.index(True))

# Built-in functions that works on Tuples
# max(): This function is used to find the largest value in a tuple. You use this function on a tuple that stores only int or float.

print(max(score_sheet))
print(max(discount_float))

# min(): This function is used to find the smallest value in a tuple. You use this function on a tuple that stores only int or float.
print(min(score_sheet))

# sum(): This function is used to find the add values in a tuple together. You use this function on a tuple that stores only int or float.
print(sum(score_sheet))

# Tuple operations
# Concatenation: This operation is used to join two tuples together. The syntax for concatenation is tuple1 + tuple2, where tuple1 and tuple2 are the tuples you want to concatenate.

result =mixed_tuple + score_sheet
print(result)


# Repetition: This operation is used to repeat a tuple as many times as you want using the "*" operator. The syntax for repetition is tuple * n, where tuple is the tuple you want to repeat and n is the number of times you want to repeat it.

repeated_tuple = mixed_tuple * 2
print(repeated_tuple)

# Identify situations where tuples are more appropriate than lists
