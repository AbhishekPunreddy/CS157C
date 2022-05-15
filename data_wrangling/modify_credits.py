import csv 
import json 
import pandas as pd
import regex as re
from datetime import datetime 

def csv_to_json(csvFilePath):
    
    
    #Converting csv file to json
    jsonarray = []
    with open(csvFilePath,encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        skip = next(csv_reader)
        row1 = next(csv_reader)
        #print(row1[0],row1[1],row1[2],row1[3])
        i = 1
        for row in csv_reader:

            x = str(re.findall(r"'name': \'.*?\'",row[0]))
            x = re.findall(r"\b(?!name|id)[A-z ]+",x)
            #print(i,x)
            i+=1
            row[0] = x
            dict = {}
            dict['id'] = int(row[1])
            dict['cast'] = row[0]
            jsonarray.append(dict)
            
    print(jsonarray[0])
    with open('cast.json', mode='w') as f:
        f.write(json.dumps(jsonarray, indent=3))



csvFilePath = r"credits.csv"
csv_to_json(csvFilePath)