import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

class GamingLogger:
    """Custom logger for dev-toolkit-91 gaming engine tasks."""
    def __init__(self, name: str = 'dev-toolkit-91', log_file: str = 'engine.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [PID:%(process)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler = RotatingFileHandler(
            log_dir / log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

log_engine = GamingLogger().get_logger()