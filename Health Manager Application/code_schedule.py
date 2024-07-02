from datetime import datetime, timedelta
import requests
from time import sleep
from twilio.rest import Client
import pytz

class TwilioReminder:
    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number, user_phone_number, sheety_url):
        # Set up the Twilio client
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number
        self.user_phone_number = user_phone_number

        self.msg = ""

        # Set up the Sheety API endpoint URL
        self.sheety_url = sheety_url

        # Retrieve the list of times from the Sheety API endpoint
        response = requests.get(self.sheety_url)
        self.times_list = [row['time'] for row in response.json()['sheet1']]
        print(self.times_list)

        # Convert the times to datetime objects in the local timezone
        local_tz = pytz.timezone('Asia/Kolkata')  # Replace with your local timezone
        local_times = [datetime.strptime(time, '%H:%M').replace(tzinfo=local_tz) for time in self.times_list]

        # Convert the local times to UTC times
        utc_tz = pytz.timezone('UTC')
        self.utc_times = [time.astimezone(utc_tz).strftime('%H:%M') for time in local_times]

        print(self.utc_times)
        # self.times_list = self.utc_times

        # Convert the times to datetime objects
        self.utc_times = [datetime.strptime(time, '%H:%M') for time in self.utc_times]
        # Add 25 minutes to each datetime object
        new_utc_times = [time + timedelta(minutes=25) for time in self.utc_times]
        # Convert the datetime objects back to strings in the format '%H:%M'
        self.new_utc_time_strings = [time.strftime('%H:%M') for time in new_utc_times]
        self.times_list = self.new_utc_time_strings
        # print(self.new_utc_time_strings)

        self.recommended = ''


    def runthis(self):
        # Loop indefinitely
        while True:
            # Get the current time
            now = datetime.now()
            print(str(now.strftime('%H:%M')))
            print(self.times_list[0])
            print(self.utc_times[0])
            # Check if it's time to send the morning message
            if self.times_list[0] == now.strftime('%H:%M'):
                self.msg = "Good morning! start your day with Exercise and healthy Breakfast!! also don't forget to keep us updated"

            # Check if it's time to send the evening message
            elif self.times_list[4] == now.strftime('%H:%M'):
                self.msg = "Good night! one more day to accomplish healthy and long life"

            # Check if it's between the morning and evening times
            elif self.times_list[0] < now.strftime('%H:%M') < self.times_list[4]:
                # Check if it's been 3 hours since the last message was sent
                if (now - self.last_msg_time) >= timedelta(seconds=40):
                    # Set the customized message to send
                    # Make a GET request to the API to retrieve the data
                    response = requests.get("https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/msg/sheet1/2")
                    # Extract the data from the response as a JSON object
                    data = response.json()
                    # Extract the recommended message from the data
                    self.recommended = data["sheet1"]["recommended"]
                    # Modify this line to set your own customized message
                    self.msg = self.recommended

            # Send the message if there is one to send
            if self.msg != "":
                print("entered in sheet")

                # message = self.twilio_client.messages.create(
                #     body=self.msg,
                #     from_=self.twilio_phone_number,
                #     to=self.user_phone_number
                # )
                print(f"Message sent at {now.strftime('%H:%M:%S')} and {self.msg}")
                self.msg = ""  # Reset the message to an empty string

                # Record the time the message was sent
                self.last_msg_time = now

            # Wait for one minute before checking again
            sleep(50)


reminder = TwilioReminder(
   
    #add keys, numbers and sheety api link
)
reminder.runthis()

