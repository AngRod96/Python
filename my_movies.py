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