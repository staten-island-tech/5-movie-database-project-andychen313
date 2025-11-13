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

    year_start = int(input("Enter the year you want your movies to be released after: "))
    year_end = int(input("Enter the year you want your movies to be released before: "))

    if year_start not in years or year_end not in years:
        print("Please enter appropriate years.")
        return
    
    for d in data:
        year = int(d["year"])
        if year_start < year < year_end:
            print(f"{d['title']} ({d['year']})")
before_and_after_year(data) """

#File Four

""" def during_year(data):
    years = [int(d['year']) for d in data]
    user_year = (input("Enter a year and I will print all movies that were released in that year: "))
    user_year = int(user_year)
    if user_year not in years:
        print("Please enter appropriate years.")
        return
    
    for d in data:
        movie_year = int(d["year"])
        if movie_year == user_year:
            print(f"{d['title']} ({d['year']})")
during_year(data) """

#File Five

""" def search_movies():
    search = input("What movie are you trying to find?: ").lower()
    found = False
    
    for d in data:
        title = d["title"].lower()

        if search in title:
            print(f"{d['title']} ({d['year']})")
            found = True
    if not found:
        print("Please try again, but be more specific.")
search_movies() """

#File Six

""" def genre_search():
    search = input("What genre(s) of movies are you trying to find?: ").lower()
    found = False

    for d in data:
        for g in d['genres']:
            if search in g.lower():
                print(f"{d['title']} ({d['year']}) - {d['genres']}")
                found = True
    if not found:
        print("Please try again, but be more specific.")
genre_search() """