import os
from dotenv import load_dotenv
import requests
import datetime


load_dotenv()

NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
TOKEN = os.getenv("TOKEN")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/55aa9079fb5635ff903fe1909e3652fd/myWorkout/workout"

exercise_input = input("Tell which exercise you did today?: ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
    "Content-Type": "application/json"
}

payload = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 30
}

def get_current_date():
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    return today

def get_current_time():
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    return time_now

response_exercise = requests.post(EXERCISE_ENDPOINT, headers=headers, json=payload)
if response_exercise.status_code == 200:
    data = response_exercise.json()

    exercise_name = data['exercises'][0]['user_input']
    exercise_duration = data['exercises'][0]['duration_min']
    exercise_calories = data['exercises'][0]['nf_calories']

    # print(data)  # uncomment this if you want to print the data

    header = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
    }

    exercise_info = {
        'workout': {
            'date': get_current_date(),
            'time': get_current_time(),
            'exercise': exercise_name,
            'duration': exercise_duration,
            'calories': exercise_calories,  # modify this as per your requirement
        }
    }

    response_sheety = requests.post(SHEETY_ENDPOINT, json=exercise_info, headers=header)
    if response_sheety.status_code == 200:
        data_sheety = response_sheety.json()
        print(data_sheety)
    else:
        print("Request to Sheety failed with status code:", response_sheety.status_code)
else:
    print("Request to Exercise endpoint failed with status code:", response_exercise.status_code)




