# Class
class Album():
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
# Creating anew list called album1 and adding 5 album objects
albums1 = [Album("Jesus is King", "Joshua King", 6),
           Album("Amen Amen", "Octavia Lee", 12),
           Album("In His Presence", "Benjamin Dub", 10),
           Album("Love of God", "Maxwell Smith", 8),
           Album("Create in me a clean heart", "David", 24)]

# Now print albums1
print("albums1:")
for album in albums1:
    print(album)
# Sort the list according to the by number_of_songs
albums1.sort(key=lambda a: a.number_of_songs)
print("\nalbums1 sorted by number_of_songs:")
for album in albums1:
    print(album)
# Swap elements 
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nalbums1 after swapping first two albums:")
for album in albums1:
    print(album)

# Create a new list called albums2
albums2 = []

# Now add 5 albums to albums2 list
albums2.append(Album("Healer", "Lee Char", 14))
albums2.append(Album("Glory", "Beauty", 8))
albums2.append(Album("God in me", "Ash May", 10))
albums2.append(Album("Creator", "Joe Mel", 12))
albums2.append(Album("The blood", "Julie Angel", 15))

print("\nalbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2
for album in albums1:
    albums2.append(album)

# Now add "Dark Side of the Moon", "Pink Floyd", 9"  and "Oops!... I Did It Again", "Britney Spears", 16" albums to albums2
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# Sort  the albums2 alphabetically according to the album name by album_name
albums2.sort(key=lambda a: a.album_name)
print("\nalbums2 sorted by album_name:")
for album in albums2:
    print(album)

#  Search fo r the album "Dark Side of the Moon" in albums2
found_index = -1
for i in range(len(albums2)):
    if albums2[i].album_name == "Dark Side of the Moon":
        found_index = i
        break

print("\nIndex of 'Dark Side of the Moon' in albums2:", found_index)

# References 
# https://www.w3schools.com/python/python_lambda.asp