# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:14:11 2015

@author: RedQueen
"""
"""

OPTIONAL HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.

For example, get_movie_info('tt0111161') returns:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
"""

import requests


# define a function that accepts an IMDb ID and returns a dictionary of movie information
from time import sleep
def get_movie_info(imdb_id):
    r = requests.get('http://www.omdbapi.com/?i=' + imdb_id +'&r=json&type=movie')
    info = r.json()
    if info['Response'] == 'True':
        movie_info = {} 
        movie_info['content_rating'] = info ['Rated']
        movie_info['description'] = info ['Plot']
        movie_info['duration'] = info ['Runtime']
        movie_info['star_rating'] = info ['imdbRating']
        movie_info['title'] = info ['Title']
        return movie_info
        sleep(2)
    else:
        return 0

# test the function

# open the file of IDs (one ID per row), and store the IDs in a list
with open ('imdb_ids.txt', 'rU') as f:
    imdb_ids =[imdb_id.strip() for imdb_id in f]


# get the information for each movie, and store the results in a list
query = [get_movie_info(imdb_id) for imdb_id in imdb_ids]


# check that the list of IDs and list of movies are the same length
assert(len(imdb_ids)==len(query))


# convert the list of movies into a DataFrame
import pandas as pd
pd.DataFrame(query)
