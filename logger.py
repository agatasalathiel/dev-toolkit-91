import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class GamingLogger:
    def __init__(self, name='dev-toolkit-91', log_path='logs/game_engine.log'):
        self.path = Path(log_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
            datefmt='%H:%M:%S'
        )
        
        handler = RotatingFileHandler(
            self.path,
            maxBytes=1024 * 1024 * 5,
            backupCount=3
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def get_logger(self):
        return self.logger

logger_instance = GamingLogger().get_logger()