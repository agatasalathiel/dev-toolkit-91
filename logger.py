import logging
from logging.handlers import RotatingFileHandler
import os
import sys

class QuestLogFormatter(logging.Formatter):
    """Custom log formatter styling records as RPG system notifications."""
    SEVERITY_TAGS = {
        logging.DEBUG: "⚔️  [LOOT]",
        logging.INFO: "📜 [QUEST]",
        logging.WARNING: "⚠️  [DANGER]",
        logging.ERROR: "💥 [CRIT]",
        logging.CRITICAL: "💀 [WIPE]"
    }

    def format(self, record):
        tag = self.SEVERITY_TAGS.get(record.levelno, "🎮 [GAME]")
        timestamp = self.formatTime(record, "%H:%M:%S")
        record.msg = f"{tag} [{timestamp}] {record.msg}"
        return super().format(record)

def setup_game_logger(
    logger_name: str = "session_telemetry",
    log_dir: str = "saved_logs",
    max_bytes: int = 512 * 1024,
    backup_count: int = 3
) -> logging.Logger:
    """Initializes a rotating file logger for tracking game session events."""
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        return logger

    log_filepath = os.path.join(log_dir, f"{logger_name}.log")
    file_handler = RotatingFileHandler(
        log_filepath, 
        maxBytes=max_bytes, 
        backupCount=backup_count, 
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    formatter = QuestLogFormatter("%(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

if __name__ == "__main__":
    game_log = setup_game_logger()
    game_log.info("Entered dungeon: Obsidian Spire")
    game_log.debug("Acquired item: Ring of Mana Regeneration")
    game_log.warning("Boss 'Dragon Sovereign' entered rage mode!")
    game_log.error("Health dropped below 10%")
    game_log.critical("Party wiped on floor 50")
