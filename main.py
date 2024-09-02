from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTarinigPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f"Starting {STAGE_NAME}")
        data_ingestion = DataIngestionTarinigPipeline()
        data_ingestion.main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e                                 