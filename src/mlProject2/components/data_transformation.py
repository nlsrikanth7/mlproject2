# update components
# we are only performing train_test split as data is already cleaned up
# You can add different data transformation techniques like Standard Scaler, PCA, all kinds of EDA before passing this data to the model
import os
from src.mlProject2 import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject2.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):   # We are looking for a boolean type output like True or False
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets (0.75, 0.25) split. 
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)