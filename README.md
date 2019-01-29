# Datadog import and export dashboards and monitors

I had to migrate all my dashboards and monitors from one location to another. This can also be used to import export between accounts I believe.
This series of scripts is handy to achive these purposes.

## Howto
- create an .env file with your secrets. Make sure you python interpreter loads the variables. An example:
  ```
  EXPORT_API_KEY=<secret>
  EXPORT_APP_KEY=<secret>
  EXPORT_API_HOST=https://api.datadoghq.com
  IMPORT_API_KEY=<secret>
  IMPORT_APP_KEY=<secret>
  IMPORT_API_HOST=https://api.datadoghq.eu
  ```
- Run all the exporters scripts, this will create json files
- Run the importer scripts, this will create objects in the destination Datadog account
