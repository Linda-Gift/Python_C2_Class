# Scope in python is where python sees your variable(s)
# types of scope in python: Global scope and local/in-block scope


# age = 18

# print(age)


# def global_variable():
#     print(age)

# global_variable()

living_room_item = "Television"

# def things_in_the_living_room():
#     print(f"I found a {living_room_item} in LindaGift's house")
#     print(f"It's quite pathetic that people mistake LindaGift's age as {age}")

# # things_in_the_living_room()


# def calculate_average(score1, score2, score3):
#     total_score = score1 + score2 + score3
#     average_score = total_score / 3
#     print(average_score)
    



def franchise():
    global age
    age = 24
    return(age)


# franchise()

# print(age)

linda_age = franchise()
print(linda_age)
