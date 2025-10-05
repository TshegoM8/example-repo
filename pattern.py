# Describe the pattern to be created
pattern = "arrow"
asterisks = input("Enter a star sign to create a pattern: ")
if asterisks == "*":
     print("*")
# Using for loop with if else to output the pattern
     for pattern in asterisks: 
        print("**")
     for pattern in asterisks: 
        print("***")
     for pattern in asterisks: 
        print("****")
     for pattern in asterisks: 
        print("*****")
     for pattern in asterisks: 
        print("****")
     for pattern in asterisks: 
        print("***")
     for pattern in asterisks: 
        print("**")
     for pattern in asterisks: 
        print("*")

else:
    print("Cannot create pattern.")