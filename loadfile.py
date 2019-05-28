from pymongo import MongoClient
from pprint import pprint
import pandas as pd
client = MongoClient("mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb")
db=client.test
employee = db.employee
df = pd.read_csv("~/Desktop/yelp/yelp-dataset/yelp_user.csv")
records_ = df.to_dict(orient = 'records')
result = db.employee.insert_many(records_)

