import urllib
import json
import pandas as pd
import csv
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# a script that gets json data from the speechusage db, parses it and uploads to google sheets

# google sheets api info
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1Hx0KTSRmOxwUW3XgS1jaLKcHns4UMi65jXDmKNq24DY/edit#gid=2089812132')
worksheet = spreadsheet.worksheet("py_input")

# pull in json data
json_url = "https://speechusage.uc.r.appspot.com/getdata"
df = pd.read_json(json_url)


# loop through PC ids and add ID with minutes remaining to usage dictionary
usage_dict = {}
for pc_id in df:
    entries_count = len(df[pc_id]['usage'])
    # if pc has usage listing reported, get min capacity
    if entries_count > 0:
        for pc_min in df[pc_id]['usage']:
            capacity_list = []
            capacity_list.append(pc_min['capacity'])
        min_remaining = min(capacity_list)
    else:
        min_remaining = 0
    usage_dict[pc_id] = min_remaining
# print(usage_dict)    

# load dict back into pandas data structure
outdata = pd.DataFrame(list(usage_dict.items()),columns = ['ID', 'MIN'])
print(outdata)

# send data to linked google sheet
set_with_dataframe(worksheet, outdata)
