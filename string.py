#Operation you can perform on strings

testing_str = "Learners are being instructed and taught \nhow to run the length string method in python\n don't forget these special characters and how to use\n them in programming, it will save you a lot"
# age_size = 68
# wear = True
# num_0f_absentees = None
# waist_Measure = 26.8

# #Length Operation
# print(len(testing_str))
# print(len(age_size))
# print(len(wear))
# print(len(num_0f_absentees))
# print(len(waist_Measure))

#Concatenation on Strings
str1 = "py"
str2 = "thon"
str4 = 60

str3 = "py" "thon"
# print(combo)
# print("\n")
# print(str3)

#Special characters in python
# \t
# \n

wrd1 = "Choice"
wrd2 = "Indentation"

# print(wrd2[0:])
# print(wrd2[:6])
# print(wrd2[::-1])
#[start : end : step]

# +
# *
# indexing []
# slicing [:]
# f-strings

# #String Methods
# len()
# upper()
text = "python is a programming language"
state = "lagos"
country = "Columbia"

# print(text.capitalize())
# print(state.capitalize())
# print(country.capitalize())


# lower()
# title()
# capitalize()


# strip()
stripped_txt = "   python is a programming language   "
stripped_txt2 = "   we are learning to strip in python @"
stripped_txt3 = "  python is a programming language @"

# print(stripped_txt.strip())
# print(stripped_txt2.lstrip())
# print(stripped_txt3.strip(" @"))


# replace()
# replace_txt = "python is a programming language"
# print(replace_txt)
# print(replace_txt.replace("programming", "MarkUp"))

# find()
# text = "Strawberry"
# print(text.find("r"))


# count()
# str_txt = "Interdenominational"
# print(str_txt.count("n"))

# split()
# split_txt = "Jethro Ezinne and Emmanuel are the future best future Python will produce"
# print(split_txt.split("Ezinne"))
# split_txt2 = "J,e,t,h,r,o"
# print(split_txt2.split(","))


# join()

# joined_txt = "J","e","t","h","r","o"
# print(" ".join(joined_txt))

# list_of_fruits = ["Mango", "Banana", "Pineapple", "Orange"]
# print(" ".join(list_of_fruits))


# startswith()
# start_txt = "Programming is said to be difficult to learn but with practice it is pretty easy with a sound teacher and a good learning environment"
# print(start_txt.startswith("Programming"))

# endswith()
# end_txt = "Programming is said to be difficult to learn but with practice it is pretty easy with a sound teacher and a good learning environment"
# print(end_txt.endswith("of"))

# isdigit()
# digit_txt = "1234567890"
# digit_txt2 = "1234567890a"
# digit_txt3 = "LindaGift"
# print(digit_txt.isdigit())
# print(digit_txt2.isdigit())
# print(digit_txt3.isdigit())

# isalpha()
# alpha_txt = "1234567890"
# alpha_txt2 = "1234567890a"
# alpha_txt3 = "LindaGift"
# print(alpha_txt.isalpha())
# print(alpha_txt2.isalpha())
# print(alpha_txt3.isalpha())

# isalnum()
# alnum_txt = "1234567890@&"
# alnum_txt2 = "1234567890asdfhgj"
# alnum_txt3 = "LindaGift$%"
# print(alnum_txt.isalnum())
# print(alnum_txt2.isalnum())
# print(alnum_txt3.isalnum())



#String formatting:
#f-strings
#.format()

user_name = "Jethro"
age = 18
city_of_residence = "Madrid"
nationality = "Spaniard"

#f-strings

print(f"Hello {user_name}, you are {age} years old, you live in {city_of_residence} and that makes you a {nationality}")

print("\n")

#.format()
print("Welcome this {} year old nigga called {}. I heard you live in {}, does this mean you are a {}?".format(age, user_name, city_of_residence, nationality))


print("Welcome this {3} year old nigga called {0}. I heard you live in {2}, does this mean you are a {1}?".format(user_name, nationality, city_of_residence, age))


# % formatting
# %s = String
# %d = Integer
# %f = Float

trader = "Prudence"
number_of_stalls = 14
product_price = 100.2367

print("Do you know that %s is a trader who markets imported fashion wears in Tejuosho market? I saw her advert on IG and i decided to visit her physical store, I found out that she has %d stalls. This is impressive for a lady of her stature, well i bought a bracelet worth %.2f naira" % (trader, number_of_stalls, product_price))






