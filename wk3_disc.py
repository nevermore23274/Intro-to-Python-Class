"""
1) Ask for first integer
2) Ask for second integer
3) Ask for third integer
4) Add values together, state if output is odd or even
"""
# Collect user input
num1 = int(input('Please enter first integer: '))
num2 = int(input('Please enter second integer: '))
num3 = int(input('Please enter third integer: '))

# Computation
numTot = num1 + num2 + num3

# Print sum, check if sum is odd or even
print("Your total is:", numTot)
if (numTot % 2) == 0:
    print("{0} is an even number.".format(numTot))
else:
    print("{0} is an odd number.".format(numTot))


