import math 
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
# user to to choose between investment or bond
Finance_calculator = input("enter either 'investment' or 'bond' from the menu above to proceed: ")
# if user entered investment calculate amount

if Finance_calculator.lower()=='investment':
    # user requested to enter relevant inputs
    deposit_amount = float(input("Enter the amount you are depositing: "))
    interest_rate = float(input("Enter the interest rate: "))
    interest_rate2 = interest_rate/100
    investment_years = int(input("Enter the number of years you plan to invest: "))
    interest = input("Do you want 'simple' or 'compound': ")
    if interest == 'simple':
       total_amount  = deposit_amount*(1 + interest_rate2*investment_years)
       print("Total amount: ", total_amount)
    if interest == 'compound':
       amount = deposit_amount*math.pow((1 + interest_rate2),investment_years)
       print("Total amount: ", amount)
    
    # if user entered bond to calculate
elif Finance_calculator.lower() =='bond':
    present_value = float(input("Enter present value of the house: "))
    monthly_interest = float(input("Enter the monthly interest: "))
    number_months = int(input("Enter the number of months over which the bond will be repaid: "))
    monthly_interest2 = monthly_interest/100
    monthly_interest3 = monthly_interest2/12
    repayment = (monthly_interest3*present_value)/(1-(1 + monthly_interest3)**(-number_months))
    print("Total amount:", repayment)

else: 
    print("ERROR")



    # references
    # Youtube tutorials 
    # https://pythongeeks.org/python-compound-interest-calculator/
    


             





