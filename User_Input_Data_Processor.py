#Objective: The aim of this assignment is to process and format user input data.

#Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. 
# If not, print an error message.

def check_username_length(firstname, lastname):
    return (f"Welcome, {firstname} {lastname}!")

while True:
    firstname_input = input("Enter your first name: ")
    if len(firstname_input) < 2:
        print("Invalid input. First name must be at least 2 characters long.")
    lastname_input = input("Enter your last name: ")
    if len(lastname_input) < 2:
        print("Invalid input. Last name must be at least 2 characters long.")
    else:
        approved_username = check_username_length(firstname_input, lastname_input)
        print(f"{approved_username}")


    continue_input = input("Would you like to check another user's name? (yes/no): ").lower()
    if continue_input != "yes":
        break
