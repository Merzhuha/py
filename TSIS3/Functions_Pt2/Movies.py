movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Function to check if a movie's IMDB score is above 5.5
def above_5_5(movie):
    return movie["imdb"] > 5.5

# Function to filter movies with IMDB score above 5.5
def filter_above_5_5(movies):
    return list(filter(above_5_5, movies))

# Function to filter movies by category
def filter_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# Function to calculate average IMDB score of a list of movies
def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

# Function to calculate average IMDB score by category
def average_imdb_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb(category_movies)

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Check if a movie's IMDB score is above 5.5")
        print("2. Filter movies with IMDB score above 5.5")
        print("3. Filter movies by category")
        print("4. Calculate average IMDB score of all movies")
        print("5. Calculate average IMDB score by category")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            movie = {"name": input("Enter movie name: "), "imdb": float(input("Enter movie's IMDB score: ")), "category": input("Enter movie category: ")}
            print(above_5_5(movie))
        elif choice == '2':
            print(filter_above_5_5(movies))
        elif choice == '3':
            category = input("Enter category to filter movies: ")
            print(filter_by_category(movies, category))
        elif choice == '4':
            print("Average IMDB score of all movies:", average_imdb(movies))
        elif choice == '5':
            category = input("Enter category to calculate average IMDB score: ")
            print("Average IMDB score of category", category, ":", average_imdb_by_category(movies, category))
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
