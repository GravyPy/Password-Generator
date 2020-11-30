import string
import random
import time
import os
import os.path

# Defining All Possible Characters
chars = string.ascii_letters + string.punctuation  + string.digits

# Creates Empty Password Variable to Be Filled Later
password = ''

# Gathers User Input for Text File
passwordApp = input("What App is this Password for? ")
while True:
    try:
        passwordLength = int(input("How long do you want your password to be? (Enter a number) "))
        assert 8 <= passwordLength <= 32
    except ValueError:
        print("Please enter a number!")
    except AssertionError:
        print("Number must be between 8 & 32 characters")
    else:
        break

# Password Generation
print("Generating Password")
time.sleep(3)
# Gets Password Length and Assigns Amount of Chars based on length
for x in range(passwordLength):
    password += random.choice(chars)
print("Password Generated")
time.sleep(2)
print("Creating File")
# Creates File on Users Desktop to Store Passwords
passwordFile = open(os.path.expanduser(os.path.join('~/Desktop/Passwords.txt')), "a")
passwordFile.write(passwordApp + '\n' + password + '\n' + '\n')
time.sleep(2)
print("File Saved")
time.sleep(1.5)
# Thank You
print("Thank You For Using The GravyGen")
time.sleep(1.5)