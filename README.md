# spm-report-generator
a script that gets json data from the speechusage db, parses it and uploads to google sheets

When this script is run the latest data from the speechusage database is pulled into python. This data is hosted as JSON here: https://speechusage.uc.r.appspot.com/getdata

The data is brought into a python pandas dataframe and parsed. Of the entries in the dataframe only entries that have reported usage are output. Once the relevent info has been parsed it is sent to the google sheet specified in the beginning of the script. I have set this sheet up to be the py_input tab on the SPM Usage sheet: https://docs.google.com/spreadsheets/d/1Hx0KTSRmOxwUW3XgS1jaLKcHns4UMi65jXDmKNq24DY/edit?usp=sharing
