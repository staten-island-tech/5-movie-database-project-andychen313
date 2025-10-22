import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" def title():
    for index, item in enumerate(data):
        print(index, item["title"])
title()
 """
""" def year():
    for index, item in enumerate(data):
        print(index, item["year"])
year() """

""" def year():
    year = input("Give me a year and I will print all movies released after that year: ")
    for index, item in enumerate(data):
        for year+1, 
        print(index, item[""]) """

""" def titles(data):
    for d in data:
        print(d["title"])
titles(data) """

""" def after_year(data):
    year = int(input("Give me a year and I will print all movies released after that year: "))
    for d in data:
        if int(d["year"]) > year:
            print(f'{d["title"]} ({d["year"]})')
after_year(data) """

""" def before_year(data):
    year = int(input("Give me a year and I will pritn all movies released before that year: "))
    for d in data:
        if int(d["year"]) < year:
            print(f'{d["title"]} ({d["year"]})')
before_year(data) """

""" def during_year(data):
    year = int(input("Give me a year and I will print all movies that were released in that year: "))
    for d in data:
        if d["year"] == year:
            print(f'{d["title"]} ({d["year"]})')
during_year(data) """