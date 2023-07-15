# Exercise Tracker

This project is a Python script that allows you to log your daily exercises. It uses the Nutritionix API to determine the details of the exercise you've done, such as the duration and calories burned. Then, it logs this data along with the current date and time to a Google Sheet using the Sheety API.

## Features

- User input for type of exercise done
- Utilizes Nutritionix API to fetch details about the exercise
- Logs the exercise data along with current date and time to a Google Sheet using Sheety API

## Pre-requisites

- Python 3
- pip
- A Nutritionix API account to get your NUTRITIONIX_ID and NUTRITIONIX_KEY
- A Sheety account to get your TOKEN and to set up the Google Sheets endpoint (SHEETY_ENDPOINT)

## Setup

Clone this repository to your local machine.

\```bash
git clone https://github.com/your_username/exercise-tracker.git
\```

Install the required Python packages.

\```bash
pip install -r requirements.txt
\```

Set up your environment variables. You need to set up the following:

- NUTRITIONIX_KEY: Your Nutritionix API key
- NUTRITIONIX_ID: Your Nutritionix ID
- TOKEN: Your Sheety token
- EXERCISE_ENDPOINT: The Nutritionix API endpoint ("https://trackapi.nutritionix.com/v2/natural/exercise")
- SHEETY_ENDPOINT: Your Sheety API endpoint

Create a .env file in your project root and set the values of these environment variables.

\```env
NUTRITIONIX_KEY=your_nutritionix_key
NUTRITIONIX_ID=your_nutritionix_id
TOKEN=your_sheety_token
EXERCISE_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise
SHEETY_ENDPOINT=your_sheety_endpoint
\```

Running the Script
Navigate to the project directory in your terminal.

\```bash
cd path_to_project
\```

Run the script.

\```bash
python main.py
\```

When prompted, enter the exercise you did. The script will log the details to your Google Sheet.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
