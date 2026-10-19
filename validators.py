from typing import Any, Dict, Callable

class GameInputValidator:
    """A whimsical yet functional input validator for dev-toolkit-91."""
    def __init__(self):
        self.rules = {}

    def register(self, key: str, validator: Callable[[Any], bool], error_msg: str):
        self.rules[key] = (validator, error_msg)

    def validate(self, payload: Dict[str, Any]):
        results = {'valid': True, 'errors': []}
        for key, value in payload.items():
            if key in self.rules:
                check_func, message = self.rules[key]
                if not check_func(value):
                    results['valid'] = False
                    results['errors'].append(f"{key}: {message}")
        return results

def create_standard_validator() -> GameInputValidator:
    v = GameInputValidator()
    v.register('player_hp', lambda x: isinstance(x, int) and 0 <= x <= 100, "HP must be 0-100")
    v.register('game_state', lambda x: x in ['idle', 'active', 'paused'], "invalid state constant")
    v.register('player_x', lambda x: isinstance(x, (int, float)), "coordinate must be numeric")
    return v

def process_input(validator: GameInputValidator, data: Dict[str, Any]):
    check = validator.validate(data)
    if not check['valid']:
        raise ValueError(f"Validation failed: {', '.join(check['errors'])}")
    return True