with open("DOB.txt", "r") as file:
    lines = file.readlines()

    names = []
    date_births = []
    for line in lines: 
        values  = line.strip().split()
        if len(values) >= 4:
            name = " ".join(values[:-3])
            date_birth = " ".join(values[-3:])
        names.append(name)
        date_births.append(date_birth)
        print("name")
        for name in names:
            print(name)

        print("\ndate_birth")
        for birth in date_births:
            print(birth)
    
    #date_births = []
    #for line in lines:
     #   values  = line.strip().split()
      #  if len(values) >= 4:
       #     date_birth = " ".join(values[:-3])
       # date_births.append(date_birth)
        #print("\ndate_birth")
        #for date_birth in date_births:
         #   print(date_birth)

       # date_birth = []
    #for line in file:
     #   values = line.split("/n")
      #  date_birth.append(values[0])
       # print(date_birth)


