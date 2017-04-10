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


class TwitterTestCases(unittest.TestCase):
	def test_tweet(self):
		t = Tweet("Mark Waters")
		self.assertEqual(type(t.director), str)


## Remember to invoke all your tests...
if __name__ == "__main__":
    unittest.main(verbosity=2)