import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


class GameSessionRotator(RotatingFileHandler):
    """Custom file rotator that injects quest session metadata headers on rollover."""

    def __init__(self, filename: str, max_bytes: int = 256 * 1024, backup_count: int = 5, realm_name: str = "Valhalla"):
        super().__init__(filename, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8")
        self.realm_name = realm_name
        self.session_id = 1
        self._write_session_header()

    def doRollover(self):
        super().doRollover()
        self.session_id += 1
        self._write_session_header()

    def _write_session_header(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = (
            f"\n=== [REALM: {self.realm_name}] "
            f"[SESSION #{self.session_id:04d}] "
            f"[INIT: {timestamp}] ===\n"
        )
        if self.stream:
            self.stream.write(header)
            self.stream.flush()


def setup_telemetry_logger(
    name: str = "game_engine",
    log_file: str = "quest_telemetry.log",
    realm: str = "Shadowlands"
) -> logging.Logger:
    """Configures telemetry logger with session-aware file rotation."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console_fmt = logging.Formatter("⚔️ [%(levelname)s] [%(name)s]: %(message)s")
    console.setFormatter(console_fmt)

    rotator = GameSessionRotator(
        filename=log_file,
        max_bytes=1024 * 128,
        backup_count=3,
        realm_name=realm
    )
    rotator.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | T:%(thread)d | %(message)s")
    rotator.setFormatter(file_fmt)

    logger.addHandler(console)
    logger.addHandler(rotator)

    return logger
