from foodrecom import FoodRecommender
FLAG = 0
CALORIE2GAIN =0
class TotalCalorieCalculator:
    def __init__(self,calorie_needs,food_calorie,exercise_calorie):
        self.calorie_needs = calorie_needs
        self.food_calorie = food_calorie
        self.exercise_calorie = exercise_calorie
        self.net_calorie = calorie_needs
        self.calorie2burn = 0
        self.calorie2gain = 0


    def TCC(self):
        if self.food_calorie or self.exercise_calorie != 0:
            self.net_calorie-=self.exercise_calorie
            self.net_calorie+=self.food_calorie
            if self.net_calorie > (self.calorie_needs+10):
                self.calorie2burn = self.net_calorie-(self.calorie_needs)
                # print(f"exercise recommend  :  {self.calorie2burn}")
                FLAG = 1
                return FLAG
            elif self.net_calorie < self.calorie_needs+10:
                self.calorie2gain = self.calorie_needs - self.net_calorie
                CALORIE2GAIN = self.calorie2gain
                print(f"food recommend  :  {CALORIE2GAIN}")
                FLAG = 2
                return FLAG
            else:
                print(f"task achieved  :  {self.net_calorie}")
                FLAG = 0
                return FLAG
        else:
            print("input your exercise r food consumption")

# obj = TotalCalorieCalculator()
# obj.TCC()
# CALORIE2GAIN = self.calorie2gain
#                 obj_foodrec = FoodRecommender(CALORIE2GAIN)
#                 obj_foodrec.fooditem_rec()
#                 with open('foodsuggestiontable', 'r') as f:
#                     table_data = f.read()