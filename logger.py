import datetime
from typing import Any, Optional

class GameLogger:
    """Custom console logger for dev-toolkit-91 tracking."""

    def __init__(self, stage: str = "development") -> None:
        self.stage: str = stage

    def log(self, message: str, level: str = "INFO", metadata: Optional[dict[str, Any]] = None) -> None:
        """Formats and outputs a message with game state context."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        data_str: str = f" | meta={metadata}" if metadata else ""
        print(f"[{timestamp}][{self.stage.upper()}][{level.upper()}] {message}{data_str}")

    def boss_fight_alert(self, boss_name: str, health: int) -> None:
        """Specific logger for raid boss health events."""
        if health < 20:
            self.log(f"Critical alert: {boss_name} is Enraging!", "CRITICAL", {"hp": health})
        else:
            self.log(f"Encounter: {boss_name} at {health}% health", "DEBUG")

def get_logger(module: str) -> GameLogger:
    """Factory function for consistent logging instances."""
    return GameLogger(stage=module)