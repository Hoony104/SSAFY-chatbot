import requests
from pprint import pprint
from decouple import config

base = 'https://api.telegram.org'
token = 'bot'+config('TELEGRAM_TOKEN')
method = 'sendmessage'

updates=f'{base}/{token}/getupdates'
status=requests.get(updates).json()
print(token)