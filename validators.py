import re

class GameValidator:
    """Creative validation logic for dev-toolkit-91 gaming assets"""
    
    @staticmethod
    def is_valid_entity_name(name: str) -> bool:
        # Allow alphanumeric, underscores, and hyphens; 3-16 chars
        return bool(re.match(r'^[a-zA-Z0-9_-]{3,16}$', name))

    @staticmethod
    def clamp_stat(value: float, min_val: float = 0.0, max_val: float = 100.0) -> float:
        # Force values into the standard gaming bracket
        return max(min_val, min(value, max_val))

    @staticmethod
    def validate_hex_color(hex_str: str) -> bool:
        # Check for standard 6-digit hex format used in game UIs
        pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
        return bool(pattern.match(hex_str))

    @staticmethod
    def sanitize_coordinates(coords: tuple) -> tuple:
        # Ensure coordinates are within a standard map grid
        return tuple(round(float(c), 2) for c in coords)

    @classmethod
    def check_version(cls, version: str) -> bool:
        # Versioning schema: major.minor.patch
        parts = version.split('.')
        return len(parts) == 3 and all(p.isdigit() for p in parts)