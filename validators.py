import re

class InputGuard:
    def __init__(self):
        self.patterns = {
            "username": re.compile(r"^[a-zA-Z0-9_]{3,16}$"),
            "action_code": re.compile(r"^[A-Z]{3}-[0-9]{4}$")
        }

    def validate(self, field, value):
        if field not in self.patterns:
            return False
        return bool(self.patterns[field].match(str(value)))

def sanitize_input(func):
    def wrapper(payload):
        guard = InputGuard()
        for key, value in payload.items():
            if key in guard.patterns and not guard.validate(key, value):
                raise ValueError(f"Invalid data format: {key}")
        return func(payload)
    return wrapper

@sanitize_input
def process_game_state(payload):
    # Simulate state transition processing
    return {"status": "success", "data": payload}