import holidays
import requests
from datetime import datetime

for i in holidays.Australia(years = 2021).items():
    date_obj = datetime.strptime("27/12/2021", '%d/%m/%Y')
    if str(i[0].strftime('%d/%m/%Y')) == "27/12/2021":
        surcharge = True
        
response = requests.get("http://api.open-notify.org/astros.json")
print(response())