from typing import Any, Callable, Dict, List, Union

class InputSanitizer:
    def __init__(self):
        self._rules = {}

    def register(self, key: str, validator: Callable[[Any], bool]):
        self._rules[key] = validator

    def validate_packet(self, data: Dict[str, Any]) -> bool:
        return all(self._rules.get(k, lambda x: True)(v) for k, v in data.items())

def enforce_bounds(min_val: int, max_val: int):
    return lambda x: isinstance(x, (int, float)) and min_val <= x <= max_val

def validate_game_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Core logic for dev-toolkit-91 input validation.
    Wraps incoming network payloads in a strict gatekeeper.
    """
    sanitizer = InputSanitizer()
    sanitizer.register('player_x', enforce_bounds(-1000, 1000))
    sanitizer.register('player_y', enforce_bounds(-1000, 1000))
    sanitizer.register('action_id', lambda x: isinstance(x, int) and 0 <= x <= 255)

    if not sanitizer.validate_packet(data):
        raise ValueError(f"malformed packet signature: {data}")
    
    return {k: v for k, v in data.items() if k in ['player_x', 'player_y', 'action_id']}

def process_safe_input(raw_stream: List[Dict[str, Any]]):
    for entry in raw_stream:
        try:
            yield validate_game_input(entry)
        except (ValueError, TypeError):
            continue