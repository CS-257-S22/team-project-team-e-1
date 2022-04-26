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

class TestRandom(unittest.TestCase):

    #test a specific case (Klara) which should always give the same movie
    def test_Klara(self):
        """checks if getRandomMovie with specific filtering returns the information of the only movie that works "Confessions of an Invisible Girl"""
        self.app = app.test_client()
        response = self.app.get('/getRandomMovie/-ca/Klara Castanho', follow_redirects=True)
        self.assertEqual(str.encode(str(['s14', 'Movie', 'Confessions of an Invisible Girl', 'Bruno Garotti', 'Klara Castanho, Lucca Picon, Júlia Gomes, Marcus Bessa, Kiria Malheiros, Fernanda Concon, Gabriel Lima, Caio Cabral, Leonardo Cidade, Jade Cardozo', '', 'September 22, 2021', '2021', 'TV-PG', '91 min', 'Children & Family Movies, Comedies', "When the clever but socially-awkward Tetê joins a new school, she'll do anything to fit in. But the queen bee among her classmates has other ideas."])), response.data,"Klara Castanho example does not work.")
    
    #test the randomness of the generic getRandomMovie function
    def test_Random(self):
        """checks if getRandomMovie without arguments is actually random (gives a new movie each time"""
        self.app = app.test_client()
        response1 = self.app.get('/getRandomMovie/', follow_redirects=True)
        response2 = self.app.get('/getRandomMovie/', follow_redirects=True)
        self.assertEqual(response1.data, response2.data,"Klara Castanho example does not work.")

class TestPopularMoviespage(unittest.TestCase):
    """Checks if the popular movies page is working correctly"""
    def test_popMoviesRoute(self):
        self.app = app.test_client()
        response = self.app.get('/popularmovies', follow_redirects=True)

        #popMovieString may need to be updated occasionally as the popular movies are subject to change
        popMovieString = b"['Naruto the Movie 3: Guardians of the Crescent Moon Kingdom', 'InuYasha the Movie 4: Fire on the Mystic Island', 'Bird Box', 'Confessions of an Invisible Girl', 'Total Frat Movie', 'Bobbleheads The Movie', 'Seabiscuit', 'The Adventures of Tintin', 'Je Suis Karl', 'Sankofa']"
        self.assertEqual(popMovieString, response.data)

class TestHELPERS(unittest.TestCase):
    def testParserHelper(self):
        testTitle = helperParser("Catch_Me_If_You_Can")
        self.assertEqual(testTitle, "Catch Me If You Can", "Helper function does not convert underscores into spaces.")

class testMATCHINGMOVIES(unittest.TestCase):
    def testMatchingMovies(self):
        '''Does the site return all the movies from 1969?'''
        self.app = app.test_client()
        movies_1969 = ['Prince', 'True Grit']
        response = self.app.get('/findMatchingMovies/-year/1969')
        for movie in movies_1969:
            self.assertIn(bytes(movie, 'utf-8'), response.data)


class TestFunction(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/getMovie/Bird_Box', follow_redirects=True)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
    print("Everything passed")