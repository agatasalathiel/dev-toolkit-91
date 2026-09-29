import time
import collections
from typing import Dict, Any, Callable

class GameEventStream:
    def __init__(self):
        self._buffer: Dict[str, list] = collections.defaultdict(list)
        self._registry: Dict[str, Callable] = {}

    def register(self, event_type: str, callback: Callable):
        self._registry[event_type] = callback

    def emit(self, event_type: str, data: Any):
        self._buffer[event_type].append({'ts': time.time(), 'payload': data})

    def process_all(self):
        for etype, events in self._buffer.items():
            if etype in self._registry:
                handler = self._registry[etype]
                while events:
                    evt = events.pop(0)
                    try:
                        handler(evt['payload'])
                    except Exception as e:
                        print(f"fault in {etype}: {e}")

def handle_player_death(data):
    print(f"respawning player {data['id']} at checkpoint")

def handle_loot_drop(data):
    print(f"spawning item {data['item']} at {data['coords']}")

event_handler = GameEventStream()
event_handler.register("death", handle_player_death)
event_handler.register("loot", handle_loot_drop)