import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = '!@#$%^&*()_+=-[]{}|:;<>,.?/~'

    # Create a pool of characters based on complexity level
    complexity_level = input("Enter complexity level (low/medium/high): ").lower()
    if complexity_level == "low":
        char_pool = lower_chars + digits
    elif complexity_level == "medium":
        char_pool = lower_chars + upper_chars + digits
    elif complexity_level == "high":
        char_pool = lower_chars + upper_chars + digits + special_chars
    else:
        print("Invalid complexity level. Using medium complexity.")
        char_pool = lower_chars + upper_chars + digits

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()

