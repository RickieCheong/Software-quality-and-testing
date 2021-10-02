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
        self.assertAlmostEqual(float(calculator.cost_calculation("0","100","17", is_peak, is_holiday)), 18.7)
        self.assertAlmostEqual(float(self.calculator.time_calculation("0", "100", "100", str(calculator.POWER[7]))), 0.2857142857)


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
        self.assertAlmostEqual(int(calculator.cost_calculation("0","100","17.6", is_peak, is_holiday)), 17)
        self.assertAlmostEqual(self.calculator.time_calculation("0", "100", "17.6", str(calculator.POWER[7])), 0.0502857142)

    def test_is_peak(self):
        """
        Purpose : Checking if it accepts valid peak hour and refuses invalid peak hour
        """
        # A : hour >= 6 / B : hour < 18
        self.calculator = Calculator()
        # A = False
        self.assertEqual(self.calculator.is_peak(5), False)
        # A = True
        self.assertEqual(self.calculator.is_peak(6), True)
        # B = True
        self.assertEqual(self.calculator.is_peak(17), True)
        # B = False
        self.assertEqual(self.calculator.is_peak(18), False)
        
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()