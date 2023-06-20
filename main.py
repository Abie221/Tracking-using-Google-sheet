import requests
from datetime import datetime
import os

GENDER = 'male'
WEIGHT = '84'
HEIGHT = '183'
AGE = '20'


API = os.environ.get('API_KEY')
ID = os.environ.get('API_ID')
USER_ID = os.environ.get('API_USER_ID')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
quiry_text = input('Tell me which exercises you did? ')
sheety_endpoint = os.environ.get('SHEET_ENDPOINT')


header = {
    'x-app-id': ID,
    'x-app-key': API
}

parametres = {
    'query': quiry_text,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

response = requests.post(exercise_endpoint, json=parametres, headers=header)
result = response.json()

today_date = datetime.now().strftime('%d/%m/%Y"')
now = datetime.now().strftime("%X")


for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']

        }
    }

# sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
sheet_response = requests.post(
    sheety_endpoint,
    json=sheet_inputs,
    auth=(
        'abie2210',
        '123QWEasdzxc'
    )
)

print(sheet_response.text)




