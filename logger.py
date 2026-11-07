import logging
import os
from logging.handlers import RotatingFileHandler

def get_game_logger(name: str = "dev-toolkit-91"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S"
    )

    file_handler = RotatingFileHandler(
        "logs/gaming_engine.log", 
        maxBytes=1024 * 1024 * 5,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

log = get_game_logger()

if __name__ == "__main__":
    log.info("dev-toolkit-91 initialized successfully")