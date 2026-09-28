import logging
import os
from logging.handlers import RotatingFileHandler

RARITY_MAP = {
    logging.DEBUG: "[COMMON]",
    logging.INFO: "[UNCOMMON]",
    logging.WARNING: "[RARE]",
    logging.ERROR: "[EPIC]",
    logging.CRITICAL: "[LEGENDARY]"
}

class QuestLogFormatter(logging.Formatter):
    """Custom log formatter dressing up standard levels as game loot rarities."""
    def format(self, record: logging.LogRecord) -> str:
        rarity = RARITY_MAP.get(record.levelno, "[TRASH]")
        timestamp = self.formatTime(record, "%H:%M:%S")
        return f"⚔️ [{timestamp}] {rarity:<11} {record.name} :: {record.getMessage()}"

def init_game_logger(name: str = "realm_event", file_path: str = "logs/quest.log", max_bytes: int = 256 * 1024, backup_count: int = 3) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        return logger

    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
        
    rotating_handler = RotatingFileHandler(
        filename=file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    
    formatter = QuestLogFormatter()
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

if __name__ == "__main__":
    log = init_game_logger()
    log.info("Player entered the Dragon Spine Cavern.")
    log.warning("Health potion count dropping below critical threshold!")
