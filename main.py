import os
from dotenv import load_dotenv
import requests


load_dotenv()

NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"




