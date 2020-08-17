"""
1) Take user input of 5 students
2) Prompt user for quiz grade for each student
3) Compute and display average of the 5 grades, and display the highest
* classAvg = classGradeSum / studCnt
"""

# Set initial values
classGradeSum = 0
classAvg = 0
inputGrade = 0
topGrade = 0
strNames, intGrades = (6, 1)
dataList = []

# For loop to take in names and grades
for x in range(strNames):
    studCnt = 1 + x
    print("Input student name: ")
    inputName = input()
    strNames = [inputName]
    classGradeSum = classGradeSum + int(inputGrade)
    for y in range(intGrades):
        print("Input student grade value: ")
        inputGrade = input()
        if topGrade < int(inputGrade):
            topGrade = int(inputGrade)
        strNames.append(inputGrade)
    dataList.append(strNames)

# Compute the sum and average
classGradeSum = classGradeSum + int(inputGrade)

classAvg = classGradeSum / studCnt

# Print the average and highest Grade
print("The class average is: " + format(classAvg, ",.2f"))
print("The highest grade in the class is: " + str(topGrade))
