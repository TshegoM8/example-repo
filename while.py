len = 0
total = 0
# Asks user to enter numbers except 0
while True:
    user_number = int(input("enter a number but not 0: "))
    # To break loop when -1 is entered
    if user_number == -1:
        break 
    # Here we exclude the numbers 0 and -1 to calculate average
    if user_number == -1 or user_number == 0:
        continue
    total += user_number
    len += 1
if len > 0:
    average = total/len
    print(average)

   
   
   
# References
# https://stackoverflow.com/questions/67897455/how-do-i-write-a-for-loop-in-python-to-repeatedly-ask-the-user-to-enter-a-number
# https://stackoverflow.com/questions/74296057/why-does-my-program-to-calculate-the-average-of-numbers-entered-into-a-while-loo