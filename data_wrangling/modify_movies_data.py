import csv 
import json 
import pandas as pd
import regex as re
from datetime import datetime 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
    #Converting csv file to json
    csv_file = pd.DataFrame(pd.read_csv(csvFilePath, sep = ",", header = 0, index_col = False))
    csv_file.to_json("data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

    f = open(r'data.json')
    newjson = []
    data = json.load(f)

    #print(data[0]['genres'])
    y = data[0]
    i=2

    for y in data:
        #Movie id
        
        print(i , y['id'])
        i += 1
        y['id'] = int(y['id'])

        #Extracting cast
        x = str(re.findall(r"'name': \'.*?\'",y['cast']))
        
        print(x)
        x = re.findall(r"\b(?!name|id)[A-z ]+",x)
        y['cast'] = x


        #Extracting genres
        genres_list = y['genres']
        y['genres'] = re.findall(r"\b(?!name|id)[A-z]+",genres_list)
        

        #Extracting production companies
        str2 = y['production_companies']
        if(str2 != None):
            y['production_companies'] = " ".join(re.findall(r"\b(?!name|id)[A-z]+",str2))

        #Converting year
        if(y['Year'] != '#VALUE!'):
            y['Year'] = int(y['Year'])

        newjson.append(y)
    
    print(newjson[2])
    with open('movies_data.json', mode='w') as f:
        f.write(json.dumps(newjson, indent=3))
    print(newjson[45462])
  
csvFilePath = r"CSV3.csv"
jsonFilePath = r'sample.json'
csv_to_json(csvFilePath, jsonFilePath)