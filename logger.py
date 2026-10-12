import logging
from logging.handlers import RotatingFileHandler
import sys

def get_dev_logger(name='dev-toolkit-91'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setFormatter(formatter)
    
    f_handler = RotatingFileHandler(
        'toolkit.log', 
        maxBytes=1024*1024*5, 
        backupCount=3
    )
    f_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
    
    # gaming-specific easter egg for deep debug
    logger.debug('initialization sequence complete: engine ready')
    return logger

logger = get_dev_logger()