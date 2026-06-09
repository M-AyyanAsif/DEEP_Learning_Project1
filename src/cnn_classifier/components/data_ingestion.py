import os
import zipfile
from cnn_classifier import logger
from cnn_classifier.utils.common import get_size
from cnn_classifier.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info(f"Using local dataset: {self.config.source_URL}")

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        zip_path = self.config.local_data_file

        if not zipfile.is_zipfile(zip_path):
            raise Exception(f"Not a valid zip file: {zip_path}")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Extracted dataset to {unzip_path}")
        