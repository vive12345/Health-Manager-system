
import requests
from datetime import datetime

class WorkoutTracker:
    def __init__(self, gender, weight_kg, height_cm, age, app_id, api_key, google_sheet_name, sheet_endpoint):
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age
        self.app_id = app_id
        self.api_key = api_key
        self.google_sheet_name = google_sheet_name

        self.sheet_endpoint = sheet_endpoint
        self.net_calorie_burn = 0
        self.result_dict = {}

    def track_workout(self, exercise_text):
        # Nutritionix API Call
        exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        headers = {
            "x-app-id": self.app_id,
            "x-app-key": self.api_key,
        }

        parameters = {
            "query": exercise_text,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age
        }

        response = requests.post(exercise_endpoint, json=parameters, headers=headers)
        result = response.json()
        print(f"Nutritionix API call: \n {result} \n")

        # Adding date and time
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        # Sheety API Call & Authentication
        for exercise in result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }
            self.net_calorie_burn += exercise["nf_calories"]
            self.result_dict = sheet_inputs

            # Sheety Authentication Option 1: No Auth
            sheet_response = requests.post(self.sheet_endpoint, json=sheet_inputs,)

            