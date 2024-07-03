
# Objective
The "Health Manager System" is a web-based application developed using Flask (Python) to help users track their health and fitness goals. It allows users to log daily exercises and meals, monitor progress, and receive personalized recommendations and reminders to stay motivated.

You **won't** be able to run this solution code as is. Why? You'll need to add **your own** API keys as environment variables first.

## Technology Used

-Frontend: HTML, CSS, JavaScript, Bootstrap

-Backend: Python (Flask with Jinja template)

-External APIs: Twilio, ChatGPT, News, Nutritionix, Sheety

-Machine Learning: KNN algorithm, food and exercise dataset

-Database: SQL

## Project Functions and Features
User-Friendly Interface: Users can input their activities in natural English, and the app records details such as the type and duration of exercises. The UI is designed to be simple and intuitive.
Personalized Recommendations: Utilizing KNN algorithms, the app recommends exercises and foods based on user data.
Motivation and Reminders: Sends regular notifications to users' phones with recommended exercises and foods based on their calorie goals.
Chatbot Integration: Includes a chatbot feature using the ChatGPT API for interactive user support.
Automatic Calculations: Automatically calculates BMR and the calories a user needs based on their input data.

## PyCharm Environment Variables

In PyCharm you set your environment variables under "Edit Configurations". You should see a section called "Environment" -> "Environment Variables". There, you can click a small symbol which brings up a window where you can paste all your environment variables at the same time. The format follows the example of the env_for_pycharm file (use your own API keys)

## Replit Environment Variables

For Replit you need to click on the padlock symbol (Secrets) in the menu. There you can add your environment variables. You can either add them one by one or paste them from a .json file. The .json provided is just an example. You'll need to replace it with own API keys.

## FAQ KeyError

The name of your environment variables in your Python code needs to match what your environment variables are actually called. If you use:

```
API_KEY = os.environ["NT_API_KEY"]
```

Then make sure your environment variable is actually called `NT_API_KEY`. If you use a different name (like `ENV_NIX_API_KEY`) then make sure your Python code matches.

## FAQ Sheety: Insufficient Permission

Sheety needs permission to access your Google Sheet. When you sign into Sheety you probably forgot to give it permission. Sign out of Sheety and sign in again. Also, go to your Google Account -> Security -> Third Party Apps with Account Access. Check that you see Sheety listed there.

## FAQ Sheety: Bad Request. The JSON Payload should be inside a root property called "X"

Your Google sheet's name does not match the name you're using in the API call in your Python code. Rename one of them to make them match. You may also need to refresh the API page on Sheety.

## Future Improvements
Extend the dataset and implement advanced recommendation algorithms like item-item collaborative filtering.
Utilize cloud technology to handle heavy datasets and train models on servers for improved performance and scalability.
