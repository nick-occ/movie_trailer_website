"""
Created on Jan 23, 2016

@author:    Nicholas Occhipinti
@summary:   Create a class capturing the movie title, image and trailer url,
            website, cast, release year and rating 
Attributes:
    title (str): Title of the moview
    poster_image_url (str): URL to display image of movie in webpage
    trailer_youtub_url (str): URL to YouTube video trailer
    movie_link  (str): URL to IMDB.com page for more information on movie
    release_year (int): Year movie was released
    movie_rating (str): Movie rating from IMDB.com
"""

# create Movie class
class Movie():
    
    # Movie constructor creating instance variables
    def __init__(self,movie_title,movie_image,movie_trailer,movie_link,
                 movie_cast,release_year,movie_rating):
        self.title = movie_title
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
        self.movie_link = movie_link,
        self.movie_cast = movie_cast,
        self.release_year = release_year,
        self.movie_rating = movie_rating
    