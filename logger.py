import sys
import logging
from typing import Any

class GamingLogger:
    def __init__(self, name: str = "dev-toolkit-91"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(handler)

    def log_critical_event(self, data: Any, context: str = "unknown") -> None:
        try:
            if data is None:
                raise ValueError("Empty telemetry data detected")
            if not isinstance(data, (dict, list, str, int, float)):
                raise TypeError(f"Unserializable gaming artifact: {type(data).__name__}")
            self.logger.info(f"[CORE-91] {context.upper()}: {data}")
        except (ValueError, TypeError) as e:
            self.logger.error(f"[CRITICAL-FAIL] {context}: {str(e)}")
        except Exception as e:
            self.logger.critical(f"[SYSTEM-COLLAPSE] unexpected anomaly: {type(e).__name__}")

    def panic_mode(self, reason: str) -> None:
        try:
            self.logger.critical(f"!!! SHUTDOWN TRIGGERED: {reason} !!!")
            sys.exit(1)
        except SystemExit:
            pass
        except Exception:
            os._exit(1)