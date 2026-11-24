import csv

#  File handling 
# What file handling is and why it is useful: 
# Open and close from text files
# open()

# file = open("Article.docx", "w")
# file.write("We are learning file handling and now practicing how to write into text files.\n")
# file.write("Put this in the next line.\n")
# # print(file)
# file.close()


# work_file = open("student_file.docx", "w")
# work_file.write("What is the difference between .doc and .docx Microsfoft Word file extension format?\n ")
# work_file.close()


# work_file = open("student_file.docx", "a")
# work_file.write("We are not testing how to update, edit contents in a file\n")
# work_file.write("We have seen how the append mode works in Python\n")
# work_file.close()


# with open("student_file.docx", "a") as work_file:
#     work_file.write("We are looking at another method of opening and closing a file without calling two separate python functions.\n")


# with open("student", "r") as library:
#     result = library.read()
#     print(result)

# with open("student", "r") as library:
#     answer = library.readlines()

#     for sentence in answer:
#         print(sentence)

#     print("\n")
#     print("=" * 30)
#     print(answer[5])

# with open("note", "w") as wisdom:
#     resp = wisdom.write("")
#     print(resp)
    
# Task: Personal Notes Manager. This program should allow users to:
# 1. Add a note
# 2. View all saved notes
# 3. Exit the program
   




# Read data from text files
# Write new data to files and append data without deleting existing content
# Using with open() to manage files safely
# Understanding file modes
# Modes: Read, Write, Append, Extended
# Read and write into files using Loops and functions
# Handling missing files and other other common file errors: file not found, permission error: Write, read, is directory error, unicode decode error.

# The code below returns an error because we are trying to read this as a file whereas it is a directory
# with open("new_folder", "r") as library:
#     answer = library.readlines()

#     print(answer)


# try:
#     with open("new_folder", "r") as test:
#         content = test.read()
#         print(content)

# except FileNotFoundError:
#     print("This file does not exist")

# except PermissionError:
#     print("You do not have permission to read this file.")



# Work with CSV and JSON files
# What is CSV: The full meaning of CSV is, comma separated values. It can be opened with excel otherwise known as spreadsheet. Each CSV values are column and rows separated by a comma.

# with open("superstore.xlsx", "r", newline="", encoding="utf-8") as spreadsheet:
#     container = csv.DictReader(spreadsheet)
#     for row in container:
#         print(row["Customer Name"], row["City"])



with open("student.csv", "r", newline="", encoding="utf-8") as student_data:
    student_reader = csv.DictReader(student_data)
    
    for column in student_reader:
        print(column["Name"], column["Score"], column["Subject"], column["Grade"])



# Build a practical application that stores and retrieves information
