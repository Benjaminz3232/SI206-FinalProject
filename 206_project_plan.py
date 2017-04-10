## Your name: Benjamin Zeffer
## The option you've chosen: 2

# Put import statements you expect to need here!
import unittest
import requests
import tweepy
import twitter_info # as always when dealing with twitter because proper authentication is needed!
import json
import sqlite3
import itertools
import collections

# Write your test cases here.

class MovieTestCases(unittest.TestCase):
	
    base_url = "http://www.omdbapi.com/"
    params = {}
    params["t"] = "mean girls"
    r = requests.get(base_url, params=params)
    data = json.loads(r.text)

    def test_movie_title(self):
        movie = Movie(data)
        self.assertEqual(movie.title, "Mean Girls")

    def test_movie_released(self):
    	movie = Movie(data)
    	self.assertEqual(movie.released, "30 Apr 2004")

    def test_movie_actors(self):
        movie = Movie(data)
        self.assertEqual(movie.actors, "Lindsay Lohan, Rachel McAdams, Tina Fey, Tim Meadows"))

	def test_movie_IMDBrating(self):
		movie = Movie(data)
		self.assertEqual(movie.IMDBrating, "84%")

    def test_movie_plot(self):
        movie = Movie(data)
        self.assertEqual(movie.plot, "Cady Heron is a hit with The Plastics, the A-list girl clique at her new school, until she makes the mistake of falling for Aaron Samuels, the ex-boyfriend of alpha Plastic Regina George.")

    def test_movie_str(self):
        movie = Movie(data)
        self.assertEqual(movie.__str__(), "Mean Girls, directed by Mark Waters")


## Remember to invoke all your tests...
if __name__ == "__main__":
    unittest.main(verbosity=2)