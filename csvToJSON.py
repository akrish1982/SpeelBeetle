# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 07:59:40 2020

@author: akris
"""

import csv
import json


input_file = 'allWordList-a-g-out.csv'
output_file = 'allwordlist.json'
format = 'dump' #other option is pretty


csv_rows = []
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    for row in reader:
        csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
#Convert csv data into json and write it
with open(output_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(csv_rows))



    