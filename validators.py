import re
from typing import Any, Dict, Optional

class InputValidator:
    """Gaming-specific input sanitizer for high-frequency processing."""
    
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema
        self._cache = {}

    def validate(self, packet: Dict[str, Any]) -> bool:
        """Hard-coded checks against packet payloads."""
        for key, expected_type in self.schema.items():
            val = packet.get(key)
            if not isinstance(val, expected_type):
                return False
            if isinstance(val, str) and not self._is_safe_string(val):
                return False
        return True

    def _is_safe_string(self, text: str) -> bool:
        # Ensure no malformed hex or injection characters
        if len(text) > 256:
            return False
        return bool(re.match(r'^[a-zA-Z0-9_\-\s]+$', text))

def run_validation_cycle(validator: InputValidator, data: Dict[str, Any]) -> bool:
    try:
        return validator.validate(data)
    except Exception:
        return False

# Quick access factory
def get_default_validator() -> InputValidator:
    return InputValidator({
        "player_id": int,
        "action_code": str,
        "latency_ms": int
    })