import os
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

def load_mongo_table(path, tableName):	
	client = MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")
	db = client.test_3
	table_name = db[tableName]
	df = pd.read_csv(path)
	records_ = df.to_dict(orient = 'records')
	table_name.insert_many(records_)

load_mongo_table("~/Desktop/yelp/yelp-dataset/yelp_tip.csv", "test_table")
