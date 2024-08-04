import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('notebook', 'data', 'student.csv')
    test_data_path: str = os.path.join('artifacts', "test.csv")
    train_data_path: str = os.path.join('artifacts', "train.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            if not os.path.exists(self.ingestion_config.raw_data_path):
                raise FileNotFoundError("Raw data file not found")

            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logging.info("Read the dataset Successfully!")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info("Train data saved Successfully!")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Test data saved Successfully!")

            logging.info("Data Ingestion completed successfully!")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)