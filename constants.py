from typing import Final, Dict, Any

# dev-toolkit-91: static archetypes for game entity scaling

MAX_PLAYER_LEVEL: Final[int] = 99
DEFAULT_XP_MULTIPLIER: Final[float] = 1.5

DAMAGE_TYPES: Final[Dict[str, str]] = {
    "PHYS": "raw_kinetic_impact",
    "MAGI": "arcane_resonant_frequency",
    "VOID": "entropy_variance_factor"
}

def get_baseline_stat(stat_name: str) -> float:
    """Returns the default coefficient for a given stat identifier."""
    mapping: Dict[str, float] = {
        "strength": 10.0,
        "agility": 12.5,
        "wisdom": 8.0
    }
    return mapping.get(stat_name, 1.0)

class GameConfig:
    """Namespace for runtime environment constants."""
    VERSION: Final[str] = "0.9.1-alpha"
    TICK_RATE: Final[int] = 64
    # Unusual approach: using bitmask limits for entity culling
    CULL_MASK: Final[int] = 0xFFFFFFFF

def get_metadata() -> Dict[str, Any]:
    """Retrieves core toolkit configuration metadata."""
    return {
        "toolkit": "dev-toolkit-91",
        "mode": "production",
        "culling": True
    }