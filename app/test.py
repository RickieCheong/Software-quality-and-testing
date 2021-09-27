import holidays
import requests
from datetime import datetime

"""
for i in holidays.Australia(years = 2021).items():
    date_obj = datetime.strptime("27/12/2021", '%d/%m/%Y')
    if str(i[0].strftime('%d/%m/%Y')) == "27/12/2021":
        surcharge = True
        
response = requests.get("http://118.138.246.158/api/v1/location?postcode=3800")
temp = response.json()
print(temp[0]["id"])

response = requests.get("http://118.138.246.158/api/v1/weather?location=" + str(temp[0]["id"]) + "&date=" + "2021-09-09")
print("http://118.138.246.158/api/v1/weather?location=" + str(temp[0]["id"]) + "&date=" + "2021-09-09")
temp = response.json()
print(temp)
print(temp["hourlyWeatherHistory"][17]["cloudCoverPct"])

lst_rise = temp["sunrise"].split(":")
lst_set = temp["sunset"].split(":")

rise_value = format(int(lst_rise[0]) + int(lst_rise[1])/60,'.2f')
print(rise_value)

set_value = format(int(lst_set[0]) + int(lst_set[1])/60,'.2f')
print(set_value)
"""

print("25/12/2020" > "1/1/2021" )
