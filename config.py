import json
import os
from typing import Any, Dict

class ConfigVault:
    """Dynamic configuration loader with fallback defaults."""
    def __init__(self, path: str, defaults: Dict[str, Any] = None):
        self._path = path
        self._defaults = defaults or {}
        self._data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self._path):
            return self._defaults
        try:
            with open(self._path, 'r') as f:
                raw = json.load(f)
                return {**self._defaults, **raw}
        except (json.JSONDecodeError, IOError):
            return self._defaults

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def sync(self) -> None:
        with open(self._path, 'w') as f:
            json.dump(self._data, f, indent=4)

def get_game_config(profile: str = 'default.json') -> ConfigVault:
    defaults = {
        "resolution": [1920, 1080],
        "vsync": True,
        "fov": 90,
        "audio_channels": 6
    }
    return ConfigVault(profile, defaults)