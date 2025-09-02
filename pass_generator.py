#1)collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

#2)get all available characters
#3) randomly pick characters upto length
#4) ensure we have at least one of each character type
#5) ensure length is valid

import string
import random
def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password Length should be at least 4 characters.")
        return
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits
    

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    remainig_length = length - len(required_characters)
    password = required_characters
    for _ in range(remainig_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)


    
