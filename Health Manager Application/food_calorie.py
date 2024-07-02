import requests
import json

FOOD_CALORIE = 0

class NutrientTableGenerator:
    def __init__(self, app_id, app_key):
        self.foodcalorie_cal = 0
        self.headers = {
            'x-app-id': app_id,
            'x-app-key': app_key,
            'Content-Type': 'application/json'
        }

    def generate_table_html(self, user_input):
        # Send a POST request to the Nutritionix API with the user input as the query parameter
        response = requests.post('https://trackapi.nutritionix.com/v2/natural/nutrients', headers=self.headers,
                                 data=json.dumps({"query": user_input}))

        # Parse the JSON response
        data = response.json()

        # Generate HTML table
        table_html = '''<table class='table table-bordered'>
        <thead class='thead-dark'>
        <tr><th>Qty</th><th>Unit</th><th>Food</th><th>Calories</th><th>Weight (g)</th></tr> 
        </thead>'''
        for food in data['foods']:
            qty = food['serving_qty']
            unit = food['serving_unit']
            name = food['food_name']
            calories = food['nf_calories']
            weight = food['serving_weight_grams']
            self.foodcalorie_cal += calories
            table_html += f"<tr><td>{qty}</td><td>{unit}</td><td>{name}</td><td>{calories}</td><td>{weight}</td></tr>"
        table_html += "</table>"
        global FOOD_CALORIE
        FOOD_CALORIE = self.foodcalorie_cal
        print(table_html)
        return table_html

# generator = NutrientTableGenerator('dab0a321', '2ce758f054c20770e28e55fa4c0375d3')
# user_input = input("What did you eat today? ")
# table_html = generator.generate_table_html(user_input)
# print(table_html) # Or save to a file and open in a browser
# print(generator.foodcalorie_cal)