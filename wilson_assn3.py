"""
 1) Prompt user for height and width of room - roomH and roomW (in ft)
 2) Prompt user for quality of carpet - carpQual
   - carpH - High quality - $5.00/sqft
   - carpA - Average quality - $4.00/sqft
   - carpL - Low quality - $3.00/sqft
*) total_Cost =(height x width) x carpQual
"""

# Initialize carpet quality cost variable
carpQualc = 0.00

# Inputs
roomH = eval(input("Please enter the room height (in feet): "))
roomW = eval(input("Please enter the room width (in feet): "))
carpQual = input("Please enter carpet quality (High, Average, Low): ")

# Function
def carp_Cost(roomH,roomW,carpQual,carpQualc):
    if carpQual == "High" or carpQual == "high":
        carpQualc = 5.00
    elif carpQual == "Average" or carpQual == "average":
        carpQualc = 4.00
    elif carpQual == "Low" or carpQual == "low":
        carpQualc = 3.00
    total_Cost = (roomH * roomW) * carpQualc
    print("The cost to carpet this room will be: $", format(total_Cost, ",.2f"))


carp_Cost(roomH,roomW,carpQual,carpQualc)
