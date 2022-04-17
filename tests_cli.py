from asyncio import subprocess
from cProfile import run
import unittest
import main
import os

class TestRandom(unittest.TestCase):
    def test_basicRandom(self):
        """ A GOOD DOCSTRING """
        self.assertIn(subprocess.run("python3 main.py getRandomMovie"), main.initializeData, "Ouput is not a valid show/movie in dataset.")
    def test_optionsRandom(self):
        self.assertIn(subprocess.run("python3 main.py getRandomMovie -t Movie -g Documentaries"), main.initializeData, "Ouput is not a valid documentary movie in dataset.")
    def test_edgeRandom(self):
        self.assertIn(subprocess.run("python3 main.py getRandomMovie -t Movie -g Documentaries -d Bruno Garotti -c Klara Castanho -y 2021"), main.initializeData[14], "Ouput is not a valid documentary movie in dataset.")
    
if __name__ == '__main__':
    unittest.main()
