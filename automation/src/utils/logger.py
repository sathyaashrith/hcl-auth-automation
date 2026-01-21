import logging
import os
from datetime import datetime

def get_logger():
    os.makedirs("automation/logs", exist_ok=True)

    logger = logging.getLogger("HCL-AUTH-AUTOMATION")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_file = f"automation/logs/execution.log"

        file_handler = logging.FileHandler(log_file, mode="a")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
