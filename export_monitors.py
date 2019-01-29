import os
import json
from datadog import initialize, api

options = {'api_key': os.environ['EXPORT_API_KEY'],
           'app_key': os.environ['EXPORT_APP_KEY'],
           'api_host': os.environ['EXPORT_API_HOST']}

initialize(**options)

data_folder="./data_monitors/"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

monitors=api.Monitor.get_all()

for monitor in monitors:
  print(monitor['id'])
  monitor_id = monitor['id']
  detailed_monitor = api.Monitor.get(monitor_id)
  with open(f'./{data_folder}/{monitor_id}.json', 'w') as outfile:
    json.dump(detailed_monitor, outfile)
