import datetime
from typing import Any, Optional, Union

class GameLogger:
    """Custom console logger for dev-toolkit-91 game engine."""
    
    def __init__(self, debug_mode: bool = False) -> None:
        self.debug_mode: bool = debug_mode
        self.prefix: str = "[DEV-TOOLKIT-91]"

    def log(self, message: Any, severity: str = "INFO") -> None:
        """Formats and prints game events to stdout."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        payload: str = f"{self.prefix} {timestamp} | {severity.upper()} | {message}"
        print(payload)

    def heartbeat(self, frame_id: int) -> None:
        """Debug utility to track engine frame sync."""
        if self.debug_mode:
            self.log(f"frame cycle {frame_id} persistent", "DEBUG")

    def alert(self, error: Exception) -> None:
        """Terminal output for critical engine state violations."""
        self.log(f"CRITICAL: {type(error).__name__} -> {str(error)}", "ERROR")

# Instantiate singleton for global module access
engine_logger: GameLogger = GameLogger(debug_mode=True)