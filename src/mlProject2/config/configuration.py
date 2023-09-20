from mlProject2.constants import *
from mlProject2.utils.common import read_yaml, create_directories
from mlProject2.entity.config_entity import (DataIngestionConfig, 
                                             DataValidationConfig, 
                                             DataTransformationConfig,
                                             ModelTrainerConfig,
                                             ModelEvaluationConfig)




class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # storing the data_ingestion config into into variable config

        create_directories([config.root_dir]) # create root directory for the variable config 

         # Returning the data type as defined in the DataIngestionCofig in the entity
#        # reading one by one from the config variable and storing them to assigned variables like root_dir, source_URL etc. 


        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation # storing the data_ingestion config into into variable config
        schema = self.schema.COLUMNS

        create_directories([config.root_dir]) # create root directory for the variable config 

         # Returning the data type as defined in the DataIngestionCofig in the entity
#        # reading one by one from the config variable and storing them to assigned variables like root_dir, source_URL etc. 


        data_ingestion_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema= schema,
        
        )

        return data_ingestion_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation # storing the data_ingestion config into into variable config

        create_directories([config.root_dir]) # create root directory for the variable config 

        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer # storing the data_ingestion config into into variable config
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir]) # create root directory for the variable config 

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha= params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation # storing the data_ingestion config into into variable config
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir]) # create root directory for the variable config 

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            
    
            model_path = config.model_path,
            all_params = params,
            metric_file_name = config.metric_file_name,
            target_column= schema.name
        )
        return model_evaluation_config
    

