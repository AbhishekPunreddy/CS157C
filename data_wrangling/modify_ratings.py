import pandas as pd 
import json 


csv_file = pd.DataFrame(pd.read_csv(r'C:\Users\samai\Desktop\ratings_small.csv', sep = ",", header = 0, index_col = False))
csv_file.to_json("ratings_small.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)