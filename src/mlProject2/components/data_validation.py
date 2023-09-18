# update components
import os
import urllib.request as request
import pandas as pd
import zipfile
from src.mlProject2 import logger
from src.mlProject2.utils.common import get_size
from src.mlProject2.entity.config_entity import DataValidationConfig
from pathlib import Path


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:   # We are looking for a boolean type output like True or False
        try:
            validation_status = None  # initially validation status is None
            data = pd.read_csv(self.config.unzip_data_dir) # Load the data into variable called data
            all_cols = list(data.columns) # convert the data.columns to list, from the data

            all_schema = self.config.all_schema.keys() # load all the schema. 

            #Validating/cpmpare if all the columns and schema are matching or not. Return True is yes, else return False. 

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status : {validation_status}")
            return validation_status
        except Exception as e:
            raise Exception