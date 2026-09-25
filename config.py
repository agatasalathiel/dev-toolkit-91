import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, file_path: str, defaults: Dict[str, Any]):
        self.path = file_path
        self.data = defaults.copy()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    disk_data = json.load(f)
                    self.data.update({k: v for k, v in disk_data.items() if k in self.data})
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def __getattr__(self, item: str) -> Any:
        return self.data.get(item)

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def override(self, **kwargs) -> None:
        self.data.update(kwargs)

# Gaming engine defaults
DEFAULT_SETTINGS = {
    "resolution": [1920, 1080],
    "vsync": True,
    "fov": 90,
    "sensitivity": 1.5
}

def get_config(path: str = "settings.json") -> ConfigLoader:
    return ConfigLoader(path, DEFAULT_SETTINGS)