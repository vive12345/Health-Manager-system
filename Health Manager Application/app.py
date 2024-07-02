from flask import *
import requests
from exercise_calorie import WorkoutTracker
from chatgpt import OpenAIChatbot
from news import HealthNews
from food_calorie import NutrientTableGenerator
from foodrecom import FoodRecommender
from bodycalorie_cal import BmrCalculator
from exerciserecom import ExerciseRecommendation
from savedetails import SheetyAPI
from msgreplace import Sheety
app = Flask(__name__)
app.secret_key = ""
app_id = ""
api_key = ""
sheet_endpoint = ""
google_sheet_name="sheet1"
EXERCISE_CALORIE = 0.0
FOOD_CALORIE =0.0
CALORIE_NEEDS = 0.0
NET_CALORIE = 0.0
CALORIE2GAIN = 0.0
CALORIE2BURN = 0.0
FLAG = 0
sheety_url = ''
sheet_url = ""
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session['email'] = email
        session['password'] = password
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == session.get('email') and password == session.get('password'):
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Invalid email or password')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('email', None)
    session.pop('password', None)
    # return render_template('logout.html', email=session['email'])
    return redirect(url_for('home'))

@app.route('/templates/logout.html')
def logout_html():
   return render_template('logout.html', email=session['email'])

@app.route('/templates/userinfo.html/', methods=["GET", "POST"])
def userinfo():
    if request.method == "POST":
        session['name1'] = request.form.get("name")
        session['age1'] = int(request.form.get("age"))
        session['gender1'] = str(request.form.get("gender"))
        session['height1'] = int(request.form.get("height"))
        session['weight1'] = int(request.form.get("weight"))

        bmr_calculator = BmrCalculator(weight=session.get('weight1'), height=session.get('height1'),
                                       age=session.get('age1'), gender=session.get('gender1'))
        bmr = bmr_calculator.calculate_bmr()
        global CALORIE_NEEDS, NET_CALORIE
        CALORIE_NEEDS = float(bmr)
        NET_CALORIE = CALORIE_NEEDS
        return redirect(url_for('signup'))
    return render_template("userinfo.html")

@app.route("/index")
def index():
    news_api_key = ""
    health_news = HealthNews(api_key=news_api_key)
    news_list = health_news.get_news()
    # print(news_list)
    return render_template("index.html", news_list=news_list)

@app.route('/templates/profile.html/')
def profile():
         global CALORIE_NEEDS
         name1 = session.get("name1")
         age1 = session.get("age1")
         gender1 = session.get("gender1")
         height1 = session.get("height1")
         weight1 = session.get("weight1")
         bmr = CALORIE_NEEDS
         return render_template('profile.html', name2= name1, age2= age1, gender2= gender1, height2= height1, weight2= weight1, bmr=bmr)

