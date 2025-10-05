print("Hi, Letshego")
Salary = int(input("How much do you earn per month?: "))
commission = int(input(" And your commission: "))
total = Salary + commission * 12 # The code runs but outputs incorrect calculation : Correct would be (salary*12) + commission, annual salary is added with commission
print('I earn' + " " + "plus or minus "+ " " + str(total) +" " + "per annum")