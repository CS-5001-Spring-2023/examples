import json
# https://docs.python.org/3/library/json.html

file = open('movie_genre.json')
data = json.load(file)
for genre in data:		
	for movies in data[genre]:
		print(data[genre][movies])
			# print(title)
