from datetime import datetime
import requests
import holidays

class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self, battery_capacity, initial_charge, final_charge, start_date, start_time, charger_configuration, postcode):
        self.battery_capacity = battery_capacity
        self.initial_charge = initial_charge
        self.final_charge = final_charge
        self.start_date = start_date
        self.start_time = start_time
        self.charger_configuration = charger_configuration
        self.postcode = postcode

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, is_peak, is_holiday):
        if is_peak:
            base_price = 100
        else:
            base_price = 50

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (final_state - initial_state) / 100 * capacity * base_price / 100 * surcharge_factor
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        time = (final_state - initial_state) / 100 * capacity / power
        return time


    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        date_obj = datetime.strptime(start_date, '%d/%m/%Y')
        surcharge = False
        """
        Checking for weekday
        """
        if date_obj.weekday() < 5:
            surcharge = True
        """
        Checking for holiday
        """
        for i in holidays.Australia(years = date_obj.year).items():
            if str(i[0].strftime('%d/%m/%Y')) == start_date:
                surcharge = True
        return surcharge

    def is_peak(self):
        time = self.start_time
        data = time.split(":")
        peak = False
        if int(data[0]) >= 6 and int(data[0]) < 18:
            peak = True
        print(peak)

    def peak_period(self, start_time):
        pass

    def get_duration(self, start_time):
        pass

    # to be acquired through API
    def get_sun_hour(self, sun_hour):
        pass

    # to be acquired through API
    def get_solar_energy_duration(self, start_time):
        pass

    # to be acquired through API
    def get_day_light_length(self, start_time):
        pass

    # to be acquired through API
    def get_solar_insolation(self, solar_insolation):
        pass

    # to be acquired through API
    def get_cloud_cover(self):
        pass

    def calculate_solar_energy(self):
        pass


