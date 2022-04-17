from asyncio import subprocess
from cProfile import run
import unittest
import main
import os

class TestRandom(unittest.TestCase):
    """ A GOOD DOCSTRING """
    def test_basicRandom(self):
        self.assertIn(subprocess.run("python3 main.py getRandomMovie"), main.initializeData, "Ouput is not a valid show/movie in dataset.")
    def test_optionsRandom(self):
        self.assertIn(subprocess.run("python3 main.py getRandomMovie -t Movie -g Documentaries"), main.initializeData, "Ouput is not a valid documentary movie in dataset.")
    def test_edgeRandom(self):
        self.assertIn(subprocess.run("python3 main.py getRandomMovie -t Movie -g Documentaries -d Bruno Garotti -c Klara Castanho -y 2021"), main.initializeData[14], "Ouput is not a valid documentary movie in dataset.")


class TestGETMOVIE(unittest.TestCase):
    def testReturnValue(self):
        result = main.getMovie("Je Suis Karl")
        self.assertIsInstance(result, list, "Function does not return a list of datapoints")

    def testMovieContents(self):
        dataset = main.initializeData()
        result = main.getMovie("Sankofa")
        self.assertEqual(result, dataset[8], "Function return value does not represent correct dataset entries")

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
