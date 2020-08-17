# 1) Prompt user for their age (age) and if the movie is 3D (moveType)
# 2) Children and seniors get a discount
# 3) 3D movies have surcharge; sur = $4.00 (4.00f)
# 4) Cutoff age for children = 3 - 11 years old (under 3 are free); chiPrice = $6.00 (6.00f) and >3 = $0.00 (0.00f)
# 5) Cutoff age for seniors = 60+; senPrice = $5.00 (5.00f)
# 5) Tickets price is based off age and if the movie is in 3D
# *) ticPrice = based off of age input
# *) totPrice = age + sur

# Enter set values and receive user input
chiPrice = 6.00
senPrice = 5.00
surcharge = 0.00
age = 0.00
age = eval(input("Please enter your age: "))
movType = input("Is this movie 3D?: ")

# Determine age and movie type
if age < 3 or age > 145:
    print ("Out of age group.")
    quit()
elif age >= 3 and age <= 11:
    ticPrice = chiPrice
elif age >= 12 and age <= 59:
    ticPrice = 10.00
elif age >= 60:
    ticPrice = senPrice
if movType == "yes" or movType == "Yes":
    surcharge = 4.00
elif movType == "no" or movType == "No":
    surcharge = 0.00

# Compute ticket cost
totPrice = ticPrice + surcharge
print ("Ticket Cost: ", totPrice)
