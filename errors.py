# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Compilation error, brackets and not putting them in is not valid and both print must be in line
print ("\n") 

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str =  24 # Runtime error using == instead of = to define a variable is incorrect, Compilation error line 9 - 11 must be in line with line 5-6, cannot add str and int
print("I'm" + " " +  str(age_Str) + " " + "years old.") # Syntax error - a
dd spacing and convert int to string

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 # Compilation error lines must be in lie
total_years = age_Str + years_from_now # Runtime error, adding a string and integer is not valid - solution remove string indicators

print ("The total number of years: " + str(total_years)) # Runtime error -  close brackets, total_years instead of answer_years and is integer not string convert to string

# Variable to calculate the total number of months from the given number of years and printing the result
months = 6 # Compilation error - add months variable because it is added on the print statement for final answer
total_months = (total_years*12) + 6  # Syntax error - total to total_years, logical error for correct calculation
print ("In 3 years and 6 months, I'll be " +str(total_months) + " " + "months old") #close brackets, total_months instead of months old and not a string

#HINT, 330 months is the correct answer

