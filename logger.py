import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name: str = 'dev-toolkit-91'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    log_formatter = logging.Formatter(
        '[%(asctime)s] {%(levelname)s} (%(filename)s:%(lineno)d) -> %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        f'logs/{name}.log', 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    file_handler.setFormatter(log_formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

logger = get_game_logger()