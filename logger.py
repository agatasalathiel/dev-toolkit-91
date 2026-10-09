import sys
import time
import inspect
from typing import Any

class GamingLogger:
    def __init__(self, tag: str = "DEV-TOOLKIT-91"):
        self.tag = tag
        self.colors = {
            "info": "\033[94m",
            "warn": "\033[93m",
            "crit": "\033[91m",
            "reset": "\033[0m"
        }

    def _format(self, level: str, msg: Any) -> str:
        caller = inspect.stack()[2].function
        ts = time.strftime("%H:%M:%S", time.localtime())
        return f"{self.colors[level]}[{ts}][{self.tag}][{caller}]{self.colors['reset']} {msg}"

    def log(self, level: str, msg: Any) -> None:
        print(self._format(level, msg), file=sys.stdout)

    def snapshot(self, data: dict, label: str = "state") -> None:
        dump = " | ".join([f"{k}:{v}" for k, v in data.items()])
        self.log("info", f"SNAPSHOT::{label.upper()} -> {dump}")

    def alert(self, msg: str) -> None:
        self.log("crit", f"!!! {msg.upper()} !!!")

game_logger = GamingLogger()