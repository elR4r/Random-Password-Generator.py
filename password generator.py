# I'm not of a country that speaks english, i say this as a warning if at any point my comments are bad writed

import random, string
	
def main():
    global amount_of_characters

    try:
        amount_of_characters = int(input ("How many characters do you want your password to have? "))
    except ValueError:
        print("Introduce a valid NUMBER, no decimals, and no text")
        main()

    if amount_of_characters > 150: # We don't let the user introduce more than 150 characters
        print("Don't introduce more than 150 digits")
        main()        
    
    save_in_file = input("Do you wanna save this password in a file? (Y/n) ")

    password = generate_pass() # We create a variable that has the password already created

    if save_in_file == "Y" or save_in_file == "y":
        service_of_password = input("For what service is this password? ") # We ask to the user for what service is te password, like Instagram, Youtube, etc

        # This will be the path where we are going to save the password
        path_of_file = input("Introduce the path to the file (using \"/\" to separate the directories)\nThe file will be saved as \"passwords.txt\"\n")
        
        # We open (create the file if it's not created) passwords.txt in the directory that the user provided to us
        with open(f"{path_of_file}/passwords.txt", "a") as passwords_file:
            passwords_file.write(f"{service_of_password}: {password}\n")

    else:
        print(f"Your password is: {password}\n")

    exit(0)

# This function creates the password
def generate_pass():
    password = ""
    for i in range(amount_of_characters):               # We use for declaration to create a password with the requested amount of characters
        password += random.choice(string.ascii_letters) # We obtain random characters

    return password  # We return the password because we need to use it


if __name__ == '__main__':
    main()
