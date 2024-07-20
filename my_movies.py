favorite_movies = []

def add_movie(movie): 
    favorite_movies.append(movie)
    print(f"Movie `{movie}` added.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed")
    else:
        print(f"Movie '{movie}' was not found.")

def display_movies():
    print("Movie List:")
    for movie in favorite_movies:
        print(f" {movie}")

def count_movies():
    print(len(favorite_movies))

def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie '{movie}' was found ")
    else:
        print(f"Movie '{movie}' was not found")

def clear_movies():
    favorite_movies.clear()
    print("the movie list has been cleared")


phonebook = {}

#Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added with number {number}.")

#Function to remove a contact
def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' was removed.")
    else:
        print(f"Contact '{name}' was not found.")

#Function to display all contacts
def display_contacts():
    print("Phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

#Adding contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")

#display Contacts
display_contacts()

#remove a contact
remove_contact("Alice")

display_contacts()

print(phonebook)
