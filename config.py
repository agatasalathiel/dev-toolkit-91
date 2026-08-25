import json
import os
from typing import Any, Dict
class GameConfig:
    DEFAULTS = {
        "title": "Epic Quest",
        "width": 1920,
        "height": 1080,
        "fps": 60,
        "sound_volume": 0.8,
        "music_volume": 0.5,
        "key_bindings": {
            "move_up": "w",
            "move_down": "s",
            "jump": "space",
            "attack": "mouse_left"
        },
        "graphics": {
            "shadows": True,
            "antialiasing": False
        }
    }
    def __init__(self, path: str = "game_config.json") -> None:
        self.path = path
        self.data: Dict[str, Any] = self._load()
    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                loaded = json.load(file)
            return self._merge(self.DEFAULTS, loaded)
        else:
            self._save(self.DEFAULTS)
            return self.DEFAULTS.copy()
    def _merge(self, defaults: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
        result = defaults.copy()
        for key, value in overrides.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge(result[key], value)
            else:
                result[key] = value
        return result
    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self.data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    def set(self, key: str, value: Any) -> None:
        keys = key.split(".")
        current = self.data
        for k in keys[:-1]:
            if k not in current or not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
        self._save(self.data)
    def reset_to_defaults(self) -> None:
        self.data = self.DEFAULTS.copy()
        self._save(self.data)