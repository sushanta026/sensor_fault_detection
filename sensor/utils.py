from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import sys,os
import pandas as pd

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        logging.info(f"reading data from database: {database_name} and collection : {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns : {df.columns}")
        logging.info(f"Dropping column: _id")
        if "_id" in df.columns:
            df = df.drop("_id",axis=1)
        logging.info(f"rows and columns : {df.shape}")
        return df



    except Exception as e:
        raise SensorException(sys,e)