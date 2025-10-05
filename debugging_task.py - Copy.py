# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # Change K to a key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = { # Fix indentation 
                "lisa": "BAAAAAART!", 
                "bart" : "Eat My Shorts!", 
                "marge": "Mmm~mmmmm", 
                "homer": "'d'oh!", # Semicolons added
                "maggie": "(Pacifier Suck)"
}

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # Add the square brackets to access the values in simpson_catch_phrases
'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

