import json
from pathlib import Path
from typing import Any, Dict, Union

GAMING_DEFAULTS = {
    "video": {
        "resolution": (1920, 1080),
        "fps_cap": 144,
        "fov": 90,
        "vsync": False,
        "preset": "high"
    },
    "audio": {
        "master_volume": 0.8,
        "sfx_volume": 1.0,
        "bgm_volume": 0.5,
        "mute_on_unfocus": True
    },
    "gameplay": {
        "difficulty": "normal",
        "invert_y": False,
        "auto_save_interval": 300
    }
}

class ConfigNode:
    """A dynamic config wrapper providing attribute fallback to defaults."""
    def __init__(self, data: Dict[str, Any], defaults: Dict[str, Any]):
        self._data = data
        self._defaults = defaults

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            val = self._data[name]
            def_val = self._defaults.get(name, {})
        elif name in self._defaults:
            val = self._defaults[name]
            def_val = val
        else:
            raise AttributeError(f"Configuration key '{name}' not found.")

        if isinstance(val, dict) and isinstance(def_val, dict):
            return ConfigNode(val, def_val)
        return val

    def __getitem__(self, item: str) -> Any:
        return self.__getattr__(item)

    def to_dict(self) -> Dict[str, Any]:
        merged = self._defaults.copy()
        for k, v in self._data.items():
            if isinstance(v, dict) and isinstance(merged.get(k), dict):
                merged[k] = ConfigNode(v, merged[k]).to_dict()
            else:
                merged[k] = v
        return merged

class ConfigLoader:
    """Loads gaming configurations with cascading preset fallbacks."""
    def __init__(self, config_path: Union[str, Path] = "game_settings.json"):
        self.config_path = Path(config_path)

    def load(self, custom_defaults: Dict[str, Any] = None) -> ConfigNode:
        base_defaults = GAMING_DEFAULTS.copy()
        if custom_defaults:
            base_defaults.update(custom_defaults)

        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                user_data = {}
        else:
            user_data = {}

        return ConfigNode(user_data, base_defaults)
