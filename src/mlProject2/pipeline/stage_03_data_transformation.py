from src.mlProject2.config.configuration import ConfigurationManager
from src.mlProject2.components.data_validation import DataValidation
from src.mlProject2.components.data_transformation import DataTransformation
from pathlib import Path
from src.mlProject2 import logger



STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()  #initialize configuration manager
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config) #initiate Datatransformation class
                data_transformation.train_test_spliting()

            else:
                raise Exception("Your data schema is not valid")
        
        except Exception as e:
            raise e
        