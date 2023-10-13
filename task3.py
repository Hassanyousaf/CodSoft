import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    else:
        print("Invalid complexity level. Please choose low, medium, or high.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("===== PASSWORD GENERATOR =====")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ")

    password = generate_password(length, complexity)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
