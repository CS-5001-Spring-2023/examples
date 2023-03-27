'''
WARNING! This is untouched from what we did in class.
This example is incomplete. Use with caution!
'''


import json
# https://docs.python.org/3/library/json.html

class Movie:
	# genre
	# id
	# title
	# rating

	def __init__(self, genre, id, title, watched=False):
		self.genre = genre
		self.id = id
		self.title = title
		self.watched = watched

	def __str__(self):
		return f'{self.title} - {self.genre}'



movie_list = []

filename = 'movie_genre.json'
file = open(filename)
movie_dataset = json.load(file)

by_char = {}
# dict of string -> list of movie objects
'''
	'A' -> [movies that start with A],
	'B' -> [movies that start with B]
'''

by_genre = {}
# dict of string -> list of movie objects
'''
	'Action' -> [movies with genre Action],
	'Mystery' -> [movies with genre Mystery]
'''

by_title = []

# list of movie objects
movie_list = []

for genre in movie_dataset:	
	movies = movie_dataset[genre]
	for movie_id in movies:
		movie_title = movies[movie_id]
		
		movie = Movie(genre, movie_id, movie_title)
		
		# add to main movie list
		movie_list.append(movie)

		# insert movie into by_title tile

		# insert into by_char dict
		# first_char = movie_title[0]		
		# if not first_char in by_char:
		# 	by_char[first_char] = [movie]
		# else
		#   by_char[first_char].append(movie)



# for movie in movie_list:
# 	print(movie)

# how many movies are there of a particular genre
target_genre = 'Action'
count = 0
for movie in movie_list:
	if movie.genre == target_genre:
		count += 1
print(f'There are {count} movies with genre {target_genre}.')

# how many movies have a title that starts with the character C
target_start_char = 'C'
count = 0
for movie in movie_list:
	if movie.title[0] == target_start_char:
		count += 1
print(f'There are {count} movies that start with {target_start_char}.')


