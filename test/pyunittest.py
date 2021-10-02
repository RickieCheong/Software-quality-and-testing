from app.calculator import *
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
        self.assertEqual(self.calculator.time_calculation("", "100", "100", "80"), ("Invalid parater values passed in"))
        self.assertEqual(self.calculator.time_calculation("0", "", "100", "80"), ("Invalid parater values passed in"))
        self.assertEqual(self.calculator.time_calculation("0", "100", "", "80"), ("Invalid parater values passed in")) 
        self.assertEqual(self.calculator.time_calculation("0", "100", "100", ""), ("Invalid parater values passed in"))

    def test_cost_1a(self):
        """
        Purpose : Checking for peak hours as well as surchages.
        """
        # Ensuring that the cost and time work for both surchages and non surchages as well as peak and non peak hours
        self.calculator = Calculator("17.6","100","100","13/04/2020","06:00","8","4000")
        is_peak = datetime.strptime("06:00", "%H:%M")
        date_format = datetime.strptime("13/04/2020","%d/%m/%Y")
        is_holiday = calculator.is_holiday(str(date_format.date()))
        is_peak = calculator.is_peak(is_peak.hour)
        self.assertAlmostEqual(calculator.cost_calculation("0","100","17", is_peak, is_holiday), 18.7, "Value does not match the expected output")
        self.assertAlmostEqual(self.calculator.time_calculation("0", "100", "100", ""), 0.286,("Expected output does not match the actual output for the time part"))


    def test_cost_1b(self):
        """
        Purpose : Checking for non peak hours as well as no surchages.
        """
        # Ensuring that the cost and time work for both surchages and non surchages as well as peak and non peak hours
        self.calculator = Calculator("17.6","100","100","11/04/2020","13:00","8","4000")
        is_peak = datetime.strptime("13:00", "%H:%M")
        date_format = datetime.strptime("11/04/2020","%d/%m/%Y")
        is_holiday = calculator.is_holiday(str(date_format.date()))
        is_peak = calculator.is_peak(is_peak.hour)
        self.assertAlmostEqual(calculator.cost_calculation("0","100","17.6", is_peak, is_holiday), 17, "Value does not match the expected output")
        self.assertAlmostEqual(self.calculator.time_calculation("0", "100", "17.6", calculator.POWER[7]), 0.05028, ("Expected output does not match the actual output for the time part"))

        
        
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()