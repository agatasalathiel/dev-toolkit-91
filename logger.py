import logging
from logging.handlers import RotatingFileHandler
import os

def setup_dev_logger(name: str = 'dev-toolkit-91', log_file: str = 'toolkit.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | [dev-kit] %(message)s',
        datefmt='%H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# gaming-centric shortcut
log = setup_dev_logger()