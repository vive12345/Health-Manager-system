from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
# Load the dataset
# from total_calorie_cal import CALORIE2GAIN
class FoodRecommender:
    def __init__(self,calorie2gain):
        self.calorie2gain = calorie2gain
        self.food_string = ''

    def fooditem_rec(self):
        food_data = pd.read_csv("nutrients_csvfile.csv")
        #replace t in the data by 0. t indicates miniscule amount inside the food item
        food_data = food_data.replace("t", 0)
        food_data = food_data.replace("t'", 0)

        #convert commas to numerical data for respective int or float variable
        food_data = food_data.replace(",","", regex=True)
        food_data['Protein'] = food_data['Protein'].replace("-1","", regex=True)
        food_data['Fiber'] = food_data['Fiber'].replace("a","", regex=True)
        food_data['Calories'][91] = (8+44)/2
        food_data = food_data.dropna()

        #convert grams, calories, protein, fat, saturated fat, fiber and carbs datatypes to int
        food_data['Grams'] = pd.to_numeric(food_data['Grams'])
        food_data['Calories'] = pd.to_numeric(food_data['Calories'])
        food_data['Protein'] = pd.to_numeric(food_data['Protein'])
        food_data['Fat'] = pd.to_numeric(food_data['Fat'])
        food_data['Sat.Fat'] = pd.to_numeric(food_data['Sat.Fat'])
        food_data['Fiber'] = pd.to_numeric(food_data['Fiber'])
        food_data['Carbs'] = pd.to_numeric(food_data['Carbs'])

        #Simplifying Categories
        food_data['Category'] = food_data['Category'].replace(['Fruits A-F', 'Fruits G-P', 'Fruits R-Z'], 'Fruits', regex=True)
        food_data['Category'] = food_data['Category'].replace(['Vegetables A-E', 'Vegetables F-P', 'Vegetables R-Z'], 'Vegetables', regex=True)

        X = food_data["Calories"]
        y = food_data["Food"]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the KNN model
        X = food_data[["Calories"]].values
        y = food_data["Food"].values
        knn = KNeighborsClassifier(n_neighbors=20)
        knn.fit(X, y)

        # Predict the food items
        calories = self.calorie2gain
        # grams = float(input("Enter the grams: "))
        food_items = knn.kneighbors([[calories]], n_neighbors=20, return_distance=False)
        food_items = [y[i] for i in food_items[0]]
        food_items_data = food_data.loc[food_data["Food"].isin(food_items), ["Food", "Calories", "Grams","Category","Measure","Protein","Fat","Fiber","Carbs","Sat.Fat"]]

        # Display the predicted food items with their calories and grams
        # for item in food_items_data['Food']:
        #     print(item)


        for item in food_items_data['Food'][:5]:
            self.food_string += item + ', '

        # Remove the trailing comma and space
        self.food_string = self.food_string[:-2]

        print(self.food_string)
        # food_items_data = food_items_data.sort_values(by='Calories', ascending=False)

        # new_food_items_data = food_items_data.replace

        html_table = food_items_data.to_html()

        with open('foodsuggestiontable', 'w') as f:
            f.write(html_table)

# fr = FoodRecommender(300)
# fr.fooditem_rec()
# print(fr.food_string)
# with open('foodsuggestiontable', 'r') as f:
#                     table_data = f.read()
