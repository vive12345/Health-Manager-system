
# def calculate_bmr(weight, height, age, gender):
#     """
#     Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
#
#     Parameters:
#     weight (float): weight of person in kg
#     height (float): height of person in cm
#     age (int): age of person in years
#     gender (str): 'male' or 'female'
#
#     Returns:
#     bmr (float): basal metabolic rate in calories
#     """
#     if gender == 'male':
#         bmr = 10 * weight + 6.25 * height - 5 * age + 5
#     elif gender == 'female':
#         bmr = 10 * weight + 6.25 * height - 5 * age - 161
#     else:
#         raise ValueError("Invalid gender. Please choose 'male' or 'female'")
#
#     return bmr
#
#
# # Test the function with sample inputs
# weight = 45
# height = 154
# age = 22
# gender = 'female'
#
# bmr = calculate_bmr(weight, height, age, gender)
# sedentary_bmr = bmr * 1.2  # Sedentary level of exercise
#
# print("Your Basal Metabolic Rate (BMR) is:", round(bmr, 2), "calories.")
# print("If you have a sedentary lifestyle, your daily caloric needs are:", round(sedentary_bmr, 2), "calories.")
class BmrCalculator:
    # A class to calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.

    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender

    def calculate_bmr(self):

        if self.gender == 'male':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender == 'female':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            raise ValueError("Invalid gender. Please choose 'male' or 'female'")

        return bmr

    # def calculate_daily_caloric_needs(self, activity_level=1.2):
    #     bmr = self.calculate_bmr()
    #     daily_caloric_needs = bmr * activity_level
    #
    #     return daily_caloric_needs

# Create an object of the BmrCalculator class with weight = 70 kg, height = 175 cm, age = 30, and gender = 'male'
bmr_calculator = BmrCalculator(weight=70, height=175, age=30, gender='male')
# Call the calculate_bmr method to calculate the BMR
bmr = bmr_calculator.calculate_bmr()
# print("Basal Metabolic Rate (BMR):", bmr)

# # Call the calculate_daily_caloric_needs method to calculate the daily caloric needs
# daily_caloric_needs = bmr_calculator.calculate_daily_caloric_needs(activity_level=1.5)
# print("Daily Caloric Needs:", daily_caloric_needs)