@app.route('/templates/edit.html/', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        session['name1'] = request.form.get("name")
        session['age1'] = int(request.form.get("age"))
        session['gender1'] = str(request.form.get("gender"))
        session['height1'] = int(request.form.get("height"))
        session['weight1'] = int(request.form.get("weight"))

        bmr_calculator = BmrCalculator(weight=session.get('weight1'), height=session.get('height1'),
                                       age=session.get('age1'), gender=session.get('gender1'))
        bmr = bmr_calculator.calculate_bmr()
        global CALORIE_NEEDS, NET_CALORIE
        CALORIE_NEEDS = float(bmr)
        NET_CALORIE = CALORIE_NEEDS
        return redirect(url_for('profile'))
    return render_template("edit.html")


@app.route('/templates/tellmeexercise.html', methods=["GET", "POST"])
def tell_func():
    if request.method == "POST":
        exercise_text = str(request.form.get("tellme1"))
        gender = session.get('gender1')
        age = session.get('age1')
        height = session.get('height1')
        weight = session.get('weight1')
        tracker = WorkoutTracker(gender=gender, weight_kg=weight, height_cm=height, age=age, app_id=app_id,
                                 api_key=api_key,
                                 google_sheet_name=google_sheet_name,
                                 sheet_endpoint=sheet_endpoint)
        tracker.track_workout(exercise_text)
        response = tracker.result_dict
        global EXERCISE_CALORIE
        EXERCISE_CALORIE = float(tracker.net_calorie_burn)
        return render_template("last_exercise.html", goal_dict = response)
    return render_template("tellmeexercise.html")


@app.route('/templates/tellmefood.html', methods=['GET', 'POST'])
def tellmefood():
    if request.method == "POST":
        user_input = request.form.get("tellmefood1")
        generator = NutrientTableGenerator(app_id, api_key)
        table_html = generator.generate_table_html(user_input)
        # food calories total stored in session variable called foodcalorie_cal
        global FOOD_CALORIE
        FOOD_CALORIE = float(generator.foodcalorie_cal)
        return render_template("foodcalorietable.html", table = table_html)
    return render_template('tellmefood.html')


@app.route('/templates/calories.html')
def calories():
    global CALORIE_NEEDS,FOOD_CALORIE,EXERCISE_CALORIE,NET_CALORIE,CALORIE2GAIN,CALORIE2BURN,FLAG
    if FOOD_CALORIE or EXERCISE_CALORIE != 0:
        NET_CALORIE = NET_CALORIE + (FOOD_CALORIE - EXERCISE_CALORIE)
        if NET_CALORIE > CALORIE_NEEDS + 50 :
            # EXERCISE_CALORIE = 0.0
            CALORIE2BURN = 0.0
            CALORIE2BURN = NET_CALORIE - CALORIE_NEEDS
            CALORIE2BURN = round(CALORIE2BURN,2)
            FLAG = 0
        elif NET_CALORIE < CALORIE_NEEDS - 50:
            # EXERCISE_CALORIE = 0.0
            # FOOD_CALORIE = 0.0
            CALORIE2GAIN = 0.0
            CALORIE2GAIN = CALORIE_NEEDS - NET_CALORIE
            CALORIE2GAIN = round(CALORIE2GAIN,2)
            FLAG = 1
        else:
            FLAG = 2
        return render_template('calories.html', calories_intake_needed=CALORIE_NEEDS, calories_burn=EXERCISE_CALORIE, calories_gain=FOOD_CALORIE, net_calorie=NET_CALORIE)

@app.route("/templates/calories.html/suggestion")
def suggestion():
    global CALORIE_NEEDS,FOOD_CALORIE,EXERCISE_CALORIE, NET_CALORIE,CALORIE2GAIN,CALORIE2BURN,FLAG,MSG
    # NET_CALORIE = NET_CALORIE + (FOOD_CALORIE - EXERCISE_CALORIE)
    api = Sheety(sheet_url)
    if FLAG == 0:
        EXERCISE_CALORIE = 0.0
        FOOD_CALORIE = 0.0
        er = ExerciseRecommendation('exercise.csv')
        html_output = er.suggest_exercises(CALORIE2BURN)
        MSG = f'You have to burn {CALORIE2BURN} Kcal.The recommended exercises are {er.exercise_string} and for more details visit our web app'
        recommended_text = MSG
        api.update_recommended(recommended_text)
        return render_template('exerciserecommender.html',calorie2burn = CALORIE2BURN,table_data=html_output)
    elif FLAG == 1 :
        EXERCISE_CALORIE = 0.0
        FOOD_CALORIE = 0.0
        fr = FoodRecommender(CALORIE2GAIN)
        fr.fooditem_rec()
        MSG=f'You have to gain {CALORIE2GAIN} Kcal.The recommended food items are {fr.food_string} and for more details visit our web app'
        # Update the "Recommended" cell in row 2 with new text
        recommended_text = MSG
        api.update_recommended(recommended_text)
        with open('foodsuggestiontable', 'r') as f:
            EXERCISE_CALORIE = 0.0
            FOOD_CALORIE = 0.0
            table_data = f.read()
        return render_template('foodrecommender.html',table_data=table_data,calories_intake_needed=CALORIE_NEEDS, calories_burn=EXERCISE_CALORIE, calories_gain=FOOD_CALORIE, calorie2gain=CALORIE2GAIN)
    elif FLAG == 2:
        MSG = f'your bmr value is {CALORIE_NEEDS} and till now you calorie intake is maintained'
        recommended_text = MSG
        api.update_recommended(recommended_text)
        calorie_maintain = "Your Calories are Maintained"
        return render_template('calories.html', calories_intake_needed=CALORIE_NEEDS, calories_burn=EXERCISE_CALORIE, calories_gain=FOOD_CALORIE, net_calorie=NET_CALORIE, calorie_maintain=calorie_maintain)

@app.route("/templates/table.html")
def table():
    # Sheety API Call & Authentication
    sheet_endpoint = ""
    response = requests.get(sheet_endpoint)
    sheet_data = response.json()["workouts"]
    return render_template("table.html", sheet_data=sheet_data)

@app.route("/templates/index_schedule.html")
def index_schedule():
    return render_template("index_schedule.html")

@app.route("/templates/add")
def add():
    return render_template("add.html")


@app.route("/templates/savedetails", methods=["POST", "GET"])
def savedetails():
    msg = "msg"

    if request.method == "POST":
        try:
            sheety = SheetyAPI(sheety_url)
            # aname = request.form["aname"]
            # time = request.form["time"]
            wakeup = request.form['wakeup']
            breakfast = request.form['breakfast']
            lunch = request.form['lunch']
            dinner = request.form['dinner']
            sleep = request.form['sleep']
            activities = [
                {"name": "wakeup", "time": wakeup},
                {"name": "breakfast", "time": breakfast},
                {"name": "lunch", "time": lunch},
                {"name": "dinner", "time": dinner},
                {"name": "sleep", "time": sleep}
            ]
            sheety.add_data(activities)
            # with sqlite3.connect("employee.db") as con:
            #     cur = con.cursor()
            #     cur.execute("INSERT into employee (aname, time) values (?,?)", (aname, time))
            #     con.commit()
            msg = "user schedule successfully Added"
        except:
            # con.rollback()
            msg = "We can not add the user to the list"
        finally:
            # con.close()
            return render_template("success.html", msg=msg)



@app.route("/templates/view")
def view():
    sheety_url = f''
    response = requests.get(sheety_url, headers={
        "Content-Type": "application/json",
    })
    sheet_data = response.json()['sheet1']
    # for data in sheet_data:
    #     print(data["name"])
    return render_template("view.html", rows=sheet_data)


@app.route("/templates/delete")
def delete():
    for id in range(5):
        sheety_url = f'https://api.sheety.co/5d8b67865b3f1df38e3438ff82a5cbcc/schedule1/sheet1/{id}'
        response = requests.delete(sheety_url, headers={
            "Content-Type": "application/json",
        })
    return render_template("delete.html")

@app.route('/templates/openaiUI.html/')
def index1():
    return render_template('openaiUI.html')

@app.route('/chat', methods=['POST'])
def chat():
    api_key1 = ""
    chatbot = OpenAIChatbot(api_key=api_key1)
    input_prompt = request.json['input_prompt']
    chat_response = chatbot.get_response(input_prompt)
    return jsonify({'chat_response': chat_response})


if __name__ == "__main__":
    app.run(debug=True, port=5050)
