from src.mlProject2.config.configuration import ConfigurationManager
from src.mlProject2.components.model_evaluation import ModelEvaluation
from src.mlProject2 import logger



STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  #initialize configuration manager
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config) #initiate Model trainer class
        model_evaluation_config.save_results()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e