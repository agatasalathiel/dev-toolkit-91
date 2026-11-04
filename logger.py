import time
import inspect
from typing import Any

class GameLogger:
    def __init__(self, tag: str = "DEV-TK-91"):
        self.tag = tag.upper()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start_time) * 1000
            caller = inspect.stack()[1].function
            self._log_payload(caller, duration, result)
            return result
        return wrapper

    def _log_payload(self, context: str, duration: float, data: Any):
        timestamp = time.strftime("%H:%M:%S", time.gmtime())
        print(f"[{self.tag}] {timestamp} | Context: {context} | Latency: {duration:.4f}ms | Result: {type(data).__name__}")

    @staticmethod
    def emergency_dump(data: dict):
        """Unorthodox snapshot mechanism for immediate state persistence"""
        with open("crash_snapshot.log", "a") as f:
            f.write(f"[SNAPSHOT] {time.time()} -> {data}\n")

log_event = GameLogger()