from typing import Dict, Any, Final
from dataclasses import dataclass

@dataclass(frozen=True)
class GameSettings:
    """Immutable configuration container for dev-toolkit-91 environment."""
    fps_cap: int = 144
    render_engine: str = "vulkan"
    debug_mode: bool = False

def load_settings(data: Dict[str, Any]) -> GameSettings:
    """Parses raw dictionary input into a type-safe settings object."""
    return GameSettings(
        fps_cap=int(data.get("fps", 60)),
        render_engine=str(data.get("engine", "opengl")),
        debug_mode=bool(data.get("debug", False))
    )

DEFAULT_CONFIG: Final[GameSettings] = GameSettings()

class ConfigRegistry:
    """Singleton-like storage for active toolkit runtime configuration."""
    _instance: Dict[str, GameSettings] = {}

    @classmethod
    def update(cls, key: str, config: GameSettings) -> None:
        """Registers a new configuration set by key."""
        cls._instance[key] = config

    @classmethod
    def fetch(cls, key: str) -> GameSettings:
        """Retrieves config, falling back to default if missing."""
        return cls._instance.get(key, DEFAULT_CONFIG)