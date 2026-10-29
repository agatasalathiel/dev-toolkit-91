import os
import logging
from logging.handlers import RotatingFileHandler
import time

class QuestLogFormatter(logging.Formatter):
    """Custom formatter translating log severity into RPG event tiers with HUD frames."""
    
    LEVEL_BADGES = {
        logging.DEBUG: "[Loot Drop]",
        logging.INFO: "[Quest Progress]",
        logging.WARNING: "[Mana Drain]",
        logging.ERROR: "[Boss Attack]",
        logging.CRITICAL: "[PARTY WIPE]"
    }

    def format(self, record: logging.LogRecord) -> str:
        badge = self.LEVEL_BADGES.get(record.levelno, "[Event]")
        timestamp = time.strftime("%H:%M:%S", time.localtime(record.created))
        frame_id = getattr(record, "frame_id", 0)
        return f"{timestamp} | F#{frame_id:06d} | {badge:<16} {record.getMessage()}"


class GameSessionLogger:
    """Self-contained session logger setup with automated byte-based rotation."""

    def __init__(self, session_id: str, log_dir: str = "logs", max_bytes: int = 51200, backup_count: int = 5):
        self.session_id = session_id
        self.log_dir = log_dir
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        os.makedirs(self.log_dir, exist_ok=True)

    def setup(self) -> logging.Logger:
        logger = logging.getLogger(f"game.session.{self.session_id}")
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        if logger.hasHandlers():
            logger.handlers.clear()

        filepath = os.path.join(self.log_dir, f"session_{self.session_id}.log")
        handler = RotatingFileHandler(
            filepath, maxBytes=self.max_bytes, backupCount=self.backup_count, encoding="utf-8"
        )
        handler.setFormatter(QuestLogFormatter())
        logger.addHandler(handler)

        return logger


def get_game_logger(session_id: str = "main_session") -> logging.Logger:
    builder = GameSessionLogger(session_id=session_id)
    return builder.setup()
