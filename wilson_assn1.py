# 1) Take users input of hours worked and total sales (for the week)
# 2) Hourly Pay is hard set - 7.25
# 3) Commisson percentage is hard set - 5% (0.05f)
# *) commPay = sales x comission percentage
# *) totPay = (number of hours x hourly rate) + commission

# Enter values
hrRate = 7.25
comm = 0.05
hours = eval(input("Enter hours worked: "))
sales = eval(input("Enter sales for the week: "))

# Compute commissions
commPay = sales * comm

# Compute pay
totPay = (hours * hrRate) + commPay
print ("Total Pay: ", format(totPay, ",.2f"))
