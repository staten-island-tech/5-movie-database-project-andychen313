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

def year():
    year = input("Give me a year and I will print all movies released after that year: ")
    for index, item in enumerate(data):
        for year+1, 
        print(index, item[""])