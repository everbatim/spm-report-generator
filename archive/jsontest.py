import urllib
import json
import pandas as pd
import csv

json_url = "https://speechusage.uc.r.appspot.com/getdata"

df = pd.read_json(json_url)
usage_dic = {}
capacity_list = []

for pc_id in df:
    entries_count = len(df[pc_id]['usage'])
    if entries_count > 0:
        for pc_min in df[pc_id]['usage']:
            capacity_list.append(pc_min['capacity'])
        max_usage = min(capacity_list)
    else:
        max_usage = 0
    usage_dic[pc_id] = max_usage
print(usage_dic)    