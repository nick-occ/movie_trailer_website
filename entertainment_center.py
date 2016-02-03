"""
Created on Jan 23, 2016

@author:    Nicholas Occhipinti
@summary:   Program will create a list of Movie objects and display them in 
            a webpage using the fresh_tomatoes module
"""

# import fresh_tomatoes python module
import fresh_tomatoes

# import Movie class in media.py module
from media import Movie


# create six Movie objects
# inputs:  movie title, image url, trailer url, movie url, cast, release date
#          and rating.
# sources: rating information obtained from http://www.imdb.com 


forrest_gump = Movie("Forrest Gump",
                     "https://www.movieposter.com/posters/archive/main/38/MPW-19355",
                     "https://www.youtube.com/watch?v=uPIEn0M8su0",
                     "http://www.imdb.com/title/tt0109830/?ref_=nv_sr_1",
                     "Tom Hanks, Robin Wright, Gary Sinise",
                     1994,
                     "8.8 out of 10 stars")

christmas_vacation = Movie("Christmas Vacation",
                           "http://www.movieposter.com/posters/archive/main/77/MPW-38615",
                           "https://www.youtube.com/watch?v=NBTTipJX-h4",
                           "http://www.imdb.com/title/tt0097958/?ref_=nv_sr_1",
                           "Chevy Chase, Beverly D'Angelo, Juliette Lewis",
                           1989,
                           "7.6 out of 10 stars")

martian = Movie("The Martian",
                "http://www.movieposter.com/posters/archive/main/204/MPW-102006",
                "https://www.youtube.com/watch?v=ej3ioOneTy8",
                "http://www.imdb.com/title/tt3659388/?ref_=nv_sr_1",
                "Matt Damon, Jessica Chastain, Kristen Wiig",
                2015,
                "8.1 out of 10 stars")

saving_private_ryan = Movie("Saving Private Ryan",
                            "http://www.movieposter.com/posters/archive/main/41/MPW-20712",
                            "https://www.youtube.com/watch?v=vwAxi4A2YcY",
                            "http://www.imdb.com/title/tt0120815/?ref_=nv_sr_1",
                            "Tom Hanks, Matt Damon, Tom Sizemore",
                            1998,
                            "8.6 out of 10 stars")

gladiator = Movie("Gladiator",
                  "http://www.movieposter.com/posters/archive/main/22/A70-11370",
                  "https://www.youtube.com/watch?v=ol67qo3WhJk",
                  "http://www.imdb.com/title/tt0172495/?ref_=nv_sr_1",
                  "Russell Crowe, Joaquin Phoenix, Connie Nielsen",
                  2000,
                  "8.5 out of 10 stars")

ghostbusters = Movie("Ghostbusters",
                     "https://www.movieposter.com/posters/archive/main/58/MPW-29159",
                     "https://www.youtube.com/watch?v=vntAEVjPBzQ",
                     "http://www.imdb.com/title/tt0087332/?ref_=nv_sr_2",
                     "Bill Murray, Dan Aykroyd, Sigourney Weaver",
                     1984,
                     "7.8 out of 10 stars")


# put movies object in a list
movies = [forrest_gump, christmas_vacation, martian, saving_private_ryan,
          gladiator, ghostbusters]


# call open_movies_page in fresh_tomatoes module and pass list of movies as a
# parameter
fresh_tomatoes.open_movies_page(movies)
