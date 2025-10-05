#ask user to enter triathlon times and print out the total output
swimming = int(input("enter swimming time in minutes: " )) 
cycling = int(input("enter cycling time in minutes: "))
running = int(input("enter running time in miutes: "))
triathlon = int((swimming+cycling+running))
Sentence = "Total time taken for the traithlon:"
time = "minutes"
print(Sentence,triathlon,time)
#now rewrads user for time range quallified with an award
if (triathlon==0): 
    print("Award: Provincial colours.")
elif (triathlon<=100):
    print("Award: Provincial colours.")
elif (triathlon >= 101) and (triathlon <=105):
    print("Award: Provincial half colours.")
elif (triathlon>=106) and (triathlon<=110):
    print("Award: Provincial scroll.")
elif triathlon>=111:
    print("Award: No award.")

