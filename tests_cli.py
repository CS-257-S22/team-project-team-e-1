from asyncio import subprocess
from cProfile import run
import unittest
import main
import os

class TestRandom(unittest.TestCase):
    """A GOOD DOCSTRING """
    def test_basicRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser([])), main.initializeData, "Ouput is not a valid show/movie in dataset.")
    def test_optionsRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser(["-t", "Movie", "-g", "Documentaries"])), main.initializeData, "Ouput is not a valid documentary movie in dataset.")
    def test_edgeRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser(["-t", "Movie", "-g", "Comedies","-d", "Bruno Garotti", "-c", "Klara Castanho", "-y", "2021"])), main.initializeData[14], "Ouput is not a valid documentary movie in dataset.")
    def test_Randomness(self):
        self.assertNotEqual(main.getRandomMovie(main.Parser([])), main.getRandomMovie(main.Parser([])), "Ouput is not random (or the odds are for ever in your favor)")

class TestGettingPopularMovies(unittest.TestCase):
    def test_popularTitlestxtExists(self):
        """Checks if popularTitles.txt is already made"""
        import os.path
        popularTitlesTextExists = os.path.exists('popularTitles.txt')
        self.assertTrue(popularTitlesTextExists, "The text file popularTitles.txt does not exist")

    def test_sortingAlgorithmHelper(self):
        testList = [['MovieTitle1',1], ["MovieTitle2",4], ["MovieTitle3",3], ["MovieTitle4",5], ["MovieTitle5",2]]
        sortedtestList = [["MovieTitle1",1], ["MovieTitle5",2], ["MovieTitle3",3], ["MovieTitle2",4], ["MovieTitle4",5]]
        self.assertEqual(bubble_sort(testList), sortedtestList, "Sorting algorithm does not return sorted list")
    
    def test_movieListUpdateHelper(self):
        currentMovie = ["Movie", "newTitle", 11]
        movieList = [["MovieTitle1",1], ["MovieTitle5",2], ["MovieTitle3",3], ["MovieTitle2",4], ["MovieTitle4",5], ["MovieTitle7",6], ["MovieTitle8",7], ["MovieTitle10",8], ["MovieTitle6",9], ["MovieTitle9",10]]
        self.assertIn(["newTitle", 11], updatePopularMoviesList(movieList, currentMovie), "updatePopularMoviesList function does not replace less popular movie in list with more popular movie when list is full")

class TestGETMOVIE(unittest.TestCase):
    def testReturnValue(self):
        result = main.getMovie("Je Suis Karl")
        self.assertIsInstance(result, list, "Function does not return a list of datapoints")

    def testMovieContents(self):
        dataset = main.initializeData()
        result = main.getMovie("Sankofa")
        self.assertEqual(result, dataset[8], "Function return value does not represent correct dataset entries")

class TestPROCESSING(unittest.TestCase):
    def testDataset(self):
        result = main.initializeData()
        self.assertEqual(len(result), 8808, "Dataset not fully processed")

class testPARSER(unittest.TestCase):
    def testParseArgs(self):
        testString = ["-cast", "Ryan", "Gosling", "-year", "1969", "1984"]
        result = main.Parser(testString)
        self.assertEqual(result.getCast(), ["Ryan", "Gosling"], "Doesn't parse cast search terms")
        self.assertEqual(result.getYear(), ["1969", "1984"], "Doesn't parse year search terms")
class testFINDMATCHINGMOVIES(unittest.TestCase):
    def testSearchOneTerm(self):
        parsedArgs = main.Parser([])
        parsedArgs.title = ["bangkok"]
        result = main.findMatchingMovie(parsedArgs)
        for movie in result:
            self.assertIn("bangkok", movie, "Returns movie which don't match the criterion")
    def testParseAndSearch(self):
        parsedArgs = main.Parser(["-title", "bangkok"])
        result = main.findMatchingMovie(parsedArgs)
        for movie in result:
            self.assertIn("bangkok", movie, "Returns movie which don't match the criterion")

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
