import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dirs = "logs"
log_filepath = os.path.join(log_dirs,"running_logs.log")
os.makedirs(log_dirs, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
)

logger = logging.getLogger("cnnClassfierLogger")