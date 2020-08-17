"""
1) Prompt user for one number
2) Promt user for second number
3) Add numbers
4) Display the sum with sarcastic happiness
"""

int_1 = 0.0
int_2 = 0.0

print('First Number: ')
int_1 = eval(input())
print('Second Number: ')
int_2 = eval(input())

sum_3 = int_1 + int_2
print('The sum of your numbers is: ' + str(sum_3) + ', congrats on passing 1st grade.')
