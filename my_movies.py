#PRACTICE
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

#PHONEBOOK APP

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

#LEARNING ABOUT DICTIONARIES
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

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 78},
    {"name": "Charlie", "grade": 92}
]

def average_grade():
    total_grades = 0
    for student in students:
        total_grades += student['grade']

        average = total_grades / len(students)

    print(f"The average grade is: {average}")
    
average_grade()



#LEARNING ABOUT SETS 
#STEP 1
def extract_unique_words(paragraph):
    # Split the paragraph into words and convert them to lowercase
    words = paragraph.lower().split()

    # Create a set to store unique words
    unique_words = set(words)

    return unique_words

# Example paragraph
paragraph1 = "Python is a great programming language. Python is popular and powerful."

# Extracting unique words
unique_words1 = extract_unique_words(paragraph1)
print("Unique words in paragraph 1:", unique_words1)

#STEP 2
def find_common_words(set1, set2):
    return set1.intersection(set2)

def find_unique_words(set1, set2):
    return set1.difference(set2)

# Example paragraphs
paragraph2 = "Python is widely used in data science. Data science is an exciting field."

# Extracting unique words from the second paragraph
unique_words2 = extract_unique_words(paragraph2)
print("Unique words in paragraph 2:", unique_words2)

# Finding common words
common_words = find_common_words(unique_words1, unique_words2)
print("Common words:", common_words)

# Finding words unique to the first paragraph
unique_to_paragraph1 = find_unique_words(unique_words1, unique_words2)
print("Words unique to paragraph 1:", unique_to_paragraph1)

#FINDING WORDS UNIQUE TO THE SECOND PARAGRAPH 
unique_to_paragraph2 = find_unique_words(unique_words2, unique_words1)
print("Words unique to paragraph 2:", unique_to_paragraph2)

#STEP 3 
def display_results(common, unique1, unique2):
    print("Comparison Results:")
    print("\nCommon Words:")
    for word in common:
        print(word)

    print("\nUnique Words in Paragraph 1:")
    for word in unique1:
        print(word)

    print("\nUnique Words in Paragraph 2:")
    for word in unique2:
        print(word)

# Displaying the comparison results
display_results(common_words, unique_to_paragraph1, unique_to_paragraph2)