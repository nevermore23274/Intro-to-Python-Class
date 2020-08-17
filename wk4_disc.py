"""
1) Ask user for 2 values
2) Begin counting variable at 1
3) Place values in list
3) Sum all values, integer and/or float
"""

# Import math library
import math

# Define list and amount of variables in list
listAmount = (2)
numList = []

# Begin counting for values, accept user input
for x in range(listAmount):
    cnt = 1 + x
    print("Please input value " + str(cnt) + ":")
    inputName = eval(input())
    listAmount = inputName

    # Place user input in list
    numList.append(listAmount)

# Print summation of list
print(math.fsum(numList))
