import os
from src.cnnClassifier.utils.common import read_yaml, create_directories
from src.cnnClassifier.constants import (CONFIG_FILE_PATH,PARAMS_FILE_PATH)
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
# from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
# from src.cnnClassifier.entity.config_entity import TrainingConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config['artifacts_root']])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config
        data_ingestion_config = config['data_ingestion']
        create_directories([data_ingestion_config['root_dir']])

        return DataIngestionConfig(
            root_dir=data_ingestion_config['root_dir'],
            source_URL=data_ingestion_config['source_URL'],
            local_data_file=data_ingestion_config['local_data_file'],
            unzip_dir=data_ingestion_config['unzip_dir']
        )