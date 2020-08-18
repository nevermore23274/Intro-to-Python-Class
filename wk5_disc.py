"""
1) User supplies iterations
2) List outputed each iteration
3) Use while loop to verify if input is int, float or neither
"""

# Initialize list
u_list = []

# Take users input of the amount of elements for list
list_num = int(input("Enter number of elements: "))
print("\n")

# Set the range of list equal to users input
for i in range(0, list_num):
    while True:
        value = input("Enter a number: ")
        # Evaluate if value is integer
        try:
            value = int(value)
            print("Value is an integer.\n")
        except ValueError:
            # Evaluate if value is float, if it failed int evaluation
            try:
                value = float(value)
                print("Value is a float.\n")
            # Print if prior evaluations failed, print such, continue to next evaluation which returns to top of loop
            except ValueError:
                print("The value is neither an int nor a float.\n")
                continue
        break
    
    # Append list with verified value
    u_list.append(value)

# Print final list
print("\nYour list is: ", u_list)
