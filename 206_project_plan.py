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

    base_url = "http://www.omdbapi.com/"
    parameters = {}
    parameters["t"] = "mean girls"
    response = requests.get(base_url, params=parameters)
    data = json.loads(response.text)

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

    # This will be testin gthe movie's release date
    def test_movie_released(self):
    	m = Movie(data)
    	self.assertEqual(m.released, "30 Apr 2004")

    # This will be testing the actors
    def test_movie_actors(self):
        m = Movie(data)
        self.assertEqual(m.actors, ["Lindsay Lohan", "Rachel McAdams", "Tina Fey", "Tim Meadows"])
		self.assertEqual(len(m.actors), 4)
		self.assertEqual(type(m.actors), list)

	def test_movie_IMDBrating(self):
		m = Movie(data)
		self.assertEqual(m.IMDBrating, "84%")





class DatabaseTests(unittest.TestCase):

    def test_movie_db_columns1(self):
        conn = sqlite3.connect('final_project.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Movies')
        result = cur.fetchall()
        self.assertEqual(len(result[0]), 8)
        conn.close()

    def test_users_db_columns2(self):
        conn = sqlite3.connect('final_project.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users')
        result = cur.fetchall()
        self.assertEqual(len(result[0]), 4)
        conn.close()

    def test_tweets_db_columns3(self):
        conn = sqlite3.connect('final_project.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Tweets')
        result = cur.fetchall()
        self.assertEqual(len(result[0]), 6)
        conn.close()


## Remember to invoke all your tests...
if __name__ == "__main__":
    unittest.main(verbosity=2)