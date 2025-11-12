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
before_and_after_year(data) """

#File Four

""" def during_year(data):
    years = [int(d['year']) for d in data]
    year = input("Enter a year and I will print all movies that were released in that year: ")
    while True:
        if not year.isnumeric():
            print("Invalid year. Please enter an appropriate year that you want your movie(s) to accomodate.")
        elif int(year) not in years:
            print("Invalid year. Please enter an appropriate year that you want your movie(s) to accomodate.")
        else:
            break
        year = input("Enter a year and I will print all movies that were released in that year: ")
    year = int(year)

    matching_movies = [d for d in data if year == int(d["year"])]

    if matching_movies:
        for d in matching_movies:
            print(f'{d["title"]} ({d["year"]})')
    else:
        print("No movies found")
during_year(data) """

#File Five

""" def search_movies(title):
    results = []
    for d in data:
        if title.lower() in d["title"].lower():
            results.append(d)
    return results

search = input("What movie are you trying to find?: ").lower()
matches = search_movies(search)

if matches:
    for m in matches:
        print(f"{m['title']} ({m['year']}) - ({m['genres']})")
else:
    print("No movies found.") """

#File Six

""" def genre_search(genre):
    results = []
    for d in data:
        if any(genre.lower() in g.lower() for g in d["genres"]):
            results.append(d)
    return results
    
search = input("What genre of movies are you trying to find?: ").lower()
matches = genre_search(search)

if matches:
    for m in matches:
        print(f"{m['title']} ({m['year']}) - ({m['genres']})")
else:
    print("No movies found. Please try again using the full word(s) of the genres your looking for.") """

def genre_search():
    search = input("What genre of movies are you trying to find?: ").lower()
    if not search:
        print("Please enter a genre or genres.")
    for d in data:
        if search in d["genres"].lower():
            print(d['title'] (d['genres']))

