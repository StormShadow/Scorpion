'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''
import pandas as pd
# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('imdb_1000.csv', sep = ',')

# check the number of rows and columns
# 979 x 6
movies.shape

# check the data type of each column
# Star Rating is a float (likely a scale of 10 w min at 7.40 and max at 9.30)
# Tite is object/ string
# Content rating is object/ string
# Genre is object/ string
# Duration is integer (likely in minutes)
# Actor list is object/ list of strings
movies.dtypes

# calculate the average movie duration
# 121 minutes
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
# Shortest is Freaks at 64 min
movies.sort('duration').head(1)
# Longsest is Hamlet at 242 min
movies.sort('duration', ascending = False).head(1)

# create a histogram of duration, choosing an "appropriate" number of bins
import matplotlib.pyplot as plt
movies.duration.plot(kind = 'hist', bins = 8)


# use a box plot to display that same data
movies.duration.plot(kind =  'box', figsize = (10,8))

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
# R: 460, PG13: 189, PG: 123, Not Rated: 65, Approved: 47
# Unrated: 38, G: 32, Passed: 7, NC-17: 7, X: 4, GP 3, TVMA: 1
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title = 'Number of Movies by Rating')
plt.xlabel('Movie Rating')
plt.ylabel('Frequency')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace = True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X', 'TV-MA'], 'NC-17', inplace = True)

# count the number of missing values in each column
# 3 missing values
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
movies.content_rating.fillna(value= 'PG', inplace=True)


# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
# Greater than 2 hours, avg star rating is 8.0
# Less than 2 hours, avg star rating is 7.8
movies[movies.duration >= 120].star_rating.mean()
movies[movies.duration < 120].star_rating.mean()

# use a visualization to detect whether there is a relationship between star rating and duration
# longer duration appears to correlate with higher star rating
movies.plot(kind = 'scatter', x = 'duration', y = 'star_rating', alpha = 0.3, figure =(10,8))
movies.boxplot(column='duration', by='star_rating', figsize = (10,8))


# calculate the average duration for each genre
# Action: 126 min, Adventure: 135 min, Animation: 97 min, Biography: 132 min
# Comedy: 108 min, Crime: 122 min, Drama: 127 min, Family: 108 min
# Fantasy: 112 min, Film-Noir: 97 min, History: 66 min, Horror: 102 min
# Mystery 116 min, Sci-Fi: 109 min, Thriller: 114 min, Western 137 min
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
"""
movies.groupby('content_rating').mean().drop('star_rating', axis=1).plot(kind='bar', stacked=True)
movies.groupby('content_rating').mean().drop('star_rating', axis=1).plot(kind='bar')
don't think this told me much, thought it better to do a cross tab of movie lenghts vs. content rating
also tried value counts of duration and histogram, but too many entries spanning various durations
thought it better to cross tab a movie length range/ descriptive rating (based on duration) with content rating
"""
# Appears that R & PG 13 have more movies over 2 hours
movies['movie_length'] = 'short'   
movies.loc[movies.duration.between(102, 120), 'movie_length'] = 'average'     
movies.loc[movies.duration.between(121, 243), 'movie_length'] = 'long'    
pd.crosstab(movies.content_rating, movies.movie_length)
pd.crosstab(movies.content_rating, movies.movie_length).plot(kind = 'bar')

# determine the top rated movie (by star rating) for each genre
# Top rated G = Modern Times at 8.6 stars
# Top rated NC-17 = A Clockwork Organge at 8.4 stars
# Top rated PG = Star Wars Ep 5 Empire Strikes Back at 8.8 stars
# Top rated PG13 = The Dark Knight at 9
# Top rated R = Shawshank Redemption at 9.3
# Top Rated UNRATED tie between 12 Angry Men and The Good, the Bad and the Ugly

movies.groupby('content_rating').star_rating.agg(['max']) #shows max rating per genre
movies[(movies.content_rating == 'G') & (movies.star_rating == 8.6)].loc[:, 'star_rating': 'title']
movies[(movies.content_rating == 'NC-17') & (movies.star_rating == 8.4)].loc[:, 'star_rating': 'title']
movies[(movies.content_rating == 'PG') & (movies.star_rating == 8.8)].loc[:, 'star_rating': 'title']
movies[(movies.content_rating == 'PG-13') & (movies.star_rating == 9.0)].loc[:, 'star_rating': 'title']
movies[(movies.content_rating == 'R') & (movies.star_rating == 9.3)].loc[:, 'star_rating': 'title']
movies[(movies.content_rating == 'UNRATED') & (movies.star_rating == 8.9)].loc[:, 'star_rating': 'title']
# running above code as a block only shows the last group (Unrated) in output?

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.title.duplicated()] # shows suspected duplicate titles
# The Girl with the Dragon Tatooo, Dracula, Les Miserables, True Grit
# Although titles are identicals, not actual duplicates, represent remakes, can tell easily tell from actors, year if available would probably also be a good indicator
movies[movies.title.isin(['The Girl with the Dragon Tattoo', 'Dracula', 'True Grit', 'Les Miserables'])] 
# ^ pulls suspected dupes and confirms not actual duplicates, different actors and star ratings
# Ask about text editor used by Kevin in class

# calculate the average star rating for each genre, but only include genres with at least 10 movies
# identify number of entries in each genre
movies.groupby('genre').genre.value_counts()
# calculate mean, drop values for genres identified above where thre are less than ten entries
movies.groupby('genre').star_rating.mean().drop(['Family', 'Fantasy', 'Film-Noir', 'History', 'Sci-Fi', 'Thriller', 'Western'])

'''
BONUS
'''
# Figure out something "interesting" using the actors data!
"""
Save for practice, use csv reader to count actor frquency
Current problem, turning actor data into a clean list that 
Using

import csv
with open("imdb_1000.csv", 'rU') as imdb_file:
    imdb_data = [imdb_row for imdb_row in csv.reader(imdb_file)]
imdb_header = imdb_data[0]
imdb_body = imdb_data[1:]
actor_col = 

from collections import defaultdict
actor_frequency = defaultdict(int)
for actor in imdb_body[5]:
    if chip_order in chip_order_quant:
        chip_order_count[chip_order[0]] = chip_order_count[chip_order[0]] +1*chip_order[1]
    else:
        chip_order_count[chip_order[0]] = 1*chip_order[1]
"""