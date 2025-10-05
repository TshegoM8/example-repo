 # Initialise total sum to 0
total_sum = 0
# Start with the first even integer
even_integer = 2
# Loop until the total sum exceeds 250
while total_sum <= 250:
# Add the current even integer to the total sum
    total_sum += even_integer
# Move to the next even integer
even_integer += 2
# Print the current total sum
print(total_sum)