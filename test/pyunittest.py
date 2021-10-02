from app.calculator import *
import json
import unittest


class TestCalculator(unittest.TestCase):
    json = '{"date":"2020-04-11","sunrise":"06:03:00","sunset":"17:35:00","moonrise":"20:12:00","moonset":"09:07:00","moonPhase":"Waning Gibbous","moonIlluminationPct":68,"minTempC":20,"maxTempC":29,"avgTempC":26,"sunHours":5.4,"uvIndex":6,"location":{"id":"81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8","postcode":"4000","name":"BRISBANE","state":"QLD","latitude":"-27.4660994","longitude":"153.023588","distanceToNearestWeatherStationMetres":2225.7460538928362,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},"hourlyWeatherHistory":[{"hour":18,"tempC":26,"weatherDesc":"Partly cloudy","cloudCoverPct":2,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":252,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":37,"visibilityKm":10,"pressureMb":1009},{"hour":0,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":61,"uvIndex":1,"windspeedKph":12,"windDirectionDeg":211,"windDirectionCompass":"SSW","precipitationMm":0.4,"humidityPct":84,"visibilityKm":10,"pressureMb":1015},{"hour":1,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":64,"uvIndex":1,"windspeedKph":12,"windDirectionDeg":238,"windDirectionCompass":"WSW","precipitationMm":0.2,"humidityPct":84,"visibilityKm":10,"pressureMb":1015},{"hour":2,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":67,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":265,"windDirectionCompass":"W","precipitationMm":0.3,"humidityPct":84,"visibilityKm":10,"pressureMb":1014},{"hour":3,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":69,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0.4,"humidityPct":85,"visibilityKm":9,"pressureMb":1014},{"hour":4,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":59,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":293,"windDirectionCompass":"WNW","precipitationMm":0.2,"humidityPct":84,"visibilityKm":9,"pressureMb":1014},{"hour":5,"tempC":20,"weatherDesc":"Patchy rain possible","cloudCoverPct":48,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":294,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":83,"visibilityKm":10,"pressureMb":1014},{"hour":6,"tempC":21,"weatherDesc":"Patchy rain possible","cloudCoverPct":38,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":296,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":82,"visibilityKm":10,"pressureMb":1014},{"hour":7,"tempC":22,"weatherDesc":"Patchy rain possible","cloudCoverPct":29,"uvIndex":5,"windspeedKph":12,"windDirectionDeg":295,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":77,"visibilityKm":10,"pressureMb":1014},{"hour":8,"tempC":23,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":6,"windspeedKph":12,"windDirectionDeg":295,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":72,"visibilityKm":10,"pressureMb":1014},{"hour":9,"tempC":24,"weatherDesc":"Partly cloudy","cloudCoverPct":12,"uvIndex":6,"windspeedKph":13,"windDirectionDeg":294,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1014},{"hour":10,"tempC":25,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":291,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1013},{"hour":11,"tempC":27,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":287,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":56,"visibilityKm":10,"pressureMb":1012},{"hour":12,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":15,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1011},{"hour":13,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":281,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":47,"visibilityKm":10,"pressureMb":1010},{"hour":14,"tempC":29,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":279,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1010},{"hour":15,"tempC":29,"weatherDesc":"Partly cloudy","cloudCoverPct":9,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":277,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":41,"visibilityKm":10,"pressureMb":1009},{"hour":16,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":268,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1009},{"hour":17,"tempC":27,"weatherDesc":"Partly cloudy","cloudCoverPct":4,"uvIndex":7,"windspeedKph":14,"windDirectionDeg":260,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":25,"weatherDesc":"Partly cloudy","cloudCoverPct":8,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":251,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":24,"weatherDesc":"Clear","cloudCoverPct":15,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":250,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":23,"weatherDesc":"Clear","cloudCoverPct":21,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":249,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":22,"weatherDesc":"Clear","cloudCoverPct":18,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":256,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1011},{"hour":23,"tempC":22,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":263,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1011}]}'

    # you may create more test methods
    # you may add parameters to test methods
    # this is an example
    def test_cost_empty_param(self):
        """
        Purpose : Checking for empty string as parameter to cost_calculation
        """
        # Empty values passed in to each and every parameter each to ensure that everything affects it.
        self.calculator = Calculator()
        self.assertEqual(self.calculator.cost_calculation("", "100", "100", "True", "True"),
                         ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "", "100", "True", "False"),
                         ('Invalid parameter values'))
        self.assertEqual(self.calculator.cost_calculation("0", "100", "", "False", "True"),
                         ('Invalid parameter values'))
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
        self.calculator = Calculator("17.6", "100", "100", "13/04/2020", "06:00", "8", "4000")
        is_peak = datetime.strptime("06:00", "%H:%M")
        date_format = datetime.strptime("13/04/2020", "%d/%m/%Y")
        is_holiday = self.calculator.is_holiday(str(date_format.date()))
        is_peak = self.calculator.is_peak(is_peak.hour)
        self.assertAlmostEqual(float(self.calculator.cost_calculation("0", "100", "17", is_peak, is_holiday)), 18.7)
        self.assertAlmostEqual(
            float(self.calculator.time_calculation("0", "100", "100", str(self.calculator.POWER[7]))), 0.2857142857)

    def test_cost_1b(self):
        """
        Purpose : Checking for non peak hours as well as no surchages.
        """
        # Ensuring that the cost and time work for both surchages and non surchages as well as peak and non peak hours
        self.calculator = Calculator("17.6", "100", "100", "11/04/2020", "13:00", "8", "4000")
        is_peak = datetime.strptime("13:00", "%H:%M")
        date_format = datetime.strptime("11/04/2020", "%d/%m/%Y")
        is_holiday = self.calculator.is_holiday(str(date_format.date()))
        is_peak = self.calculator.is_peak(is_peak.hour)
        self.assertAlmostEqual(int(self.calculator.cost_calculation("0", "100", "17.6", is_peak, is_holiday)), 17)
        self.assertAlmostEqual(self.calculator.time_calculation("0", "100", "17.6", str(self.calculator.POWER[7])),
                               0.0502857142)

    def test_is_peak(self):
        """
        Purpose : Checking for peak hour
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

    def test_solar_energy(self):
        """
        Purpose : Ensure that solar energy would work for date that are later than the current date
        """
        self.calculator = Calculator("17.6", "0", "100", "11/04/2022", "13:00", "8", "4000")
        self.assertAlmostEqual(self.calculator.solar_energy(self.calculator.start_date), 8.959827984966)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()