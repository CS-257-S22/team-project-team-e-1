import os.path
import unittest
import main


data = main.initializeData()
 
class TestRandom(unittest.TestCase):
    """A GOOD DOCSTRING """
    def test_basicRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser([])), data, "Ouput is not a valid show/movie in dataset.")
    def test_certainCriteria(self):
        self.assertEqual(main.getRandomMovie(main.Parser(["-cast", "Klara Castanho"])),data[14],"Does not provide correct movie.")
    def test_optionsRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser(["-ti", "Movie", "-di", "Spielberg"])), data, "Ouput is not a valid documentary movie in dataset.")
    def test_edgeRandom(self):
        self.assertIn(main.getRandomMovie(main.Parser(["-ty", "Movie","-di", "Bruno Garotti", "-ca", "Klara Castanho", "-y", "2021"])), data, "Ouput is not a valid documentary movie in dataset.")
    def test_Randomness(self):
        self.assertNotEqual(main.getRandomMovie(main.Parser([])), main.getRandomMovie(main.Parser([])), "Ouput is not random (or the odds are for ever in your favor)")
    
class TestGettingPopularMovies(unittest.TestCase):
    def test_popularTitlestxtExists(self):
        """Checks if popularTitles.txt is already made"""
        popularTitlesTextExists = os.path.exists('popularTitles.txt')
        self.assertTrue(popularTitlesTextExists, "The text file popularTitles.txt does not exist")

    def test_sortingAlgorithmHelper(self):
        """checks if the bubble sort algorithm works correctly on the list it's given"""
        testList = [['MovieTitle1',1], ["MovieTitle2",4], ["MovieTitle3",3], ["MovieTitle4",5], ["MovieTitle5",2]]
        sortedtestList = [["MovieTitle1",1], ["MovieTitle5",2], ["MovieTitle3",3], ["MovieTitle2",4], ["MovieTitle4",5]]
        self.assertEqual(main.bubble_sort(testList), sortedtestList, "Sorting algorithm does not return sorted list")
    
    def test_movieListUpdateHelper(self):
        """Checks if the list of popular movies is updated when a more popular movie is found.

        Keyword arguments:
        currentMovie -- a movie that is more popular than the least popular movie currently in the popular movies list
        movieList -- the popular movies list
        """
        currentMovie = ["Movie", "newTitle", 11]
        movieList = [["MovieTitle1",1], ["MovieTitle5",2], ["MovieTitle3",3], ["MovieTitle2",4], ["MovieTitle4",5], ["MovieTitle7",6], ["MovieTitle8",7], ["MovieTitle10",8], ["MovieTitle6",9], ["MovieTitle9",10]]
        self.assertIn(["newTitle", 11], main.updatePopularMoviesList(movieList, currentMovie), "updatePopularMoviesList function does not replace less popular movie in list with more popular movie when list is full")

class TestGETMOVIE(unittest.TestCase):
    def testReturnValue(self):
        result = main.getMovie("Je Suis Karl")
        self.assertIsInstance(result, list, "Function does not return a list of datapoints")

    def testMovieContents(self):
        result = main.getMovie("Sankofa")
        self.assertEqual(result, data[8], "Function return value does not represent correct dataset entries")

    def testNoisyData(self):
        result = main.getMovie("Seabiscuit ")
        self.assertEqual(result, data[350], "Function does not correct for spaces at end of text")

class TestPROCESSING(unittest.TestCase):
    def testDataset(self):
        self.assertEqual(len(data), 8808, "Dataset not fully processed")

        
class testPARSER(unittest.TestCase):
    def testParseArgs(self):
        testString = ["-cast", "Ryan", "Gosling", "-year", "1969", "1984"]
        result = main.Parser(testString)
        self.assertEqual(result.getCast(), ["Ryan", "Gosling"], "Doesn't parse cast search terms")
        self.assertEqual(result.getYear(), ["1969", "1984"], "Doesn't parse year search terms")
        badInput = ["-c", "Ryan", "Gosling", "-year", "1969", "1984"]
        #self.assertEqual(main.Parser(badInput),"Incorrect definition of a category. Use \"usage\" function to get help.", "Doesn't throw error for faulty category in command line.")

class testFINDMATCHINGMOVIES(unittest.TestCase):
    def testSearchOneTerm(self):
        parsedArgs = main.Parser([])
        parsedArgs.title = ["Bangkok"]
        result = main.findMatchingMovies(parsedArgs)
        for movie in result:
            self.assertIn("Bangkok", movie, "Returns movie which don't match the criterion")
    def testParseAndSearch(self):
        parsedArgs = main.Parser(["-title", "Bangkok"])
        result = main.findMatchingMovies(parsedArgs)
        for movie in result:
            self.assertIn("Bangkok", movie, "Returns movie which don't match the criterion")

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
