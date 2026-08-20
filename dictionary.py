from pprint import pprint


# Dictionary: is a data type. It is a python built-in collection data type used to store an object information in a key-value pair. 

# What is a dictionary? A dictionary is ordered, it is mutable, it can store different data types but it does not allow duplicate values. 

# Why do we need or use dictionaries? When we need to collect information of an object such as this information about a person.
# firstname 
# last_name
# Middle_name
# age
# phonenumber
# email
# gender
# cor
# nok_firstname
# nok_lastname
# nok_email
# nok_phonenumber


# Creating a dictionary in Python: The syntax for creating a dictionary in python is the {} called the curly bracket or brace. 
# {}
# people = {} 
# people = dict()

# Characteristics of a dictionary: A dictionary is ordered, it is mutable, it can store different data types but it does not allow duplicate values. The keys must be written as strings while the values can be any data type


# Understanding dictionaries key-value pairs
persons = {
    "person1" :
    {   "fname" : "LindaGift",
        "lname" : "Johnson",
        "m_name" : "Ohaha",
        "score" : 18,
        "phone_number" : 234808494949,
    "gender" : "Female",
    "height" : 5.56,
    "is_adult" : True,
    "hobbies" : ["Writing", "Reading", "Cooking", "Going on Adventures", [1, 2, 4, 6, ["Sugar", "Milo","Toothbrush"]]],
    "pets" : {
        "Dog": "Flox", 
        "cat" : "Kane",
        "birdie" : "Talka",
        "flies" : {
            "wingtype": "Tsetse fly",
            "bitetype" : "Mosquito"
        }
    }
    },

    "person2" :{
        "fname" : "Jaden",
        "lname" : "Johnson",
        "m_name" : "Ohaha",
        "age" : 18,
        "phone_number" : 234808494949,
        "gender" : "Female",
        "height" : 5.56,
        "is_adult" : True,
        "hobbies" : ["Writing", "Reading", "Cooking", "Going on Adventures", [1, 2, 4, 6, ["Sugar", "Milo","Toothbrush"]]],
        "pets" : {
            "Dog": "Flox", 
            "cat" : "Kane",
            "birdie" : "Talka",
            "flies" : {
                "wingtype": "Tsetse fly",
                "bitetype" : "Mosquito"
            }
        }
        },

    "person1" :{"fname" : "LindaGift",
        "lname" : "Johnson",
        "m_name" : "Ohaha",
        "age" : 18,
        "phone_number" : 234808494949,
        "gender" : "Female",
        "height" : 5.56,
        "is_adult" : True,
        "hobbies" : ["Writing", "Reading", "Cooking", "Going on Adventures", [1, 2, 4, 6, ["Sugar", "Milo","Toothbrush"]]],
        "pets" : {
            "Dog": "Flox", 
            "cat" : "Kane",
            "birdie" : "Talka",
            "flies" : {
                "wingtype": "Tsetse fly",
                "bitetype" : "Mosquito"
            }
        }
        }
    
}

# pprint(person)

# Accessing dictionary values
# print(person["height"])
# print("\n")
# print(person["score"])


# Adding and updating items
# To add a value to a dictionary, we use this method:
# person["score"] = 95
# person["nationality"] = "Nigerian"
# person["isokay"] = True

# pprint(person)

# updating in python dictionary is more like editing the values in an existing dictionary
# print("\n")

# person["score"] = 98
# person["m_name"] = "Godslove"
# person["age"] = 25
# pprint(person)

# Removing items:
# The pop() method: this removes a specific key-value pair
# syntax: Call the variable, then the .pop() method and specify the key inside the bracket.

# person.pop("isokay")
# pprint(person)

# .popitem() method: This removes the last key-value inserted in a dictionary
# syntax: Call the variable, then the .popitem() method.

# pprint(person)

# print("\n")
# pprint(person.popitem())

# del keyword
# The del method: this removes a specific key-value pair
# # syntax: Call the variable, then the del method and specify the key inside the bracket.

# del person["age"]
# pprint(person)

# .clear() method: this removes all items in a dictionary
# syntax: Call the variable, then the .clear() method and specify the key inside the bracket.

# pprint(person)
# print("\n")

# person.clear()
# pprint(person)

# .keys(): This returns all keys stored in a dictionary
# pprint(person.keys())

# .values(): This returns all values assigned to keys stored in a dictionary
# pprint(person.values())

# .items() this returns the keys and values in a dictionary. 
# pprint(person.items())
# print(person.items())

# Checking to see if a key exists: We use the in keyword to check if a key exists in a dictionary.

# answer = "fname" in person
# print(answer)

# print("\n")
# result = "nok_name" in person
# print(result)

# Looping through dictionaries
# We can loop through a dictionary to get all the keys stored in the dictionary
# for i in person:
#     print(i)

# We can loop through a dictionary to get all the values stored in the dictionary
# for x in person.values():
#     print(x)

# We can loop through a dictionary to get all the keys and values stored in the dictionary
# for key, value in person.items():
#     print(key, ":", value)

# Checking to see the length of a dictionary using the len() method.
# print(len(person))

# .get() method: is used to return items that either exist or not. in a situation where an item does not exist, it returns none.
non_dict = {
    "data" : None,
    "islogged_in" : True,
    "number" : 20
}
# print(person.get("last_name"))

# Dictionary methods

# Nested dictionaries 
# How do we access items in a List inside a dictionary
# ans = person["hobbies"][0]
# print(ans)

# print("\n")
# ansa = person["hobbies"][4][4][2]
# print(ansa)

# How do we access items in a dictionary that is inside a dictionary

# solution = person["pets"]["flies"]["bitetype"]
# print(solution)

#Tasks:
# Create a dictionary called "student" containing vital information about a student or students. create your own keys and values for the student.
# print the dictionary

# use the information stored in the dictionary in the above,:
# print student's name, age, course, score

# Add and update the dictionary

# loop to print only keys first, values next and then keys and values.


# Dictionary + Loop + Conditional

students = {
    "mary" : 50,
    "John" : 70,
    "Chizaram" : 60,
    "Peter" : 39,
    "Judas" : 80
}

for name, score in students.items():
    if score >= 60:
        print(name, "Passed")
    else:
        print(name, "Failed")
