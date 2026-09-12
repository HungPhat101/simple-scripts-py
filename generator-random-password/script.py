'''
version: 1.1
This script helps to generate random password quickly
1. Choose option uppercase include in the password
2. Choose option punctuation include in the password
'''

import random
import sys
import string
from datetime import datetime, timezone

characters = string.ascii_letters 

uppercase_option = input("Include uppercase for password (Yes/No): ")
is_uppercase = True

if uppercase_option == "Yes":
    is_uppercase = True
elif uppercase_option == "No":
    is_uppercase = False
else:
    print("Please select Yes or No")

if uppercase_option == True:
    characters += string.digits
else:
    sys.exit()

punctuation_option = input("Include special char for password (Yes/No): ")
is_punctuation = False

if uppercase_option == "Yes":
    is_punctuation = True
elif uppercase_option == "No":
    is_punctuation = False
else:
    print("Please select Yes or No")

if uppercase_option == True:
    characters += string.punctuation
else:
    sys.exit()


length = int(input("Input length of password: "))

characters = string.ascii_letters + string.digits + string.punctuation

random_password = '' . join(random.choices(characters, k=length))

now = datetime.now(timezone.utc)

with open("password.txt", "a", encoding="utf-8") as file:
    content = file.write(f"{now}: Password generate: \"{random_password}\" \n")

print("New password generate: ",random_password)
