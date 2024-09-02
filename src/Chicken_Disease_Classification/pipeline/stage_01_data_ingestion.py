from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.data_ingestion import DataIngestion
from Chicken_Disease_Classification import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTarinigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataIngestionTarinigPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e
