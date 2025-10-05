# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Runtime error, " " should be added to define string
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a" + " " + animal + "." + " " + "It is a" + " " + animal_type + " " + "and it has" + " " + str(number_of_teeth) + " " + "teeth"  # Logical error, output is not what is expected, Wrong parenthesis, variables swapped, int to string

print(full_spec) # Syntax error - add brackets to fix - missing parentheses is invalid output for printing

