import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")  # CWD current working directory
os.makedirs(log_path, exist_ok=True)  # Create directory if it doesn't exist


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,  # Use 'filename' instead of 'file_name'
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")