"""
Main entry point for the password generator application.
"""
import password_generator as PasswordGenerator

def main():
    print("Password Generator by Jan")
    print("--------------------------------")
    print("1. Generate Password")
    print("2. Exit")
    print("--------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        password_settings = collect_password_settings()
        password = PasswordGenerator.generate_password(password_settings)
        print("Password: ", password)
    elif choice == "2":
        exit()

def collect_password_settings():
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ") == "y"
    include_lowercase = input("Include lowercase letters? (y/n): ") == "y"
    include_numbers = input("Include numbers? (y/n): ") == "y"
    include_symbols = input("Include symbols? (y/n): ") == "y"
    include_special_characters = input("Include special characters? (y/n): ") == "y"
    include_spaces = input("Include spaces? (y/n): ") == "y"
    settings = {
        "length": length,
        "include_uppercase": include_uppercase,
        "include_lowercase": include_lowercase,
        "include_numbers": include_numbers,
        "include_symbols": include_symbols,
        "include_special_characters": include_special_characters,
        "include_spaces": include_spaces
    }
    return settings

if __name__ == "__main__":
    main()
