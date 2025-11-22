import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL_KEY = os.getenv("MONGO_DB_URL_KEY")
# print(MONGO_DB_URL_KEY) # Debug: Print the MongoDB URL to verify it's loaded correctly
import certifi # Import certifi to handle SSL certificates
ca=certifi.where() # Get the path to the CA bundle # Use this 'ca' variable when connecting to MongoDB
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception import exception
from networksecurity.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            print(e)

    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            print(records[0])
            return records
        except Exception as e:
            print(e)
    def insert_data_in_DB(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL_KEY)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            print(e)
if __name__=='__main__':
    a = NetworkDataExtract()
    records = a.csv_to_json_convertor('Network_Data\phisingData.csv')
    result = a.insert_data_in_DB(records,'SATYAMAI','NetworkData')
    print(result)