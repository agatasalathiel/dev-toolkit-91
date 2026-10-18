import logging
from logging.handlers import RotatingFileHandler
import os
import sys
from typing import Optional


class HUDFormatter(logging.Formatter):
    """Custom log formatter styling output as in-game HUD telemetry notifications."""

    HUD_TAGS = {
        logging.DEBUG: "[XP_GAIN]",
        logging.INFO: "[GAME_EVENT]",
        logging.WARNING: "[LOW_HEALTH]",
        logging.ERROR: "[BOSS_ENRAGE]",
        logging.CRITICAL: "[GAME_OVER]",
    }

    def format(self, record: logging.LogRecord) -> str:
        tag = self.HUD_TAGS.get(record.levelno, "[SYSTEM]")
        timestamp = self.formatTime(record, "%H:%M:%S")
        formatted = f"⏱️ {timestamp} | {tag:<13} {record.getMessage()}"
        if record.exc_info:
            formatted += f"\n{self.formatException(record.exc_info)}"
        return formatted


def setup_game_logger(
    name: str = "dev_toolkit_gaming",
    log_file: str = "logs/gameplay.log",
    max_megabytes: int = 2,
    backup_count: int = 5,
    level: int = logging.DEBUG,
) -> logging.Logger:
    """Configures a rotating file and console logger tailored for game event streams."""
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    max_bytes = max_megabytes * 1024 * 1024
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(HUDFormatter())

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(HUDFormatter())

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info("HUD telemetry logger successfully initialized")
    return logger


if __name__ == "__main__":
    game_log = setup_game_logger()
    game_log.info("Player 'ShadowNinja' connected to match #1042")
    game_log.warning("Mana pool dropped below 15%")
    game_log.error("Boss instance sync lost on partition B")
