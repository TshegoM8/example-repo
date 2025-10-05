def calculation():
   try:
      number = input("enter number: ")
      number2 = input("enter another number: ")
   except ValueError:
      print("incorrect number, pleas enter again")
      return
   operation = input("enter a math sign: ")
   if operation ==  '+':
      answer = number + number2
   elif operation == '-':
       answer = number - number2
   elif operation == '*':
        answer = number * number2
   elif operation == '/':
        answer = number / number2
   else:
       print("invalid entry")
   equation = number + " " + operation + number2 + " = " + answer
   print(equation)
   try: 
    with open('equations.txt', 'a') as file:  
      file.write( equation + "\n")
   except Exception as error:
    print("Can't save to file")

   
    

     