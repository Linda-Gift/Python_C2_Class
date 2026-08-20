#Task: write a program that accepts only three colors from user for traffic light signals and for each of these signals,they should indicate an instruction.

traffic_light = input("Enter a color: ").lower()


if traffic_light == "green" or traffic_light == "yellow" or traffic_light == "red":

    if traffic_light == "green":
        print("Go")
    elif traffic_light == "yellow":
        print("Slow Down")
    else:
        print("Stop")
else:
    print("Enter any of these valid colors: red, yellow or green")



# print(input("Enter Fullname: " ))

print(input("Enter First name: "))
print(input("Enter Middle name: "))
print(input("Enter Last name: "))



