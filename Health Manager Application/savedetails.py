# import requests
# from datetime import datetime
#
# # Define the Sheety API endpoint URL and authentication token
# sheety_url = 'https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/schedule1/sheet1'
# # auth_token = "Basic dmlwc2FwYXRlbDp2aXBzYXBhdGVsMTIzNDU="
#
# # Get the current date and time
# # now = datetime.now()
# current_date = datetime.now().strftime("%d/%m/%Y")
# print(current_date)
#
# # Ask the user to input the activity name and recommended exercise or food
# activity_name = input("Enter the activity name: ")
# recommended = input("Enter the recommended exercise or food: ")
# time = input("Enter time: ")
# # Prepare the data to be sent to the Sheety API endpoint
# payload = {
#     "sheet1": {
#         "date": current_date,
#         "time": time,
#         "name": activity_name,
#         "recommended": recommended
#     }
# }
# headers = {
#     "Content-Type": "application/json",
# }
#
# # Send a POST request to the Sheety API endpoint to create a new row in the sheet
# response = requests.post(sheety_url, json=payload, headers=headers)
#
# # Check the response status code and print the result
# if response.status_code == 200:
#     print("Data saved successfully!")
# else:
#     print(f"Failed to save data. Response status code: {response.status_code}")

# import requests
# from datetime import datetime
#
# class SheetyAPI:
#     def __init__(self, url, auth_token=None):
#         self.url = url
#         self.auth_token = auth_token
#         self.headers = {
#             "Content-Type": "application/json",
#         }
#         if self.auth_token:
#             self.headers["Authorization"] = self.auth_token
#
#     def add_data(self, data):
#         # date = datetime.now().strftime("%d/%m/%Y")
#         payload = {}
#         for activity in data:
#             # name = activity["name"]
#             # time = activity["time"]
#             playload = {"sheet1":{
#                 "name": activity["name"],
#                 "time":  activity["time"]
#             }}
#             print(playload)
#         response = requests.post(self.url, json=payload, headers=self.headers)
#
#         if response.status_code == 200:
#             print("Data saved successfully!")
#         else:
#             print(f"Failed to save data. Response status code: {response.status_code}")
#
# if __name__ == "__main__":
#     # Define the Sheety API endpoint URL and authentication token
#     sheety_url = 'https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/schedule1/sheet1'
#     # auth_token = "Basic dmlwc2FwYXRlbDp2aXBzYXBhdGVsMTIzNDU="
#     # Get the current date and time
#     # print(current_date)
#
#     # Define a dictionary of 5 activities and their corresponding times
#     activities = [
#         {"name": "wakeup", "time": "10:00"},
#         {"name": "breakfast", "time": "11:00"},
#         {"name": "lunch", "time": "12:00"},
#         {"name": "dinner", "time": "13:00"},
#         {"name": "sleep", "time": "14:00"}
#     ]
#
#     # Create a SheetyAPI instance and call the add_data method
#     sheety = SheetyAPI(sheety_url)
#     sheety.add_data(activities)
import requests
from datetime import datetime

class SheetyAPI:
    def __init__(self, url, auth_token=None):
        self.url = url
        self.auth_token = auth_token
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.auth_token:
            self.headers["Authorization"] = self.auth_token

    def add_data(self, data):
        payload = {}
        for activity in data:

            payload = {"sheet1": {
                "name": activity["name"],
                "time":  activity["time"]
            }}
            print(payload)
            response = requests.post(self.url, json=payload, headers=self.headers)

            if response.status_code == 200:
                print("Data saved successfully!")
            else:
                print(f"Failed to save data. Response status code: {response.status_code}")
# activities = [
#     {"name": "wakeup", "time": "10:00"},
#     {"name": "breakfast", "time": "11:00"},
#     {"name": "lunch", "time": "12:00"},
#     {"name": "dinner", "time": "13:00"},
#     {"name": "sleep", "time": "14:00"}
# ]
# sheety_url = 'https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/schedule1/sheet1'
# sheety = SheetyAPI(sheety_url)
# sheety.add_data(activities)

