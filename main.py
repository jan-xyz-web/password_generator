"""
Main entry point for the password generator application.
"""
import password_generator as PasswordGenerator

def main():
    password_settings = None  # Start with no settings
    
    while True:  # Loop forever until user exits
        print("\n=== Password Generator by Jan ===")
        print("1. Generate Password")
        print("2. Change Settings")
        print("3. Exit")
        print("--------------------------------")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # If no settings yet, ask for them
            if password_settings is None:
                password_settings = collect_password_settings()
            
            # Generate and show password
            password = PasswordGenerator.generate_password(password_settings)
            print(f"\nGenerated Password: {password}")
            
            # Inner loop for regeneration
            while True:
                regen = input("\nRegenerate? (y) | Change Settings (s) | Main Menu (m): ").lower()
                if regen == "y":
                    password = PasswordGenerator.generate_password(password_settings)
                    print(f"Generated Password: {password}")
                elif regen == "s":
                    password_settings = collect_password_settings()
                    password = PasswordGenerator.generate_password(password_settings)
                    print(f"Generated Password: {password}")
                elif regen == "m":
                    break  # Go back to main menu
                    
        elif choice == "2":
            password_settings = collect_password_settings()
            print("\nSettings updated!")
            
        elif choice == "3":
            print("Goodbye!")
            break  # Exit the program
        
        else:
            print("Invalid choice, please try again.")

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
