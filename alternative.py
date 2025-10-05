string = input("Enter a string") # Ask user to enter a string 
user_string = " " # Empty the string
for index in range(len(string)): # Now check the letters in the string and change from lower to upper case and vice versa 
       if index % 2 == 0:
        user_string += string[index].upper()
       else:
        user_string += string[index].lower()
        continue # continue for words to change from lower to upper and vice versa
new_words = string.split()      
user_string2 = []
for index in range(len(new_words)):
   if index % 2 == 0:
      user_string2.append(new_words[index].upper())
   else:
      user_string2.append(new_words[index].lower())
output = ' '.join(user_string2)

print(user_string)
print(output)

# References
# https://www.youtube.com/shorts/crwBnEFnt6Q?t=4&feature=share
# https://www.youtube.com/shorts/F5zZFv9Dxf8?feature=share
# https://youtu.be/h8a1dwF2OrQ
