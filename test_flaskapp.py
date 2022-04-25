from teamFlaskApp import *
import unittest
import main

class TestHomepage(unittest.TestCase):
    """Checks if the homepage is working correctly"""
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        
        #checks if the first part of the homepage introduction works
        self.assertIn(b'Welcome to the', response.data)
        #checks if the last part of the homepage introduction works
        self.assertIn(b'followed by /getMovie/Bird_Box.', response.data)

class TestPopularMoviespage(unittest.TestCase):
    """Checks if the popular movies page is working correctly"""
    def test_popMoviesRoute(self):
        self.app = app.test_client()
        response = self.app.get('/popularmovies', follow_redirects=True)

        #popMovieString may need to be updated occasionally as the popular movies are subject to change
        popMovieString = b"['Naruto the Movie 3: Guardians of the Crescent Moon Kingdom', 'InuYasha the Movie 4: Fire on the Mystic Island', 'Bird Box', 'Confessions of an Invisible Girl', 'Total Frat Movie', 'Bobbleheads The Movie', 'Seabiscuit', 'The Adventures of Tintin', 'Je Suis Karl', 'Sankofa']"
        self.assertEqual(popMovieString, response.data)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")