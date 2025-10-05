students = int(input("how many students are registering: "))
file = open("reg_form.txt" , "w")
for i  in range(students):
    studentID = input("enter student's ID: ")
    file.write(studentID + "...........\n")

file.close()

print("attendance register")