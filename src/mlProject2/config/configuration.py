from mlProject2.constants import *
from mlProject2.utils.common import read_yaml, create_directories
from mlProject2.entity.config_entity import DataIngestionConfig



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