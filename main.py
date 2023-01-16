import requests
from datetime import datetime

ENDPOINT_NUTR = "https://trackapi.nutritionix.com/v2/natural/exercise"
ENDPOINT_SHEE = "YOUR-SHEETY-ENDPOINT"

APP_ID = "YOUR-APP-ID"
APP_KEY = "YOUR-APP-KEY"

GENDER = "MALE"
WEIGHT = "80"
HEIGHT = "191"
AGE = "35"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response_nutr = requests.post(ENDPOINT_NUTR, json=parameters, headers=headers)
result = response_nutr.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    exercise_update = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=ENDPOINT_SHEE, json=exercise_update)
    print(response.text)
