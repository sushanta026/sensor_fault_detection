import logging
import os,sys
from datetime import datetime

#log file name 
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"


#Log directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")

#create folder if not availavle
os.makedirs(LOG_FILE_DIR, exist_ok=True)


#log_file_path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)











