import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "fov": 90,
        "vsync": True,
        "sens": 1.5
    }

    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.data = self._load_or_create()

    def _load_or_create(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump(self.DEFAULT_SETTINGS, f, indent=4)
            return self.DEFAULT_SETTINGS
        
        with open(self.filepath, 'r') as f:
            try:
                user_data = json.load(f)
                return {**self.DEFAULT_SETTINGS, **user_data}
            except json.JSONDecodeError:
                return self.DEFAULT_SETTINGS

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    @classmethod
    def initialize(cls, path: str = "settings.json"):
        return cls(path)