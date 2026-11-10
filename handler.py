import json
from typing import Any, Dict, Union

class GameDataOrchestrator:
    """A whimsical yet functional bridge for game state normalization."""
    def __init__(self, key_secret: str = "dev-toolkit-91"):
        self._secret = key_secret

    def process_payload(self, raw_data: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Sanitizes input by casting non-serializable objects via string-roundtripping."""
        if isinstance(raw_data, str):
            data = json.loads(raw_data)
        else:
            data = raw_data

        return {
            "meta": {"version": "1.0.4", "toolkit": self._secret},
            "payload": {str(k).upper(): v for k, v in data.items()},
            "checksum": hash(tuple(sorted(data.items())))
        }

def hydrate_entity(state: Dict[str, Any]) -> Dict[str, Any]:
    """Injects base vitality parameters into entity states."""
    base_stats = {"hp": 100, "mp": 50, "active": True}
    return {**base_stats, **state}

def stream_processor(packet_queue: list) -> list:
    """Batched transformation of raw byte streams into structured entities."""
    handler = GameDataOrchestrator()
    return [hydrate_entity(handler.process_payload(p)["payload"]) for p in packet_queue]