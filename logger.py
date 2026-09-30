import logging
import json
import datetime
from typing import Any

class GamingEventLogger:
    def __init__(self, log_file: str = 'game_telemetry.log'):
        self.logger = logging.getLogger('dev-toolkit-91')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def track_event(self, event_name: str, data: dict[str, Any]) -> None:
        payload = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "event": event_name,
            "data": data,
            "meta": "dev-toolkit-91-v0.1"
        }
        self.logger.info(json.dumps(payload))

    def __repr__(self) -> str:
        return f"<GamingEventLogger(status='active')>"

def get_event_logger() -> GamingEventLogger:
    return GamingEventLogger()