import string

password = input("Please enter a password to be checked, it will be reviewed: Very bad, Bad, Ok, Good, Very Good: ")

# Checks
contains_number = any(char.isdigit() for char in password)
contains_lowercase = any(char.islower() for char in password)
contains_uppercase = any(char.isupper() for char in password)
contains_special = any(char in string.punctuation for char in password)
contains_letter = any(char.isalpha() for char in password)

# Points system
points = 0
advice = ""

if len(password) >= 8:
    points += 1
if contains_number:
    points += 1
if contains_lowercase:
    points += 1
if contains_uppercase:
    points += 1
if contains_special:
    points += 1
if contains_letter:
    points += 1

#advice
if len(password) < 8:
    advice += "Make your password 8 or more characters. "
if contains_number == False:
    advice += "Add a number to your password. "
if contains_lowercase == False:
    advice += "Add a lowercase letter. "
if contains_uppercase == False:
    advice += "Add an upercase letter. "
if contains_special == False:
    advice += "Add a special character(e.g &,$,?) "
if contains_letter == False:
    advice += ""

# Rating
if points == 0:
    print("Very Bad")
    print(advice)
elif 1 <= points <= 2:
    print("Bad")
    print(advice)
elif points == 3:
    print("Ok")
    print(advice)
elif 4 <= points <= 5:
    print("Good")
    print(advice)
else:
    print("Very Good")
