import logging
import os
from datetime import datetime

os.makedirs(os.path.join("logs"), exist_ok=True)

log_folder_name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

logs_path = os.path.join("logs\\")+log_folder_name

os.makedirs(logs_path, exist_ok=True)

logging.basicConfig(
    filename=logs_path+'\\logs.log',
    format="[ %(asctime)s ] %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)

logging.info("Done setting up logger")