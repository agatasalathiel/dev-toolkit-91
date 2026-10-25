import logging
from logging.handlers import RotatingFileHandler
import os

def setup_dev_toolkit_logger(name='dev-toolkit-91', log_file='game.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | [%(name)s] -> %(message)s',
        datefmt='%H:%M:%S'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5,
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def get_logger():
    return logging.getLogger('dev-toolkit-91')

if __name__ == '__main__':
    log = setup_dev_toolkit_logger()
    log.info('System operational: dev-toolkit-91 initialized')