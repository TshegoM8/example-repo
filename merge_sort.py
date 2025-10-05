def merge_sort_by_length(strings):
    if len(strings) <= 1:
        return strings

    middle = len(strings) // 2
    left_half = merge_sort_by_length(strings[:middle])
    right_half = merge_sort_by_length(strings[middle:])

    return merge_by_length(left_half, right_half)

# Merge two lists by string length
def merge_by_length(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add  the remaining items
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# List of birds
birds = ["blue waxbill", "blue crane", "owl", "Ostrich", "eagle", "dove","penguin", "pelican", "crane", "kite","vulture"]
sorted_birds = merge_sort_by_length(birds)
print("Sorted birds by length (longest to shortest):")
print(sorted_birds)
print()
# List of type of flowers 
flowers = ["rose", "lily", "sunflower", "tulip", "protea", "daisy", "bush lily" "iris","orchid","dahlia"]
sorted_flowers = merge_sort_by_length(flowers)
print("Sorted flowers by length (longest to shortest):")
print(sorted_flowers)
print()

# List of countries 
countries = ["Lesotho", "South Africa", "Nigeria", "Ghana", "Zambia", "Zimbabwe", "Germany", "France", "Brasil", "Namibia", "kenya"]
sorted_countries = merge_sort_by_length(countries)
print("Sorted countries by length (longest to shortest):")
print(countries)

# References 
# https://www.datacamp.com/tutorial/python-merge-sort-tutorial