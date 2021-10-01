from calculator import *
import unittest

class TestCalculator(unittest.TestCase):

    # you may create more test methods
    # you may add parameters to test methods
    # this is an example
    def test_cost_empty_param(self):
        """
        Purpose : Checking for empty string as parameter to cost_calculation
        """
        # Empty values passed in to each and every parameter each to ensure that everything affects it.
        self.calculator = Calculator()
        self.assertEqual(self.calculator.cost_calculation("", "100", "100", "True", "True"), ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "", "100", "True", "False"), ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "100", "", "False", "True"), ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "100", "100", "", "False"), ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "100", "100", "True", ""), ('Invalid parameter values'))

    def test_time_empty_param(self):
        """
        Purpose : Checking for empty string as parameter to time_calculation
        """
        # Empty values passed in to each and every parameter each to ensure that everything affects it.
        self.calculator = Calculator()
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in"))
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in"))
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in")) 
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in"))
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in")) 
        self.assertEqual(self.calculator.time_calculation("", "", "", ""), ("Invalid parater values passed in"))        

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()