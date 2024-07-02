# from urllib import response
#
# import requests
# import json
#
#
# class MsgReplace:
#     def __init__(self,sheet_url):
#         self.sheet_url = sheet_url
#     def update_row(self, recommended_text=new_data):
#         # Convert the new data to JSON
#         new_data_json = json.dumps({"row": new_data})
#
#         # Define the request headers and data as a JSON object
#         headers = {
#             "Content-Type": "application/json"
#         }
#         data = {
#             "sheet1": {
#                 "recommended": recommended_text
#             }
#         }
#
#         # Check the response to make sure the row was updated successfully
#         if response.status_code == 200:
#             print("Row updated successfully.")
#         else:
#             print("Error updating row: ", response.status_code)
#
#
# # Create a MsgReplace instance
# sheet_url='https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/msg/sheet1/2'
# MsgReplaceobj = MsgReplace(sheet_url)
# MSG = "heyee"
# # Define the new data you want to replace the row with
# new_data = {
#     "reccomend": MSG,
# }
# # Update the row with the new data
# MsgReplaceobj.update_row(new_data)

import requests
import json


class Sheety:
    def __init__(self, sheet_url):
        self.sheet_url = sheet_url

    def update_recommended(self, recommended_text):
        # Define the API endpoint URL for updating a specific row
        update_url = self.sheet_url

        # Define the request headers and data as a JSON object
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "sheet1": {
                "recommended": recommended_text
            }
        }

        # Make a PUT request to update the row
        response = requests.put(url=update_url, headers=headers,
                                data=json.dumps(data))

        # Check the response status code to see if the update was successful
        if response.status_code == 200:
            print(f"Recommended text updated successfully for r.")
        else:
            print(f"Error updating recommended text for roStatus code: {response.status_code}")


# Example usage:
# Create a SheetyAPI instance with the sheet URL and credentials
# sheet_url = "https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/msg/sheet1/2"
# api = SheetyAPI(sheet_url)
#
# # Update the "Recommended" cell in row 2 with new text
# recommended_text = "Add more protein to your diet."
# api.update_recommended(recommended_text)
# import requests
#
# # Make a GET request to the API to retrieve the data
# response = requests.get(sheet_url)
# # Extract the data from the response as a JSON object
# data = response.json()
# # Extract the recommended message from the data
# recommended = data["sheet1"]["recommended"]
# print(recommended)

