import datetime
import typing

class GamingLogger:
    """Advanced console logger for dev-toolkit-91 entities."""

    def __init__(self, prefix: str = "[DEV-TOOLKIT]") -> None:
        self.prefix: str = prefix

    def log(self, message: str, level: str = "INFO") -> None:
        """Formats and outputs a message with game-state metadata."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_msg: str = f"{self.prefix} {timestamp} | {level.upper():<5} | {message}"
        print(formatted_msg)

    def debug_frame(self, frame_data: typing.Dict[str, typing.Any]) -> None:
        """Dumps frame-specific state for debugging glitchy movement."""
        for key, value in frame_data.items():
            self.log(f"[FRAME_DUMP] {key}: {value}", level="DEBUG")

def get_default_logger() -> GamingLogger:
    """Factory for persistent dev-toolkit-91 logger instance."""
    return GamingLogger()