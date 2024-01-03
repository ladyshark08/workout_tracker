import requests
from datetime import date
import datetime
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
present_day = datetime.datetime.now()
present_time = present_day.time().strftime('%H:%M:%S')
nl_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
parameters = {
    "query": input("What did you do?: ")
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response = requests.post(url=nl_url, json=parameters, headers=headers)
print(response.status_code)
nl_result = response.json()["exercises"]
print(response.json())

sheety_url = os.environ.get("SHEETY_URL")
bearer_auth = os.environ.get("BEARER_AUTH")
for exercise in nl_result:
    data = {
        "workout": {
            "date": str(date.today().strftime('%d/%m/%Y')),
            "time": present_time,
            "exercise": str(exercise["name"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
    bearer_headers = {
        "Authorization": bearer_auth
    }
    sheety_req = requests.post(url=sheety_url, json=data, headers=bearer_headers)
    print(sheety_req.text)
