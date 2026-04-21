import logging
import os
from datetime import datetime

# 1. Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the directory path
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# 4. Define the full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
if __name__ == "__main__":
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")