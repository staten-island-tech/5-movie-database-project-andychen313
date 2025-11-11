import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#File One

""" def titles(data):
    for d in data:
        print(d["title"])
titles(data) """

#File Two

""" def after_year(data):
    years = [int(d["year"]) for d in data]
    year = input("Give me a year and I will print all movies released after that year: ")
    while not year.isnumeric() or int(year) not in years:
        print("Invalid year. Please enter an appropriate year that accomodates the movie.")
        year = int(input("Please enter an appropriate year that accomodates with the movie: "))
    year = int(year)
    for d in data:
        if int(d["year"]) > year:
            print(f"{d['title']} ({d['year']})")
after_year(data) """

#File Three

""" def before_and_after_year(data):
    years = [int(d["year"]) for d in data]
    year_start = input("Enter the year you want your movies to be released after: ")
    year_end = input("Enter the year you want your movies to be released before: ")
    while (not year_start.isnumeric() or not year_end.isnumeric()) or (int(year_start) not in years or int(year_end) not in years):
        print("Invalid year(s). Please enter an appropriate year that accomodates the movie.")
        year_start = input("Enter the year you want your movies to be released after: ")
        year_end = input("Enter the year you want your movies to be released before: ")
    year_start = int(year_start)
    year_end = int(year_end)
    matching_movies = [d for d in data if year_start < int(d["year"]) < year_end]
    if matching_movies:
        for d in matching_movies:
            print(f"{d['title']} ({d['year']})")
    else:
        print("No movies found.")
before_and_after_year(data)
 """
def before_and_after_year(data):
    years = [int(d["year"]) for d in data]
    
    year_start = input("Enter the year you wnat your movies to be released after: ")
    year_end = input("Enter the year you want your movies to be released before: ")

    while True:
        if not (year_start.isnumeric() and year_end.isnumeric()):
            print("Invalid year(s). Please enter appropriate years.")
        elif int(year_start) not in years or int(year_end) not in years:
            print("Invalid year(s). Please enter appropriate years.")
        else:
            break

        year_start = input("Enter the year you want your movies to be released after: ")
        year_end = input("Enter the year you want your movies to be released before: ")

    year_start = int(year_start)
    year_end = int(year_end)

    matching_movies = [d for d in data if year_start < int(d["year"]) < year_end]
    
    if matching_movies:
        for d in matching_movies:
            print(f"{d['title']} ({d['year']})")
    else:
        print("No movies found.")
before_and_after_year(data)
#File Four

""" def during_year(data):
    year = int(input("Give me a year and I will print all movies that were released in that year: "))
    for d in data:
        if d["year"] == year:
            print(f'{d["title"]} ({d["year"]})')
during_year(data)
 """
#File Five

""" def search_movies():
    search = input("What movie are you trying to find?: ").lower()
    movie_results = [d for d in data if search in d["title"].lower()]
    print(movie_results)
search_movies() """

#File Six

""" def genre_search():
    search = input("What genre of movies are you trying to find?: ").lower()
    movie_results = [d for d in data if any(search in g.lower() for g in d["genres"])]
    print(movie_results)
genre_search() """

#Practice

""" def titles(data):
    for d in data:
        print(d["title"])
titles(data) """

""" def after_year(data):
    year = int(input("Give me a year and I will print movies released after that year: "))
    for d in data:
        if (d["year"]) > year:
            print(f'{d["title"]} ({d["year"]})')
after_year(data) """

""" def after_year(data):
    year = int(input("Give me a year and I will print all movies released after that year: "))
    for d in data:
        if int(d["year"]) > year:
            print(f'{d["title"]} ({d["year"]})')
after_year(data) """

