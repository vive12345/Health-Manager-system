# from sklearn.model_selection import train_test_split
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# # Load the dataset
# # from total_calorie_cal import CALORIE2GAIN
# class exerciseRecommender:
#     def __init__(self,calorie2burn):
#         self.calorie2gain = calorie2burn
#
#     def exerciseitem_rec(self):
#         exercise_data = pd.read_csv("exercise.csv")
#         # Import necessary libraries
#         import pandas as pd
#         from sklearn.neighbors import NearestNeighbors
#
#         # Load the dataset
#         df = pd.read_csv('exercise.csv')
#
#         # Get user input
#         calories = int(input("Enter the number of calories burned during the workout: "))
#
#         # Filter the dataset to get only the workout types with similar calorie counts
#         calories_df = df[df['Calories'].between(calories - 50, calories + 50)]
#
#         # Fit the KNN model
#         knn_model = NearestNeighbors(n_neighbors=11, algorithm='ball_tree').fit(
#             calories_df[['Calories', 'Duration(min)']])
#
#         # Find the 10 nearest neighbors to the user input
#         _, indices = knn_model.kneighbors([[calories, 30]])
#
#         # Print the suggested workout types with similar calorie counts
#         print("The suggested workout types with similar calorie counts are:")
#         for index in indices[0][1:]:
#             print(
#                 f"{calories_df.iloc[index]['workout_type']} - {calories_df.iloc[index]['Calories']} calories - {calories_df.iloc[index]['Duration(min)']} minutes")
#
#         html_table = exercise_items_data.to_html()
#
#         with open('exercisesuggestiontable', 'w') as f:
#             f.write(html_table)
#
# # fr = exerciseRecommender()
# # fr.exerciseitem_rec()
# # with open('exercisesuggestiontable', 'r') as f:
# #                     table_data = f.read()

import pandas as pd
from sklearn.neighbors import NearestNeighbors


class ExerciseRecommendation:

    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.knn_model = None
        self.calories_df = None
        self.exercise_string = ''

    def suggest_exercises(self, calories):
        self.df = self.df.replace(",", "", regex=True)
        # convert the object type column to float
        self.df['Calories'] = self.df['Calories'].astype(float)
        # Filter the dataset to get only the workout types with similar calorie counts
        self.calories_df = self.df[self.df['Calories'].between(calories - 50, calories + 50)]

        if len(self.calories_df) == 0:
            return "<p>No workouts found with similar calorie counts. Please try a different calorie count.</p>"

        # Fit the KNN model
        self.knn_model = NearestNeighbors(n_neighbors=11, algorithm='ball_tree').fit(
            self.calories_df[['Calories', 'Duration(min)']])

        # Find the 10 nearest neighbors to the user input
        _, indices = self.knn_model.kneighbors([[calories, 30]])
        for index in indices[0][1:6]:
            self.exercise_string += self.calories_df.iloc[index]['workout_type'] + ', '
        # print(self.exercise_string)

        # # Generate HTML code for the suggested workout types with similar calorie counts
        # html_output = "<p>The suggested workout types with similar calorie counts are:</p><ul>"
        # for index in indices[0][1:]:
        #     html_output += f"<li>{self.calories_df.iloc[index]['workout_type']}  |  {self.calories_df.iloc[index]['Calories']} Kcal  |  {self.calories_df.iloc[index]['Duration(min)']} minutes</li>"
        # html_output += "</ul>"
        # return html_output
        html_output = "<div class='container'><p></p>"
        html_output += "<table class='table table-striped'><thead><tr><th>Workout Type</th><th>Calories</th><th>Duration (min)</th></tr></thead><tbody>"
        for index in indices[0][1:]:
            html_output += f"<tr><td>{self.calories_df.iloc[index]['workout_type']}</td><td>{self.calories_df.iloc[index]['Calories']} Kcal</td><td>{self.calories_df.iloc[index]['Duration(min)']}</td></tr>"
        html_output += "</tbody></table></div>"
        return html_output

# er = ExerciseRecommendation('exercise.csv')
# html_output = er.suggest_exercises(300)
# print(er.exercise_string)
