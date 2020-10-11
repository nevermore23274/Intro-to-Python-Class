"""
Tyler Wilson ***05OCT2020***
BMI Calculator
- Preselected 6 names
- Using for loop:
    + Include name of person for info
    + Height in inches
    + Weight in pounds
    + Call function that accepts height and weight as parameters, returns BMI
        + weight * 703 / height^2
        + Append BMI to list
        + Use second loop to judge each element from BMI list as:
            + Underweight = < 20
            + Normal = 20 - 25
            + Overweight = > 25
"""

# Define lists and variables
uList = ['Chase P.', 'Tyler W.', 'Brad V.', 'Marcellino M.', 'Andrew R.', 'Jaramie W.'] # Preset users list
uWeight = [] # User input for weight
uHeight = [] # User input for height
calcList = [] # List for BMI Calculation
choice = ' ' # set initial menu value

# Create callable functions for modularity
# Encompassing BMI Calculation function
def bmiFunc():

    # Ask for heigh and weight for each element in uList, append user input to uWeight and uHeight
    for i in range(len(uList)):
        inWeight = float(input("What is the weight of " + str(uList[i]) + "? "))
        uWeight.append(inWeight)
        #print(uWeight) # for testing
        
        inHeight = float(input("What is the height of " + str(uList[i]) + "? "))
        uHeight.append(inHeight)
        #print(uHeight) # for testing
        
        # The actual BMI calculation
        bmiCalc = float(round(uWeight[i] * 703 / (uHeight[i] ** 2), 2)) # Rounded the float to saved that nasty exponent
        #print(uHeight[i]) # for testing
        calcList.append(bmiCalc)
        print("The BMI of " + uList[i] + " is " + str(calcList[i]))

        # Function for weight calculation assessment
        def bmiCatch():
            if calcList[i] < 20:
                print("User " + uList[i] + " is underweight.")
                print("\n")

            elif calcList[i] == 20 or calcList[i] <= 25:
                print("User " + uList[i] + " is a normal weight.")
                print("\n")

            elif calcList[i] > 25:
                print("User " + uList[i] + " is overweight.")
                print("\n")

        bmiCatch()

# Set intial "Welcome" message...To be "friendly"
print("\nWelcome to my final project. It only calculates BMI, but I could slap in the functions from other programs I've made.")

while choice != 'q' or choice != 'Q': # Start loop until user enters "q" or "Q"
    # Give user choices
    print("\n---Main Menu---")
    print("\n[1] BMI Calculator")
    print("[2] Enter q to quit")
    
    choice = str(input("\nWhat would you like to do? ")) # Take users input for the choice
    
    # Responses for menu input
    if choice == '1':
        # Clear lists before reloop, begin passFunction()
        uWeight.clear()
        uHeight.clear()
        calcList.clear()
        print("\n")
        bmiFunc()
    elif choice == 'q' or choice == 'Q':
        print("\nMany whelps. Bye.")
        break
    else:
        print("\nEnter valid input, ya dunce.\n") # Because nobody loves you
