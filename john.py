# Store the names
incorrect_names = []

while True :
    # Ask user for names 
    name = str(input("enter your name: "))
    # If John is entered go to print the incorrect names entered
    if name.strip().lower() == "john" :
     break
    else:
       incorrect_names.append(name)
   
 #names.remove("John")
print("names: ", incorrect_names)