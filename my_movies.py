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


student_grades = {}

#Adding students and grades 
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' was added with grade {grade}")

#Removing student from dictionary
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Contact '{name}' was removed")
    else:
        print(f"Contact '{name}' not found")

#Displaying students and grades 
def display_students():
    print("Students and Grades:")
    for name, grade in student_grades.items():
        print(f"{name}, {grade}")
##updating Students and grades 
def update_grade(name, grade):
    student_found = False

    for student in student_grades:
        if student ['name'] == name:
            student ['grade'] = grade
            student_found = True
            print(f"Updated {name}'s grade to {grade}.")
            break
        if not student_found:
            print(f"Student {name} was not found.")

#testing function for updating students and their grades
update_grade("Alice", 99)


#Adding Students 
student_grades("Taylor", 99)
student_grades("Patrick", 60)

#display students and grades
display_students()

#remove student
remove_student("Taylor")

#display Sutddents and grades again
display_students()