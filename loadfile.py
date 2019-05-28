import os
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

def load_mongo_table(path, tableName):	
    basepath = os.path.expanduser('~/') + path
    client = MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")
    db = client.yelpdb
    table_name = db[tableName]
    df = pd.read_csv(basepath, index_col = None, header = 0)
    records_ = df.to_dict(orient = 'records')
    table_name.insert_many(records_)

