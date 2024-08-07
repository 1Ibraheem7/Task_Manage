import random
import string

def generate_password(length):
    if length < 1:
        print("Password length must be at least 1.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("----- Welcome to Password Generator -----")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")

        another = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the password generator. Goodbye!")
            break

password_generator()
