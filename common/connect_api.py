import requests
from dotenv import load_dotenv
import os


API_URL = os.getenv('API_URL')
API_PORT = os.getenv('API_PORT')

# connect to the API
def status():
    print(f'{API_URL}:{API_PORT}/status')
    r = requests.get(f'{API_URL}:{API_PORT}/status')
    if r.status_code != 200:
        raise Exception('API is not available')
    return r.text == '1'


def authenticate(user, password):
    response = requests.get(f'{API_URL}:{API_PORT}/permissions', params={'username': user, 'password': password})
    return response
