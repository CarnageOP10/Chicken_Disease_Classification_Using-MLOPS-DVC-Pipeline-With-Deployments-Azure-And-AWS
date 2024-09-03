from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.prepare_base_model import PrepareBaseModel
from Chicken_Disease_Classification import logger



STAGE_NAME = "Prepare Base model"

class PrepareBaseModelTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = PrepareBaseModelTrainigPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e