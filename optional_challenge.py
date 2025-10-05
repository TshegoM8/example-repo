print "Hi, I hear you started the Data science boot camp"  # Syntax error - missing parentheses invalid language
Print("before we begin, I just know that you are going to be great Data scientist one day!")  # Syntax error, Capital P is different from p
time = int(input("How long is the boot camp in months: "))
programme_type  = online # Runtime error, online is expected to be in quotes 
start = input("when did you start: ") 
print("The boot camp is for" + " " + str(start) + " " + " " + "months, " + " " + programme_type + " " +  "and I started on the" + " " +  str(time)) # Logical error, the output is not what was intended but still runs; months should come before start time to correlate with the sentence