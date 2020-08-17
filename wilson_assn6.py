"""
1) Read users inputs for 10 days
2) Store days in array
3) Display array
4) Convert from Celsius to Fahrenheit
5) Display converted array
6) Give number of cool, warm, and hot days.
    - Cool = 45 or less
    - Warm = 46 - 65
    - Hot  = 66 or more
*) Far = (Cel x 1.8) + 32
"""

# Set variables and array
cntCool = 0
cntWarm = 0
cntHot = 0

intCTemp = (5)
intFTemp = 0
celTemp = []
fahTemp = []

for x in range(intCTemp):
    cnt = 1 + x
    print("Input celsius temperature for day " + str(cnt))
    inputName = input()
    intCTemp = inputName
    intFTemp = (int(inputName)*1.8)+32

    if intFTemp < 45:
        cntCool = 1 + cntCool
    elif intFTemp > 45 and intFTemp < 65:
        cntWarm = 1 + cntWarm
    elif intFTemp > 65:
        cntHot = 1 + cntHot

    celTemp.append(int(intCTemp))
    fahTemp.append(intFTemp)

print(celTemp)
print(fahTemp)
print("There are " + str(cntCool) + " cool days.")
print("There are " + str(cntWarm) + " warm days.")
print("There are " + str(cntHot) + " hot days.")
