import statistics
# Store numbers
floats =[]
# Ask user to enter 10 numbers 
for i in range(10):
 list_floats = float(input("enter number: "))
 floats.append(list_floats)
 # Now add the numbers up and print
total = sum(floats)
print(sum(floats))
# Get max number 
index_max = floats.index(max(floats))
print("The index max is : ",index_max)
# Get min number
index_min =floats.index(min(floats))
print("The index min is : ", index_min)
# Calculate mean and print
mean = statistics.mean(floats)
print(round(mean,2))
# Calculate median and print
median = statistics.median(floats)
print("The median is: ", median)


