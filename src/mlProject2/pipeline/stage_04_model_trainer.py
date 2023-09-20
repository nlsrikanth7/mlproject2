from src.mlProject2.config.configuration import ConfigurationManager
from src.mlProject2.components.model_trainer import ModelTrainer
from src.mlProject2 import logger



STAGE_NAME = "Model trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  #initialize configuration manager
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config) #initiate Model trainer class
        model_trainer_config.train()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e