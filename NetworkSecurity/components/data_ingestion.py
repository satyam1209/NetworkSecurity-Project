# Read data from Mongo DB 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.enitity.artifact_entity import DataIngestionArtifact
# configuration for data ingestion config

from networksecurity.enitity.config_entity import DataIngestionConfig
import os
import sys
import pymongo
from typing import List
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL_KEY')


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def read_data_from_db_as_dataframe(self):
        try:
            client = pymongo.MongoClient(MONGO_DB_URL)
            db = client[self.data_ingestion_config.database_name]
            collection = db[self.data_ingestion_config.collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df.drop(columns = ['_id'],inplace=True)
            df.replace({'na',np.nan},inplace=True)
            return df
        except Exception as e :
            raise NetworkSecurityException(e,sys)
    def store_data_in_feature_store(self,df):
        try:
            dir_path = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            df.to_csv(self.data_ingestion_config.feature_store_file_path,index=False,header=True)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_into_train_test(self,df):
        try:
            df_train,df_test = train_test_split(df,random_state=42,test_size=self.data_ingestion_config.train_test_split_ratio)
            train_dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            test_dir_path = os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(train_dir_path,exist_ok=True)
            os.makedirs(test_dir_path,exist_ok=True)
            df_train.to_csv(self.data_ingestion_config.training_file_path,index =False,header=True)
            df_test.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
        except Exception as e:
            raise NetworkSecurityException(e,sys)



    def initiate_data_ingestion(self):
        try:
            # read data from DB
            df = self.read_data_from_db_as_dataframe()
            self.store_data_in_feature_store(df)
            self.split_data_into_train_test(df)
            dataingestionartifact = DataIngestionArtifact(self.data_ingestion_config.training_file_path,
                                                          self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
