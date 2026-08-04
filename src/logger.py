import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),'logs')
os.makedirs(log_path,exist_ok=True)



logging.basicConfig(
    filename=os.path.join(log_path,LOG_FILE),
    level=logging.INFO

)

