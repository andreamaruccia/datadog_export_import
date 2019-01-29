import os
import json
from datadog import initialize, api

options = {'api_key': os.environ['EXPORT_API_KEY'],
           'app_key': os.environ['EXPORT_APP_KEY'],
           'api_host': os.environ['EXPORT_API_HOST']}

initialize(**options)

data_folder="./data_screen/"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

screenboards=api.Screenboard.get_all()['screenboards']

for screenboard in screenboards:
  print(screenboard['id'])
  screenboard_id = screenboard['id']
  detailed_screenboard = api.Screenboard.get(screenboard_id)
  with open(f'./{data_folder}/{screenboard_id}.json', 'w') as outfile:
    json.dump(detailed_screenboard, outfile)
