import unittest
import command_line

class TestSOMETHING(unittest.TestCase):
    def test_A_GOOD_NAME(self):
        """ A GOOD DOCSTRING """
        #make a bit of dummy data
        act_num_goals = 4
        #call your non-existent function
        alleged_num_goals = getNumberGoals()
        #check if the result of the call is what it should be
        #   probably using self.assertEqual(something, something_else)
        self.assertEqual(act_num_goals,alleged_num_goals,"The alleged number of goals is not the actual number.")

if __name__ == '__main__':
    unittest.main()