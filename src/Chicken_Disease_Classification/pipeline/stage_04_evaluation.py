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


