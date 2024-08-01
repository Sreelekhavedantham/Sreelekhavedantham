import random
import string

def generate_password(length=12):
    """Generate a random password with a mix of letters, digits, and special characters."""
    
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
   
    all_characters = letters + digits + special_chars
    
    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),
    ]
    
   
    password += random.choices(all_characters, k=length - len(password))
    
    
    random.shuffle(password)
    
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()