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
    year = int(input("Give me a year and I will print all movies released after that year: "))
    for d in data:
        if int(d["year"]) > year:
            print(f'{d["title"]} ({d["year"]})')
after_year(data) """

#File Three

""" def before_year(data):
    year = int(input("Give me a year and I will pritn all movies released before that year: "))
    for d in data:
        if int(d["year"]) < year:
            print(f'{d["title"]} ({d["year"]})')
before_year(data) """

#File Four

""" def during_year(data):
    year = int(input("Give me a year and I will print all movies that were released in that year: "))
    for d in data:
        if d["year"] == year:
            print(f'{d["title"]} ({d["year"]})')
during_year(data) """

#File Five

def search(data):
    find = input("What movie(s) are you searching for?: ")
    title = [data['title']]
    for movie in data:
        if find == title:
            print(title)
search(data)

#File Six

""" def genre_search(data):
    genre_list = [data["genres"]]
    movie = input("Give me a genre to search for movies of the same genre: ")
    for movie in data:
        for movie in genre  """

