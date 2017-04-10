## Your name: Benjamin Zeffer
## The option you've chosen: 2

# Put import statements you expect to need here!
import unittest # for testing
import requests 
import tweepy
import twitter_info # as always when dealing with twitter because proper authentication is needed!
import json
import sqlite3
import itertools # for generators and list comprehension
import collections # used for containers and Counter



##### Potential Functions/Sudo code ##############################


#### def getTwitterInfo(username):
#
# PURPOSE: Making a call to the Tweepy API to get data about posted Tweets by the specified twitter user
#
# INPUT: twitter username
#
# RETURN: JSON object that can be used for extracting data later on
#
#
#------------------------------------------------------------
#
#### def getOMDBInfo(search_info):
# 
# PURPOSE: Making a call to the OMDB API and requesting the specified data
# 
# INPUT: search terms like movie name, actors, director, IMDB rating, etc
# 
# RETURN: JSON object that can be used later for extracting data when necessary
# 
# API: http://www.omdbapi.com/?
# 
# EXAMPLE OF RETURN DATA:
# {"Title":"Jason Bourne","Year":"2016","Rated":"PG-13","Released":"29 Jul 2016",
#  "Runtime":"123 min","Genre":"Action, Thriller","Director":"Paul Greengrass",
#  "Writer":"Paul Greengrass, Christopher Rouse, Robert Ludlum (characters)",
#  "Actors":"Matt Damon, Tommy Lee Jones, Alicia Vikander, Vincent Cassel",
#  "Plot":"The CIA's most dangerous former operative is drawn out of hiding to
#   uncover more explosive truths about his past.","Language":"English, Greek, 
#   German","Country":"UK, China, USA", "Awards":"13 nominations.", "Poster":
#  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1ODg2OTU1MV5BMl5BanB
#  nXkFtZTgwMzA5OTg2ODE@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie 
#  Database","Value":"6.7/10"},{"Source":"Rotten Tomatoes","Value":"56%"},
#  {"Source":"Metacritic","Value":"58/100"}],"Metascore":"58","imdbRating":
#  "6.7","imdbVotes":"143,037","imdbID":"tt4196776","Type":"movie","DVD":
#  "06 Dec 2016","BoxOffice":"$162,162,120.00","Production":"Universal",
#  "Website":"http://www.jasonbournemovie.com/","Response":"True"}
# 
# ----------------------------------------------------------------
# 
# #### class Movie(self, OMDB_obj = {}):
# 
# PURPOSE: this class will be for the movie attributes (title, director, IMDB rating, actors, etc).
# 
# INPUT: The JSON object that will be extracted using the OMDB function from the getOMBDInfo function which grabs data from the OMDB API
# 
# RETURN: it would return a string method containing the information being searched for (director, title, IMDB rating, actors, etc)
# 
# CONSTRUCTOR: will be defining all of the self variables so that they may be used for further methods in the class
# 
#     METHODS: there will be methods with are dedicated to returning each of the stated elements (and possibly more). There will be a method whose purpose is to put the data in a format that will be easy to push it into a database. More methods are coming...
# 
# Other functions/classes/things are in the making/still being thought of...
# 
##################################################################



# Write your test cases here.

class MovieTestCases(unittest.TestCase):

	# fetching data about a movie, in this case "Mean Girls"
    base_url = "http://www.omdbapi.com/"
    parameters = {}
    parameters["t"] = "mean girls" # "t" came from the API pages, this is what the key is automatically
    response = requests.get(base_url, params=parameters)
    data = json.loads(response.text)


    # Testing if the movie title is a string
    def test_movie_title_type(self):
        self.assertEqual(type(m.title), str)

    # This will be testing the movie title
    def test_movie_title(self):
        m = Movie(data)
        self.assertEqual(m.title, "Mean Girls")

    # This will be testing the __str__ method for the class Movie and it's "output"
    def test_movie_str(self):
        m = Movie(data)
        self.assertEqual(m.__str__(), "Mean Girls, directed by Mark Waters")

    # This will be testing the plot of the movie
    def test_movie_plot(self):
        m = Movie(data)
        self.assertEqual(m.plot, "Cady Heron is a hit with The Plastics, the A-list girl clique at her new school, until she makes the mistake of falling for Aaron Samuels, the ex-boyfriend of alpha Plastic Regina George.")

    # This will be testin the movie's release date is a string
    def test_movie_released(self):
    	m = Movie(data)
    	self.assertEqual(m.released, str)

    # Tesing if the strings match
    def test_movie_released(self):
    	m = Movie(data)
    	self.assertEqual(m.released, "30 Apr 2004")

    # This will be testing the actors and seeing if they appear in a string
    def test_movie_actors_type(self):
        m = Movie(data)
        self.assertEqual(type(m.actors), str)

    # Tesing the number of actors is 4
    def test_movie_actors_len(self):
    	m = Movie(data)
    	self.assertEqual(len(m.actors.split(",")), 4)

    # Tesing that the actors are correct
    def test_movie_actors_names(self):
    	m = Movie(data)
    	self.assertEqual(m.actors, "Lindsay Lohan, Rachel McAdams, Tina Fey, Tim Meadows")


## Remember to invoke all your tests...
if __name__ == "__main__":
    unittest.main(verbosity=2)