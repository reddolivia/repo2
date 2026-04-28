import logging
import os
import sys
from datetime import datetime

"""LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)"""

#logging.basicConfig(
#    filename=LOG_FILE_PATH,
 #   format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
  #  level=logging.INFO,
   # force=True
#)


"""file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

"""



import logging
import os

LOG_FILE = "app.log"
LOG_PATH = os.path.join(os.getcwd(), LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(sys.stdout),
    ],
)
