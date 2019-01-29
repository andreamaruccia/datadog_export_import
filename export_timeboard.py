import os
import json
from datadog import initialize, api

options = {'api_key': os.environ['EXPORT_API_KEY'],
           'app_key': os.environ['EXPORT_APP_KEY'],
           'api_host': os.environ['EXPORT_API_HOST']}

initialize(**options)

data_folder="./data_timeboard/"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

dashes=api.Timeboard.get_all()['dashes']

for dash in dashes:
  print(dash['id'])
  dash_id = dash['id']
  detailed_dash = api.Timeboard.get(dash_id)
  with open(f'./{data_folder}/{dash_id}.json', 'w') as outfile:
    json.dump(detailed_dash, outfile)
