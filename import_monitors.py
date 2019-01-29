import json
import glob
import os
from datadog import initialize, api

options = {'api_key': os.environ['IMPORT_API_KEY'],
           'app_key': os.environ['IMPORT_APP_KEY'],
           'api_host': os.environ['IMPORT_API_HOST']}

initialize(**options)

data_folder="./data_monitors/"

for json_file in glob.glob(f"./{data_folder}/*.json"):
  with open(json_file) as f:
      data = json.load(f)

      api.Monitor.create(
          type=data['type'],
          query=data['query'],
          name=data['name'],
          message=data['message'],
          tags=data['tags'],
          options=data['options']
      )

      print("ok")