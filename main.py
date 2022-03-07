import requests
from datetime import datetime

API_KEY = "37f77f8d66d0cd3431331f8104d560e9"
API_ID = "360ae15a"
API_URL = f"https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_API = "https://api.sheety.co/ae242319d210966e5669717ffeb7833e/myWorkouts/workouts"

my_height = "167.64"
my_weight = "50"
my_gender = "female"
my_age = 21

parameters = {
    "query": input("Tell me which exercise you did:\n"),
    "gender": my_gender,
    "weight_kg": my_weight,
    "height_cm": my_height,
    "age": 21
}
header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=API_URL, json=parameters, headers=header)
result = response.json()

today = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
    sheet_response = requests.post(SHEETY_API, json=sheet_input)
    print(sheet_response.text)