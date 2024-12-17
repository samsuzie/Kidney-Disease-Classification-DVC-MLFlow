# # importing the logger inside the main file
# from src.cnnClassifier import logger
# logger.info("Welcome to our custom log")

# first we will import data ingestion pipeline and my logger
from src.cnnClassifier.utils import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
# from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage "
try:
    logger.info(f">>>>>>stage{STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e