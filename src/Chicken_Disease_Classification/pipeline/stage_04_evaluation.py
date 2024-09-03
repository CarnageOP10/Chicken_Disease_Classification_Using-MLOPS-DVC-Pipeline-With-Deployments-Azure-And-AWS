from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.model_training import Training
from Chicken_Disease_Classification.components.prepare_callbacks import PrepareCallback
from Chicken_Disease_Classification.components.model_evaluation import Evaluation
from Chicken_Disease_Classification import logger

STAGE_NAME = "Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
        try:
            logger.info(f"*******************")
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelEvaluationPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e


