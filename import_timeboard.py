import json
import glob
import os
from datadog import initialize, api

options = {'api_key': os.environ['IMPORT_API_KEY'],
           'app_key': os.environ['IMPORT_APP_KEY'],
           'api_host': os.environ['IMPORT_API_HOST']}

initialize(**options)

data_folder="./data_timeboard/"

for json_file in glob.glob(f"./{data_folder}/*.json"):
  with open(json_file) as f:
      data = json.load(f)

      title = data['dash']['title']
      description = data['dash']['description']
      graphs = data['dash']['graphs']
      if data['dash']['template_variables'] is None:
        data['dash']['template_variables'] = []
      template_variables = data['dash']['template_variables']
      read_only = data['dash']['read_only']
      
      res = api.Timeboard.create(title=title,
                          description=description,
                          graphs=graphs,
                          template_variables=template_variables,
                          read_only=read_only)
      print(f"imported {title} - {res}")
