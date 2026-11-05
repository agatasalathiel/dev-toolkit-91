import re

class GameEntityValidator:
    @staticmethod
    def validate_player_tag(tag: str) -> bool:
        # Check for alphanumeric with underscore, length 3-16
        pattern = r'^[a-zA-Z0-9_]{3,16}$'
        return bool(re.match(pattern, tag))

    @staticmethod
    def validate_coordinate_bounds(coord: tuple, limit: int = 1000) -> bool:
        return all(-limit <= val <= limit for val in coord)

    @staticmethod
    def validate_rarity(level: int) -> str:
        # Mapping numeric rarity to string tiers using dictionary dispatch
        tiers = {1: 'common', 2: 'uncommon', 3: 'rare', 4: 'epic', 5: 'legendary'}
        return tiers.get(level, 'trash')

    @staticmethod
    def sanitize_input(data: str) -> str:
        # Remove non-printable characters for clean chat logs
        return ''.join(char for char in data if char.isprintable())

def check_integrity(entity_data: dict) -> bool:
    # Minimalistic schema validation for game objects
    required = {'id', 'type', 'pos'}
    return required.issubset(entity_data.keys())

def format_latency(ms: int) -> str:
    # Color-coded string return for game status overlays
    if ms < 50: return f'[GREEN]{ms}ms'
    if ms < 150: return f'[YELLOW]{ms}ms'
    return f'[RED]{ms}ms'