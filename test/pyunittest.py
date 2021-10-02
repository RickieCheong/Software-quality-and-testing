from app.calculator import *
import json
import unittest
from unittest.mock import MagicMock
from app.calculator_form import *
from flask import Flask, flash
from flask import render_template
from main import *
from flask import request

class TestCalculatorForm(unittest.TestCase):
    fake_form = MagicMock()
    app = Flask(__name__)

    def test_battery(self):
        ev_calculator_app.config["WTF_CSRF_ENABLED"] = False  # disable CSRF to prevent context errors
        with ev_calculator_app.app_context():
                form = Calculator_Form(request.form)
                battery_pack_capacity_field = MagicMock()
                battery_pack_capacity_field.data = None
                with self.assertRaises() as e:
                    form.validate_BatteryPackCapacity(battery_pack_capacity_field)
                    self.assertEqual('Field data is num', str(e.exception))


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
                         'Invalid parameter values')
        self.assertEqual(self.calculator.cost_calculation("0", "", "100", "True", "False"),
                         'Invalid parameter values')
        self.assertEqual(self.calculator.cost_calculation("0", "100", "", "False", "True"),
                         'Invalid parameter values')
        self.assertEqual(self.calculator.cost_calculation("0", "100", "100", "", "False"), 'Invalid parameter values')
        self.assertEqual(self.calculator.cost_calculation("0", "100", "100", "True", ""), 'Invalid parameter values')

    def test_time_empty_param(self):
        """
        Purpose : Checking for empty string as parameter to time_calculation
        """
        # Empty values passed in to each and every parameter each to ensure that everything affects it.
        self.calculator = Calculator()
        self.assertEqual(self.calculator.time_calculation("", "100", "100", "80"), "Invalid parameter values passed in")
        self.assertEqual(self.calculator.time_calculation("0", "", "100", "80"), "Invalid parameter values passed in")
        self.assertEqual(self.calculator.time_calculation("0", "100", "", "80"), "Invalid parameter values passed in")
        self.assertEqual(self.calculator.time_calculation("0", "100", "100", ""), "Invalid parameter values passed in")

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

    def test_is_holiday(self):
        """
        Purpose : checking to see if surcharge is True or False
        Purpose : checking to see if valid surcharge is accepted and invalid surcharge is rejected
        """
        self.calculator = Calculator()
        # October 28, a Thursday, normal weekday
        self.assertEqual(self.calculator.is_holiday("2021-10-28"), True)
        # October 29, a friday, Ekka People's day
        self.assertEqual(self.calculator.is_holiday("2021-10-29"), True)
        # October 30, a Saturday, normal weekend
        self.assertEqual(self.calculator.is_holiday("2021-10-30"), False)
        # Extremely old date that lies on a weekday
        self.assertEqual(self.calculator.is_holiday("2001-10-31"), True)

    def test_get_duration(self):
        """
        Purpose : checking to see if the calculations are working properly with the formula given
        """
        # charger configuration set to 8
        self.calculator = Calculator("1000", "0", "100", "2021-10-28", "00:00", "8")
        self.assertAlmostEqual(self.calculator.get_duration(), 2.86, 2)

        # charger configuration set to 1
        self.calculator = Calculator("1000", "0", "100", "2021-10-29", "00:00", "1")
        self.assertAlmostEqual(self.calculator.get_duration(), 500.00, 2)

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

    def test_provide_mean_sum_1(self):
        """
        Purpose : Testing mean sum with surcharges
        """
        # Mock data can be on top of the method at the beginner of the class. We are using that JSON data as our mock api data.
        self.calculator = Calculator("200.6", "0", "100", "11/04/2020", "13:00", "4", "4000")  # Date is initialise to a weekday thus giving us surcharges
        time_str = self.calculator.start_date + " " + self.calculator.start_time  # Time taken would not exceed one hour
        time = datetime.strptime(time_str, "%d/%m/%Y %H:%M")
        y = json.loads(self.json)
        lst_rise = datetime.strptime(y["sunrise"], "%H:%M:%S")
        lst_set = datetime.strptime(y["sunset"], "%H:%M:%S")
        dl = self.calculator.get_day_light_length(time.date())
        si = self.calculator.get_sun_hour(time.date())
        self.assertAlmostEqual(self.calculator.provide_mean_sum(time, 50, lst_rise, lst_set, si, dl), 0.8267321962031)

    def test_provide_mean_sum_2(self):
        """
        Purpose : Testing mean sum without surcharges
        """
        # Mock data can be on top of the method at the beginner of the class. We are using that JSON data as our mock api data.
        self.calculator = Calculator("1000.6", "0", "100", "13/04/2020", "05:00", "4", "4000")  # Date is initialise to a weekend avoiding surcharges
        time_str = self.calculator.start_date + " " + self.calculator.start_time  # Time taken exceeding one hour
        time = datetime.strptime(time_str, "%d/%m/%Y %H:%M")
        y = json.loads(self.json)
        lst_rise = datetime.strptime(y["sunrise"], "%H:%M:%S")
        lst_set = datetime.strptime(y["sunset"], "%H:%M:%S")
        dl = self.calculator.get_day_light_length(time.date())
        si = self.calculator.get_sun_hour(time.date())
        self.assertAlmostEqual(self.calculator.provide_mean_sum(time, 130, lst_rise, lst_set, si, dl), 0.17245995451025942)

    def test_get_day_light_length(self):
        """
        Purpose : Checking get day light length
        """
        # test A
        self.calculator = Calculator("200.6", "0", "100", "11/04/2020", "13:00", "4", "4000")
        date_str = self.calculator.start_date
        date = datetime.strptime(date_str, "%d/%m/%Y")
        string = '{"date":"2020-04-11","sunrise":"06:03:00","sunset":"17:35:00","moonrise":"20:12:00","moonset":"09:07:00","moonPhase":"Waning Gibbous","moonIlluminationPct":68,"minTempC":20,"maxTempC":29,"avgTempC":26,"sunHours":5.4,"uvIndex":6,"location":{"id":"81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8","postcode":"4000","name":"BRISBANE","state":"QLD","latitude":"-27.4660994","longitude":"153.023588","distanceToNearestWeatherStationMetres":2225.7460538928362,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},"hourlyWeatherHistory":[{"hour":0,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":61,"uvIndex":1,"windspeedKph":12,"windDirectionDeg":211,"windDirectionCompass":"SSW","precipitationMm":0.4,"humidityPct":84,"visibilityKm":10,"pressureMb":1015},{"hour":1,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":64,"uvIndex":1,"windspeedKph":12,"windDirectionDeg":238,"windDirectionCompass":"WSW","precipitationMm":0.2,"humidityPct":84,"visibilityKm":10,"pressureMb":1015},{"hour":2,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":67,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":265,"windDirectionCompass":"W","precipitationMm":0.3,"humidityPct":84,"visibilityKm":10,"pressureMb":1014},{"hour":3,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":69,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":292,"windDirectionCompass":"WNW","precipitationMm":0.4,"humidityPct":85,"visibilityKm":9,"pressureMb":1014},{"hour":4,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":59,"uvIndex":1,"windspeedKph":10,"windDirectionDeg":293,"windDirectionCompass":"WNW","precipitationMm":0.2,"humidityPct":84,"visibilityKm":9,"pressureMb":1014},{"hour":5,"tempC":20,"weatherDesc":"Patchy rain possible","cloudCoverPct":48,"uvIndex":1,"windspeedKph":11,"windDirectionDeg":294,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":83,"visibilityKm":10,"pressureMb":1014},{"hour":6,"tempC":21,"weatherDesc":"Patchy rain possible","cloudCoverPct":38,"uvIndex":5,"windspeedKph":11,"windDirectionDeg":296,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":82,"visibilityKm":10,"pressureMb":1014},{"hour":7,"tempC":22,"weatherDesc":"Patchy rain possible","cloudCoverPct":29,"uvIndex":5,"windspeedKph":12,"windDirectionDeg":295,"windDirectionCompass":"WNW","precipitationMm":0.1,"humidityPct":77,"visibilityKm":10,"pressureMb":1014},{"hour":8,"tempC":23,"weatherDesc":"Partly cloudy","cloudCoverPct":21,"uvIndex":6,"windspeedKph":12,"windDirectionDeg":295,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":72,"visibilityKm":10,"pressureMb":1014},{"hour":9,"tempC":24,"weatherDesc":"Partly cloudy","cloudCoverPct":12,"uvIndex":6,"windspeedKph":13,"windDirectionDeg":294,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":68,"visibilityKm":10,"pressureMb":1014},{"hour":10,"tempC":25,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":291,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1013},{"hour":11,"tempC":27,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":287,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":56,"visibilityKm":10,"pressureMb":1012},{"hour":12,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":15,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":284,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":50,"visibilityKm":10,"pressureMb":1011},{"hour":13,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":13,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":281,"windDirectionCompass":"WNW","precipitationMm":0,"humidityPct":47,"visibilityKm":10,"pressureMb":1010},{"hour":14,"tempC":29,"weatherDesc":"Partly cloudy","cloudCoverPct":11,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":279,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":44,"visibilityKm":10,"pressureMb":1010},{"hour":15,"tempC":29,"weatherDesc":"Partly cloudy","cloudCoverPct":9,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":277,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":41,"visibilityKm":10,"pressureMb":1009},{"hour":16,"tempC":28,"weatherDesc":"Partly cloudy","cloudCoverPct":7,"uvIndex":7,"windspeedKph":13,"windDirectionDeg":268,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1009},{"hour":17,"tempC":27,"weatherDesc":"Partly cloudy","cloudCoverPct":4,"uvIndex":7,"windspeedKph":14,"windDirectionDeg":260,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1009},{"hour":18,"tempC":26,"weatherDesc":"Partly cloudy","cloudCoverPct":2,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":252,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":37,"visibilityKm":10,"pressureMb":1009},{"hour":19,"tempC":25,"weatherDesc":"Partly cloudy","cloudCoverPct":8,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":251,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1010},{"hour":20,"tempC":24,"weatherDesc":"Clear","cloudCoverPct":15,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":250,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":38,"visibilityKm":10,"pressureMb":1011},{"hour":21,"tempC":23,"weatherDesc":"Clear","cloudCoverPct":21,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":249,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":39,"visibilityKm":10,"pressureMb":1012},{"hour":22,"tempC":22,"weatherDesc":"Clear","cloudCoverPct":18,"uvIndex":1,"windspeedKph":15,"windDirectionDeg":256,"windDirectionCompass":"WSW","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1011},{"hour":23,"tempC":22,"weatherDesc":"Partly cloudy","cloudCoverPct":14,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":263,"windDirectionCompass":"W","precipitationMm":0,"humidityPct":40,"visibilityKm":10,"pressureMb":1011}]}'
        temp = json.loads(string)
        lst_rise = temp["sunrise"].split(":")
        lst_set = temp["sunset"].split(":")
        rise_value = format(int(lst_rise[0]) + int(lst_rise[1]) / 60, '.2f')
        set_value = format(int(lst_set[0]) + int(lst_set[1]) / 60, '.2f')
        expected = float(set_value) - float(rise_value)
        self.assertEqual(self.calculator.get_day_light_length(str(date.date())), expected)

        # test B
        self.calculator = Calculator("200.6", "0", "100", "09/04/2020", "15:00", "4", "4000")
        date_str = self.calculator.start_date
        date = datetime.strptime(date_str, "%d/%m/%Y")
        string = '{"date":"2020-04-09","sunrise":"06:02:00","sunset":"17:37:00","moonrise":"18:42:00","moonset":"06:52:00","moonPhase":"Waxing Gibbous","moonIlluminationPct":83,"minTempC":20,"maxTempC":24,"avgTempC":23,"sunHours":4.2,"uvIndex":5,"location":{"id":"81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8","postcode":"4000","name":"BRISBANE","state":"QLD","latitude":"-27.4660994","longitude":"153.023588","distanceToNearestWeatherStationMetres":2225.7460538928362,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},"hourlyWeatherHistory":[{"hour":0,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":59,"uvIndex":1,"windspeedKph":17,"windDirectionDeg":155,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":74,"visibilityKm":10,"pressureMb":1020},{"hour":5,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":76,"uvIndex":1,"windspeedKph":20,"windDirectionDeg":168,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":76,"visibilityKm":10,"pressureMb":1021},{"hour":6,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":82,"uvIndex":5,"windspeedKph":21,"windDirectionDeg":168,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":76,"visibilityKm":10,"pressureMb":1021},{"hour":7,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":87,"uvIndex":5,"windspeedKph":22,"windDirectionDeg":161,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":75,"visibilityKm":10,"pressureMb":1022},{"hour":8,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":92,"uvIndex":5,"windspeedKph":22,"windDirectionDeg":154,"windDirectionCompass":"SSE","precipitationMm":0.2,"humidityPct":73,"visibilityKm":10,"pressureMb":1022},{"hour":9,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":96,"uvIndex":5,"windspeedKph":23,"windDirectionDeg":147,"windDirectionCompass":"SSE","precipitationMm":0.2,"humidityPct":72,"visibilityKm":10,"pressureMb":1023},{"hour":10,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":91,"uvIndex":5,"windspeedKph":23,"windDirectionDeg":142,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":71,"visibilityKm":10,"pressureMb":1022},{"hour":11,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":86,"uvIndex":5,"windspeedKph":24,"windDirectionDeg":136,"windDirectionCompass":"SE","precipitationMm":0.3,"humidityPct":69,"visibilityKm":10,"pressureMb":1022},{"hour":12,"tempC":24,"weatherDesc":"Light rain shower","cloudCoverPct":81,"uvIndex":5,"windspeedKph":24,"windDirectionDeg":131,"windDirectionCompass":"SE","precipitationMm":0.4,"humidityPct":67,"visibilityKm":10,"pressureMb":1022},{"hour":13,"tempC":24,"weatherDesc":"Light rain shower","cloudCoverPct":78,"uvIndex":5,"windspeedKph":23,"windDirectionDeg":130,"windDirectionCompass":"SE","precipitationMm":0.2,"humidityPct":67,"visibilityKm":10,"pressureMb":1021},{"hour":14,"tempC":24,"weatherDesc":"Light rain shower","cloudCoverPct":75,"uvIndex":5,"windspeedKph":23,"windDirectionDeg":129,"windDirectionCompass":"SE","precipitationMm":0.5,"humidityPct":66,"visibilityKm":10,"pressureMb":1021},{"hour":15,"tempC":24,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":5,"windspeedKph":22,"windDirectionDeg":128,"windDirectionCompass":"SE","precipitationMm":0.7,"humidityPct":65,"visibilityKm":10,"pressureMb":1021},{"hour":16,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":5,"windspeedKph":21,"windDirectionDeg":129,"windDirectionCompass":"SE","precipitationMm":0.4,"humidityPct":66,"visibilityKm":10,"pressureMb":1021},{"hour":17,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":73,"uvIndex":5,"windspeedKph":20,"windDirectionDeg":130,"windDirectionCompass":"SE","precipitationMm":0.2,"humidityPct":68,"visibilityKm":10,"pressureMb":1022},{"hour":18,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":73,"uvIndex":1,"windspeedKph":19,"windDirectionDeg":131,"windDirectionCompass":"SE","precipitationMm":0.3,"humidityPct":69,"visibilityKm":10,"pressureMb":1022},{"hour":19,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":73,"uvIndex":1,"windspeedKph":18,"windDirectionDeg":131,"windDirectionCompass":"SE","precipitationMm":0.2,"humidityPct":71,"visibilityKm":10,"pressureMb":1022},{"hour":20,"tempC":22,"weatherDesc":"Patchy rain possible","cloudCoverPct":73,"uvIndex":1,"windspeedKph":17,"windDirectionDeg":131,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":73,"visibilityKm":10,"pressureMb":1023},{"hour":21,"tempC":22,"weatherDesc":"Patchy rain possible","cloudCoverPct":73,"uvIndex":1,"windspeedKph":16,"windDirectionDeg":131,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":74,"visibilityKm":10,"pressureMb":1023},{"hour":22,"tempC":22,"weatherDesc":"Patchy rain possible","cloudCoverPct":72,"uvIndex":1,"windspeedKph":14,"windDirectionDeg":128,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":75,"visibilityKm":10,"pressureMb":1023},{"hour":23,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":1,"windspeedKph":13,"windDirectionDeg":125,"windDirectionCompass":"SE","precipitationMm":0.3,"humidityPct":76,"visibilityKm":10,"pressureMb":1023},{"hour":1,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":61,"uvIndex":1,"windspeedKph":18,"windDirectionDeg":159,"windDirectionCompass":"SSE","precipitationMm":0,"humidityPct":75,"visibilityKm":10,"pressureMb":1020},{"hour":2,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":63,"uvIndex":1,"windspeedKph":18,"windDirectionDeg":163,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":75,"visibilityKm":10,"pressureMb":1020},{"hour":3,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":65,"uvIndex":1,"windspeedKph":19,"windDirectionDeg":168,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":76,"visibilityKm":10,"pressureMb":1020},{"hour":4,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":70,"uvIndex":1,"windspeedKph":19,"windDirectionDeg":168,"windDirectionCompass":"SSE","precipitationMm":0.1,"humidityPct":76,"visibilityKm":10,"pressureMb":1020}]}'
        temp = json.loads(string)
        lst_rise = temp["sunrise"].split(":")
        lst_set = temp["sunset"].split(":")
        rise_value = format(int(lst_rise[0]) + int(lst_rise[1]) / 60, '.2f')
        set_value = format(int(lst_set[0]) + int(lst_set[1]) / 60, '.2f')
        expected = float(set_value) - float(rise_value)
        self.assertEqual(self.calculator.get_day_light_length(str(date.date())), expected)

    def test_get_cloud_cover(self):
        """
        Purpose : Checking for cloud cover method inside calculator
        """
        # test A
        self.calculator = Calculator("200.6", "0", "100", "11/04/2020", "13:00", "4", "4000")
        date_str = self.calculator.start_date
        date = datetime.strptime(date_str, "%d/%m/%Y")
        self.assertEqual(self.calculator.get_cloud_cover(date.date(), 5), 48)

        # test B
        self.calculator = Calculator("200.6", "0", "100", "11/04/2020", "13:00", "4", "4000")
        date_str = self.calculator.start_date
        date = datetime.strptime(date_str, "%d/%m/%Y")
        self.assertEqual(self.calculator.get_cloud_cover(date.date(), 21), 21)

        # test C
        self.calculator = Calculator("200.6", "0", "100", "09/04/2020", "15:00", "4", "4000")
        date_str = self.calculator.start_date
        date = datetime.strptime(date_str, "%d/%m/%Y")
        self.assertEqual(self.calculator.get_cloud_cover(date.date(), 30), 0)

    def test_getID(self):
        """
        Purpose : checks to see if getID returns an appropriate result
        """
        self.calculator = Calculator("", "", "", "", "", "", "4000")
        cotton = '[{"id":"81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8","postcode":"4000","name":"BRISBANE","state":"QLD","latitude":"-27.4660994","longitude":"153.023588","distanceToNearestWeatherStationMetres":2225.7460538928362,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"4dbd2be6-d7be-4698-aa33-0018f337e0de","postcode":"4000","name":"BRISBANE ADELAIDE STREET","state":"QLD","latitude":"-27.4666186","longitude":"153.027371","distanceToNearestWeatherStationMetres":1944.291037581407,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"c6ff84b6-4b65-4dd4-8daf-cf13f3fbb829","postcode":"4000","name":"BRISBANE CITY","state":"QLD","latitude":"-27.4698","longitude":"153.025","distanceToNearestWeatherStationMetres":1837.522855904486,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"bf9f7faf-c664-4593-80cb-155416095511","postcode":"4000","name":"BRISBANE CITY DC","state":"QLD","latitude":"-27.4679","longitude":"153.028","distanceToNearestWeatherStationMetres":1792.7293662813534,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"99d0ffc4-f32b-4d06-883a-8ca29d8db601","postcode":"4000","name":"BRISBANE GPO","state":"QLD","latitude":"-27.4679","longitude":"153.028","distanceToNearestWeatherStationMetres":1792.7293662813534,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"d026d69c-3616-4e36-84f6-77eba58c71b4","postcode":"4000","name":"BRISBANE-CITY","state":"QLD","latitude":"-27.4698","longitude":"153.025","distanceToNearestWeatherStationMetres":1837.522855904486,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"dec0048f-4565-4613-a3c9-14d8217167db","postcode":"4000","name":"PARLIAMENT HOUSE","state":"QLD","latitude":"-27.4754","longitude":"153.027","distanceToNearestWeatherStationMetres":1318.5927708639924,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"b54c90b9-db4e-47e8-a9d8-7f463d4b51b3","postcode":"4000","name":"PETRIE TERRACE","state":"QLD","latitude":"-27.4626","longitude":"153.013","distanceToNearestWeatherStationMetres":3259.541746946261,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},{"id":"6e2b8349-4793-44b6-87a7-a737b2067280","postcode":"4000","name":"SPRING HILL","state":"QLD","latitude":"-27.46","longitude":"153.026","distanceToNearestWeatherStationMetres":2639.889855918334,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}}]'
        data = json.loads(cotton)
        id = data[0]["id"]
        self.assertEqual(self.calculator.getID(), id)

        # purposely given wrong postcode
        self.calculator = Calculator("", "", "", "", "", "", "10000")
        self.assertEqual(self.calculator.getID(), "Failed API ID retrieval")

    def test_get_sun_hour(self):
        """
        Purpose : checks to see if get_sun_hour returns an appropriate value
        """
        self.calculator = Calculator("", "", "", "2020-12-12", "00:00", "", "4000")
        cotton = '{"date":"2020-12-12","sunrise":"04:46:00","sunset":"18:37:00","moonrise":"02:32:00","moonset":"15:54:00","moonPhase":"Waning Crescent","moonIlluminationPct":9,"minTempC":19,"maxTempC":24,"avgTempC":22,"sunHours":3.7,"uvIndex":5,"location":{"id":"81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8","postcode":"4000","name":"BRISBANE","state":"QLD","latitude":"-27.4660994","longitude":"153.023588","distanceToNearestWeatherStationMetres":2225.7460538928362,"nearestWeatherStation":{"name":"BRISBANE","state":"QLD","latitude":"-27.4808","longitude":"153.0389"}},"hourlyWeatherHistory":[{"hour":0,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":71,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":151,"windDirectionCompass":"SSE","precipitationMm":0.4,"humidityPct":75,"visibilityKm":10,"pressureMb":1018},{"hour":1,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":154,"windDirectionCompass":"SSE","precipitationMm":0.2,"humidityPct":77,"visibilityKm":10,"pressureMb":1018},{"hour":2,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":72,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":158,"windDirectionCompass":"SSE","precipitationMm":0.7,"humidityPct":78,"visibilityKm":10,"pressureMb":1018},{"hour":3,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":73,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":161,"windDirectionCompass":"SSE","precipitationMm":0.9,"humidityPct":80,"visibilityKm":10,"pressureMb":1018},{"hour":4,"tempC":19,"weatherDesc":"Light rain shower","cloudCoverPct":75,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":159,"windDirectionCompass":"SSE","precipitationMm":0.4,"humidityPct":80,"visibilityKm":10,"pressureMb":1018},{"hour":5,"tempC":19,"weatherDesc":"Light rain shower","cloudCoverPct":77,"uvIndex":1,"windspeedKph":22,"windDirectionDeg":158,"windDirectionCompass":"SSE","precipitationMm":0.6,"humidityPct":80,"visibilityKm":10,"pressureMb":1019},{"hour":6,"tempC":19,"weatherDesc":"Light rain shower","cloudCoverPct":79,"uvIndex":4,"windspeedKph":22,"windDirectionDeg":156,"windDirectionCompass":"SSE","precipitationMm":0.8,"humidityPct":80,"visibilityKm":10,"pressureMb":1019},{"hour":7,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":75,"uvIndex":4,"windspeedKph":21,"windDirectionDeg":156,"windDirectionCompass":"SSE","precipitationMm":0.4,"humidityPct":77,"visibilityKm":10,"pressureMb":1019},{"hour":8,"tempC":20,"weatherDesc":"Light rain shower","cloudCoverPct":71,"uvIndex":5,"windspeedKph":21,"windDirectionDeg":156,"windDirectionCompass":"SSE","precipitationMm":0.6,"humidityPct":74,"visibilityKm":10,"pressureMb":1019},{"hour":9,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":66,"uvIndex":5,"windspeedKph":20,"windDirectionDeg":155,"windDirectionCompass":"SSE","precipitationMm":0.8,"humidityPct":71,"visibilityKm":10,"pressureMb":1020},{"hour":10,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":67,"uvIndex":5,"windspeedKph":20,"windDirectionDeg":152,"windDirectionCompass":"SSE","precipitationMm":0.4,"humidityPct":68,"visibilityKm":10,"pressureMb":1019},{"hour":11,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":68,"uvIndex":5,"windspeedKph":21,"windDirectionDeg":148,"windDirectionCompass":"SSE","precipitationMm":0.2,"humidityPct":64,"visibilityKm":10,"pressureMb":1019},{"hour":12,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":70,"uvIndex":5,"windspeedKph":21,"windDirectionDeg":145,"windDirectionCompass":"SE","precipitationMm":0.3,"humidityPct":61,"visibilityKm":10,"pressureMb":1018},{"hour":13,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":67,"uvIndex":5,"windspeedKph":22,"windDirectionDeg":143,"windDirectionCompass":"SE","precipitationMm":0.2,"humidityPct":61,"visibilityKm":10,"pressureMb":1017},{"hour":14,"tempC":24,"weatherDesc":"Patchy rain possible","cloudCoverPct":64,"uvIndex":5,"windspeedKph":23,"windDirectionDeg":140,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":60,"visibilityKm":10,"pressureMb":1017},{"hour":15,"tempC":24,"weatherDesc":"Patchy rain possible","cloudCoverPct":62,"uvIndex":5,"windspeedKph":24,"windDirectionDeg":138,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":60,"visibilityKm":10,"pressureMb":1016},{"hour":16,"tempC":23,"weatherDesc":"Patchy rain possible","cloudCoverPct":60,"uvIndex":5,"windspeedKph":25,"windDirectionDeg":141,"windDirectionCompass":"SE","precipitationMm":0,"humidityPct":62,"visibilityKm":10,"pressureMb":1016},{"hour":17,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":58,"uvIndex":5,"windspeedKph":25,"windDirectionDeg":143,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":64,"visibilityKm":10,"pressureMb":1016},{"hour":18,"tempC":23,"weatherDesc":"Light rain shower","cloudCoverPct":56,"uvIndex":1,"windspeedKph":25,"windDirectionDeg":145,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":66,"visibilityKm":10,"pressureMb":1016},{"hour":19,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":61,"uvIndex":1,"windspeedKph":23,"windDirectionDeg":141,"windDirectionCompass":"SE","precipitationMm":0.1,"humidityPct":70,"visibilityKm":9,"pressureMb":1016},{"hour":20,"tempC":22,"weatherDesc":"Light rain shower","cloudCoverPct":66,"uvIndex":1,"windspeedKph":22,"windDirectionDeg":136,"windDirectionCompass":"SE","precipitationMm":0.6,"humidityPct":73,"visibilityKm":9,"pressureMb":1016},{"hour":21,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":71,"uvIndex":1,"windspeedKph":21,"windDirectionDeg":132,"windDirectionCompass":"SE","precipitationMm":0.8,"humidityPct":76,"visibilityKm":8,"pressureMb":1017},{"hour":22,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":77,"uvIndex":1,"windspeedKph":20,"windDirectionDeg":128,"windDirectionCompass":"SE","precipitationMm":0.4,"humidityPct":79,"visibilityKm":8,"pressureMb":1016},{"hour":23,"tempC":21,"weatherDesc":"Light rain shower","cloudCoverPct":84,"uvIndex":1,"windspeedKph":20,"windDirectionDeg":124,"windDirectionCompass":"SE","precipitationMm":1.3,"humidityPct":81,"visibilityKm":8,"pressureMb":1016}]}'
        temp = json.loads(cotton)
        res = temp["sunHours"]
        self.assertEqual(self.calculator.get_sun_hour("2020-12-12"), res)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)
    calculator_form_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorForm)
    unittest.TextTestRunner(verbosity=2).run(calculator_form_suite)


main()