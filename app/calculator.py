from datetime import date, datetime, timedelta
from time import time
import requests
import holidays


class Calculator:
    POWER = [2, 3.6, 7.2, 11, 22, 36, 90, 350]
    COIN = [0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.3, 0.5]

    # you can choose to initialise variables here, if needed.
    def __init__(self, battery_capacity="", initial_charge="", final_charge="", start_date="", start_time="", charger_configuration="", postcode=""):
        self.battery_capacity = battery_capacity
        self.initial_charge = initial_charge
        self.final_charge = final_charge
        self.start_date = start_date
        self.start_time = start_time
        self.charger_configuration = charger_configuration
        self.postcode = postcode
        self.id = self.getID()
        
    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, is_peak, is_holiday):
        try:
            if is_peak:
                base_price = 100
            else:
                base_price = 50

            if is_holiday:
                surcharge_factor = 1.1
            else:
                surcharge_factor = 1

            cost = (int(final_state) - int(initial_state)) / 100 * float(capacity) * base_price / 100 * surcharge_factor
            cost = cost - self.solar_energy(self.start_date)
        except ValueError or TypeError:
            return "Invalid parameter values"
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, power):
        try:
            time = (int(final_state) - int(initial_state)) / 100 * float(capacity) / int(power)
        except ValueError or TypeError:
            return "Invalid parameter values passed in"
        return time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def is_holiday(self, start_date):
        date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        surcharge = False
        """
        Checking for weekday
        """
        if date_obj.weekday() < 5:
            surcharge = True
        """
        Checking for holiday
        """
        for i in holidays.Australia(years=date_obj.year).items():
            if i[0].strftime('%Y-%m-%d') == start_date:
                surcharge = True
        return surcharge

    def is_peak(self, hour):
        peak = False
        if 6 <= hour < 18:
            peak = True
        return peak

    def get_duration(self):
        calc = ((int(self.final_charge) - int(self.initial_charge))/100) * int(self.battery_capacity) / self.POWER[int(self.charger_configuration)-1]
        return calc

    # to be acquired through API
    def getID(self):
        postcode = self.postcode
        try:
            response = requests.get("http://118.138.246.158/api/v1/location?postcode=" + str(postcode))
            data = response.json()
            id = data[0]["id"]
        except KeyError:
            return KeyError("Failed API ID retrieval")
        return id

    # to be acquired through API
    def get_sun_hour(self, moving_date):
        date_obj = datetime.strptime(str(moving_date), '%Y-%m-%d')
        response = requests.get("http://118.138.246.158/api/v1/weather?location=" + str(self.id) + "&date=" + str(date_obj.strftime('%Y-%m-%d')))
        temp = response.json()
        return temp["sunHours"]

    # to be acquired through API
    def get_day_light_length(self, moving_date):
        date_obj = datetime.strptime(str(moving_date), '%Y-%m-%d')
        response = requests.get("http://118.138.246.158/api/v1/weather?location=" + str(self.id) + "&date=" + str(date_obj.strftime('%Y-%m-%d')))
        temp = response.json()
        lst_rise = temp["sunrise"].split(":")
        lst_set = temp["sunset"].split(":")
        rise_value = format(int(lst_rise[0]) + int(lst_rise[1])/60,'.2f')
        set_value = format(int(lst_set[0]) + int(lst_set[1])/60,'.2f')
        return float(set_value) - float(rise_value)

    # to be acquired through API
    def get_cloud_cover(self, moving_date, time_loc):
        date_obj = datetime.strptime(str(moving_date), '%Y-%m-%d')
        response = requests.get("http://118.138.246.158/api/v1/weather?location=" + str(self.id) + "&date=" + str(date_obj.strftime('%Y-%m-%d')))
        temp = response.json()
        temp = temp["hourlyWeatherHistory"]
        for i in range(len(temp)):
            if temp[i]["hour"] == time_loc:
                return temp[i]["cloudCoverPct"]
        return 0

    def calculate_solar_energy(self):
        total = self.solar_energy(self.start_date)
        return total

    def solar_energy(self, date):
        res = date + " " + self.start_time
        res = datetime.strptime(res, '%d/%m/%Y %H:%M')
        while res.year > datetime.now().year or res.date() > datetime.now().date():
            res = res - timedelta(days = 365)
        dl = self.get_day_light_length(res.date())
        si = self.get_sun_hour(res.date())
        time_taken = self.time_calculation(int(self.initial_charge),int(self.final_charge),float(self.battery_capacity), self.POWER[int(self.charger_configuration)-1])
        time_taken = int(time_taken * 60)
        response = requests.get("http://118.138.246.158/api/v1/weather?location=" + str(self.id) + "&date=" + str(res.date()))
        temp = response.json()
        lst_rise = datetime.strptime(temp["sunrise"], "%H:%M:%S")
        lst_set = datetime.strptime(temp["sunset"], "%H:%M:%S")
        total = self.provide_mean_sum(res, time_taken, lst_rise, lst_set, si, dl)
        return total

    def provide_mean_sum(self, time, time_taken, lst_rise, lst_set, si, dl):
        time_precedence = 3 
        res = time
        initial_hour = res.hour
        res = res + timedelta(minutes = time_taken)
        final_hour = res.hour
        if time.minute + time_taken > 60:
            initial_net = (60 - time.minute) / 60
        else:
            initial_net = (res.minute - time.minute)/60
        final_net = res.minute/60
        total = 0
        for j in range(time_precedence):
            for i in range(initial_hour, final_hour+1, 1):
                if lst_rise.hour<i<lst_set.hour:
                    cc = self.get_cloud_cover(res.date(), i)
                    if self.is_peak(i):
                        mult = 1
                    else:
                        mult = 0.5
                    if i == initial_hour:
                        calc = si * initial_net/dl * (1-(cc/100)) * 50 * 0.20 # solar energy
                        net = (self.POWER[int(self.charger_configuration)-1]*initial_net) - calc
                        if self.is_holiday(str(res.date())):
                            cost = self.COIN[int(self.charger_configuration)-1] * net * 1.1 * mult
                        else:
                            cost = self.COIN[int(self.charger_configuration)-1] * net * mult

                    elif i == final_hour:
                        calc = si * final_net/dl * (1-(cc/100)) * 50 * 0.20 # solar energy
                        net = (self.POWER[int(self.charger_configuration)-1] * final_net) - calc
                        if self.is_holiday(str(res.date())):
                            cost = self.COIN[int(self.charger_configuration)-1] * net * 1.1 * mult
                        else:
                            cost = self.COIN[int(self.charger_configuration)-1] * net * mult
                    else:
                        calc = si * 1/dl * (1-(cc/100)) * 50 * 0.20 # solar energy
                        net = (self.POWER[int(self.charger_configuration)-1] * 1) - calc
                        if self.is_holiday(str(res.date())):
                            cost = self.COIN[int(self.charger_configuration)-1] * net * 1.1 * mult
                        else:
                            cost = self.COIN[int(self.charger_configuration)-1] * net * mult
                    total = total + cost
            res = res - timedelta(days=365)
        return total / 3


#Test case 1 
calculator = Calculator("17.6","100","100","11/04/2020","13:00","8","4000")
is_peak = datetime.strptime("13:00", "%H:%M")
date_format = datetime.strptime("11/04/2020","%d/%m/%Y")
is_holiday = calculator.is_holiday(str(date_format.date()))
is_peak = calculator.is_peak(is_peak.hour)
print(calculator.cost_calculation("0","100","17.6", is_peak, is_holiday))
print(calculator.time_calculation("0", "100", "17.6", str(calculator.POWER[7])))
# cost = calculator.cost_calculation(initial_charge, final_charge, battery_capacity, is_peak, is_holiday)

#time = calculator.time_calculation(initial_charge, final_charge, battery_capacity, power)
#print(temp.cost_calculation("20","80","82",False,False))
