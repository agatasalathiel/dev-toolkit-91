import re

def validate_game_input(user_input, min_len=3, max_len=20):
    """Sanitizes raw console strings for engine safety."""
    if not isinstance(user_input, str):
        return False
    clean_data = user_input.strip()
    if not (min_len <= len(clean_data) <= max_len):
        return False
    return bool(re.match(r'^[a-zA-Z0-9_\-]+$', clean_data))

class InputGuard:
    """Decorator-like filter for stream processing loops."""
    def __init__(self, fallback_val=None):
        self.fallback = fallback_val

    def process(self, raw_stream):
        return [item if validate_game_input(item) else self.fallback for item in raw_stream]

def run_safe_loop(input_queue):
    """
    Main processing loop integration logic.
    Drops malicious sequences before hitting the engine.
    """
    validator = InputGuard(fallback_val="[INVALID_OP]")
    results = []
    for batch in input_queue:
        clean_batch = validator.process(batch)
        results.extend([item for item in clean_batch if item != "[INVALID_OP]"])
    return results