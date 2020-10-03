"""
- Analyze a string, display result
- Must use string slice, string condition, or string method
"""

import random
import re
# Set variables
chars = '1234567890abcdefghijklmnopqrstuvwxyz!?.,-'
flag = 0
# Take user input regarding number of passwords wanted
times = input('How many passwords do you want? ')
times = int(times)
# Take user input regarding how many characters the user wants the password(s) to have
length = input('How many characters do you want your password(s) to have? (must be at least 12 characters)')
print('\n')
length = int(length)

for i in range(times):
    password = ''
    for x in range(length):
        # Randomize password with characters from 'chars' variable
        password += random.choice(chars)
        # Cut password in halves to set uppercase and lowercase
        len_passwd = len(password)
        first_len = round(len_passwd / 2)
        # First portion of password is set to lowercase
        first_half = password[0:first_len].lower()
        # Second portion of password is set to uppercase
        sec_half = password[first_len:].upper()
        # Combine both portions
        password = first_half + sec_half
        
    while True:
        # Check length
        if (len(password)<12):
            flag = -1
            print('Must be more than 12 characters.')
            break
        # Check for 1 lowercase
        elif not re.search('[a-z]', password):
            flag = -1
            print('No lowercase letters were used.')
            break
        # Check for 1 uppercase
        elif not re.search('[A-Z]', password):
            flag = -1
            print('No uppercase letters were used.')
            break
        # Check for at least 1 digit
        elif not re.search('[0-9]', password):
            flag = -1
            print('No numbers were used.')
            break
        # Check for at least 1 special character
        elif not re.search('[!?.,-]', password):
            flag = -1
            print('No special characters were used.')
            break
        # If none of the other checks failed, give users password
        else:
            flag = 0
            print('Valid password.')
            print(password)
            break
    if flag == -1:
        print('Not a valid password.')
        print(password)
