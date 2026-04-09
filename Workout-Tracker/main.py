import requests
from datetime import datetime
import os
import sys

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 167
AGE = 20

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


# Set these values in your environment or .env file before running.
APP_ID = require_env("NUTRITIONIX_APP_ID")
API_KEY = require_env("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = require_env("SHEETY_ENDPOINT")
SHEETY_USER = require_env("SHEETY_USER")
SHEETY_PASSWORD = require_env("SHEETY_PASSWORD")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "workout")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

exercises = result.get("exercises", [])
if not exercises:
    print("No exercises found in Nutritionix response.")
    sys.exit(0)

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety API Call & Authentication
for exercise in exercises:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(
            SHEETY_USER,
            SHEETY_PASSWORD,
        ),
    )
    sheet_response.raise_for_status()
    print(f"Sheety Response: \n {sheet_response.text}")
