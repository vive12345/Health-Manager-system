

import os
import requests
from datetime import datetime


class WorkoutTracker:
    def __init__(self, age, gender, height_cm, weight_kg):
        self.age = age
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.APP_ID = os.environ["ENV_NIX_APP_ID"]
        self.API_KEY = os.environ["ENV_NIX_API_KEY"]
        self.exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.GOOGLE_SHEET_NAME = "workout"
        self.sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

    def calculate(self, exercise_text):
        # Nutritionix API Call
        headers = {
            "x-app-id": self.APP_ID,
            "x-app-key": self.API_KEY,
        }

        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age
        }

        response = requests.post(self.exercise_endpoint, json=parameters, headers=headers)
        result = response.json()
        print(f"Nutritionix API call: \n {result} \n")

        # Adding date and time
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        # Sheety API Call & Authentication
        for exercise in result["exercises"]:
            sheet_inputs = {
                self.GOOGLE_SHEET_NAME: {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            # Sheety Authentication Option 1: No Auth
            """
            sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
            """

            # Sheety Authentication Option 2: Basic Auth
            sheet_response = requests.post(
                self.sheet_endpoint,
                json=sheet_inputs,
                auth=(
                    os.environ["ENV_SHEETY_USERNAME"],
                    os.environ["ENV_SHEETY_PASSWORD"],
                )
            )

            # Sheety Authentication Option 3: Bearer Token
            """
            bearer_headers = {
                "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
            }
            sheet_response = requests.post(
                sheet_endpoint,
                json=sheet_inputs,
                headers=bearer_headers
            )
            """
            print(f"Sheety Response: \n {sheet_response.text}")
