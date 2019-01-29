import json
import glob
import os
from datadog import initialize, api

options = {'api_key': os.environ['IMPORT_API_KEY'],
           'app_key': os.environ['IMPORT_APP_KEY'],
           'api_host': os.environ['IMPORT_API_HOST']}

initialize(**options)

data_folder="./data_screen/"

for json_file in glob.glob(f"./{data_folder}/*.json"):
  with open(json_file) as f:
      data = json.load(f)
      board_title = data['board_title']
      description = data['description']
      width = data['width']
      widgets = data['widgets']
      template_variables = data['template_variables']

      api.Screenboard.create(board_title=board_title,
                            description=description,
                            widgets=widgets,
                            template_variables=template_variables,
                            width=width)
      print("ok")