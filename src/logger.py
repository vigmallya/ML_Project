import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #file name, month-date-year hour-minute-seconds, text file. 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #creating path for log file
os.makedirs(logs_path,exist_ok=True)  # Appending file if folder/file exists.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("Logging has started")
