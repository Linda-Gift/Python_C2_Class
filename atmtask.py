pin_number = 1234
num_of_attempt = 0
starting_balance = 250000
logged_in = True



while num_of_attempt < 4:
    login_pin = input("Enter your PIN number: ")
    if login_pin.isnumeric():
        login_pin = int(login_pin)
    
    if login_pin == pin_number:
        print("Login successful")
        break
            
    else:
        num_of_attempt += 1
        print("You have entered an incorrect pin, try again")
        print(f"You have {4 - num_of_attempt} attempts left")

if logged_in:
    while True:
        print("1. Deposit")
        print("2. Widthraw")
        print("3. Check Balance")
        print("4. Exit")

        response = input("Choose an between 1 - 4 option: ")

        if response == "1":
            amount =float(input("Enter the amount you would like to deposit"))

            if amount > 0:
                starting_balance += amount
                print("Deposit is successful")
                print("New balance:", starting_balance)
            else:
                print("Invalid deposit amount")

        elif response == "2":
            amount =float(input("Enter the amount you would like to widthraw"))

            if amount > 0:
                starting_balance -= amount
                print("Withrawal is successful")
                print("New balance:", starting_balance)

            elif amount > starting_balance:
                print("Insufficient balance")
            else:
                print("Invalid withdrawal amount")

        elif response == "3":
            print("Your account balance is:", starting_balance)

        elif response == "4":
            print("Thank you for banking with us")

        else:
            print("Invalid option, try again")
            break

else:
    print("Too many failed attempt")
    print("Account is hereby locked")

            

    