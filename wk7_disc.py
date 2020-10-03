"""
*** Wilson, Tyler 29SEP2020 ***
- Array (list) that's values are input from user
- Modify each element of array (list) using a loop
- Display end result of loop
"""

# Imports
import re
import random

# Creating empty lists and flag variable
uiSymbols = [] # User Input for Symbols
uiNumbers = [] # User Input for Numbers
uiUpperCL = [] # User Input for Uppercase Letters
uiLowerCL = [] # User Input for Lowercase Letters
charList = [] # List compiled from user input lists
flag = 0 # Flag boolean for testing password requirements
choice = '' # Set initial menu value

# Define functions
# Password Generator Function
def passFunction():
    
        # Symbols Function
        def symbFunction():

            # Number of Symbol elements the user wants
            n_Symbols = int(input("How many symbols would you like your password to have? (must be 2 or more): "))

            # Check if user's input is longer than 2 symbols
            if n_Symbols < 2:
                print("Not enough characters, please input 2 or more symbols.\n")
                return symbFunction() # Returns user to start of function
        
            # Iterating until the range
            for i in range(0, n_Symbols):
                eleNumSym = str(input())
                
                symCheck = re.compile('[@_!#$%^&*()<>?/\|}{~:;]') # Make list of possible symbols for check

                if(symCheck.search(eleNumSym) != None): # Run a search on user input to ensure it's a symbol
                    uiSymbols.append(eleNumSym) # Adding elements to uiSymbols
                    print(uiSymbols) # for testing, prints each element
                else:
                    print("Not a valid symbol, enter in an actual symbol.")
                    uiSymbols.clear() # Clears out any values from the list before starting function over
                    return symbFunction() # Returns to start of function due to invalid input

        # Numbers Function
        def numFunction():
            # Number of Number elements the user wants
            n_Numbers = int(input("How many numbers would you like your password to have? (must be 2 or more): "))

            # Check that user's input is longer than 2 numbers
            if n_Numbers < 2:
                    print("Not enough numbers, please input 2 or more numbers.\n")
                    return numFunction() # Returns user to start of function

            # Iterating until the range
            for i in range(0, n_Numbers):
                eleNumNum = str(input())
                
                numCheck = re.compile('[0-9]') # Make list of possible numbers for check
                
                if(numCheck.search(eleNumNum) != None): # Run a search on user input to ensure it's a number
                    uiNumbers.append(eleNumNum) # Adding elements to uiNumbers
                    print(uiNumbers) # for testing, prints each element
                else:
                    print("Not a valid number, enter in an actual number.")
                    uiNumbers.clear() # Clears out any values from the list before starting function over
                    return numFunction() # Returns to start of function due to invalid input

        # Uppercase Letters Function
        def uletterFunction():
            # Number of Uppercase Letter elements the user wants
            n_UpperCL = int(input("How many uppercase letters would you like your password to have? (must be 2 or more): "))

            # Check that user has input more than 2 uppercase letters
            if n_UpperCL < 2:
                    print("Not enough uppercase letters, please input 2 or more uppercase letters.\n")
                    return uletterFunction() # Returns user to start of function

            # Iterating until the range
            for i in range(0, n_UpperCL):
                eleUpper = str(input())
                
                uclCheck = re.compile('[A-Z]') # Make list of possible uppercase letters for check
                
                if(uclCheck.search(eleUpper) != None): # Run a search on user input to ensure it's an uppercase letter
                    uiUpperCL.append(eleUpper) # Adding elements to uiUpperCL
                    print(uiUpperCL) # for testing, prints each element
                else:
                    print("Not a valid letter, enter in an actual uppercase letter.")
                    uiUpperCL.clear() # Clears out any values from the list before starting function over
                    return uletterFunction() # Returns to start of function due to invalid input

        # Lowercase Letters Function
        def lletterFunction():
            # Number of Lowercase Letter elements the user wants
            n_LowerCL = int(input("How many lowercase letters would you like your password to have? (must be 2 or more): "))

            # Check that user has input 2 or more lowercase letters
            if n_LowerCL < 2:
                    print("Not enough lowercase letters, please input 2 or more lowercase letters.\n")
                    return lletterFunction() # Returns user to start of function

            # Iterating until the range
            for i in range(0, n_LowerCL):
                eleLower = str(input())
                
                lclCheck = re.compile('[a-z]') # Make list of possible lowercase letters for check
                
                if(lclCheck.search(eleLower) != None): # Run a search on user input to ensure it's a lowercase letter
                    uiLowerCL.append(eleLower) # Adding elements to uiLowerCL
                    print(uiLowerCL) # for testing, prints each element
                else:
                    print("Not a valid letter, enter in an actual lowercase letter.")
                    uiLowerCL.clear() # Clears out any values from the list before starting function over
                    return lletterFunction() # Returns to start of function due to invalid input
                
        # Password Generator Function
        def passGenFunction():
            
            # Append main password list with lists user input
            charList.extend(uiSymbols)
            charList.extend(uiNumbers)
            charList.extend(uiUpperCL)
            charList.extend(uiLowerCL)
            print(charList) # for testing, prints elements
            
            # Accept user input for how many passwords they'd like
            times = input("How many passwords would you like?: ")
            times = int(times)
                
            # Take user input regarding how many characters they'd like their password(s) to have
            length = input("How many characters would you like your password(s) to have? (Must be at least 8): ")
            print("\n")
            length = int(length)
            
            def passCheck():
                
                for i in range(times):
                    password = ''
                    for x in range(length):
                        # Randomize password from charList()
                        password += random.choice(charList)
                        # Cut password in half
                        lenPasswd = len(password)
                        firstLen = round(lenPasswd / 2)
                        # Set first and second half of the password
                        firstHalf = password[0:firstLen]
                        secHalf = password[firstLen:]
                        # Reverse first and second half of password for a tiny bit more complexity
                        password = secHalf + firstHalf
                    
                    while True:
                        # Check length of 8 requirement
                        if(len(password)<8):
                            flag = -1
                            print("Must be more than 8 characters.")
                        # Check for lowercase letters
                        elif not re.search('[a-z]', password):
                            flag = -1
                            print("Must have lowercase letters.")
                        # Check for uppercase letters
                        elif not re.search('[A-Z]', password):
                            flag = -1
                            print("Must have uppercase letters.")
                        # Check for integers
                        elif not re.search('[0-9]', password):
                            flag = -1
                            print("Must have integers.")
                        # Check for special characters
                        elif not re.search('[@_!#$%^&*()<>?/\|}{~:;]', password):
                            flag = -1
                            print("Must have special character(s).")
                        else:
                            flag = 0
                            print("This is a valid password: ")
                            print("Your password is " + password + "\n")
                            break
                        
                        if flag == -1:
                            print("Not a valid password:")
                            print(password + "\n")
                            return passCheck()
            passCheck()
        
        symbFunction()
        numFunction()
        uletterFunction()
        lletterFunction()
        passGenFunction()
    
# Set intial "Welcome" message...To be "friendly"
print("\nWelcome to my final discussion post project. It only makes passwords for now but...Eventually.....")

while choice != 'q' or choice != 'Q': # Start loop until user enters "q" or "Q"
    # Give user choices
    print("\n---Main Menu---")
    print("\n[1] Create a password")
    print("[2] Enter q to quit")
    
    choice = str(input("\nWhat would you like to do? ")) # Take users input for the choice
    
    # Responses for menu input
    if choice == '1':
        # Clear lists before reloop, begin passFunction()
        uiSymbols.clear()
        uiNumbers.clear()
        uiUpperCL.clear()
        uiLowerCL.clear()
        passFunction()
    elif choice == 'q' or choice == 'Q':
        print("\nThis was far too much effort for a discussion post, I hate everything. Bye.")
        break
    else:
        print("\nEnter valid input, ya dunce.\n") # Because nobody loves you
