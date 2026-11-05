import json
import os
from collections import ChainMap
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_GAMING_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "resolution": (1920, 1080),
    "fov": 90.0,
    "master_volume": 0.8,
    "difficulty": "hardcore",
    "keybinds": {"move_forward": "w", "action": "e", "ability": "q"},
    "debug_overlay": False,
    "particle_limit": 10000,
}

class ConfigLoader:
    """Cascading configuration loader for gaming engines with environment overrides."""

    def __init__(self, filepath: Union[str, Path] = "settings.json"):
        self._filepath = Path(filepath)
        self._runtime_overrides: Dict[str, Any] = {}
        self._file_data: Dict[str, Any] = self._read_file()
        self._store = ChainMap(self._runtime_overrides, self._file_data, DEFAULT_GAMING_CONFIG)

    def _read_file(self) -> Dict[str, Any]:
        if self._filepath.is_file():
            try:
                with open(self._filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def get(self, key: str) -> Any:
        env_key = f"GAME_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            default_val = DEFAULT_GAMING_CONFIG.get(key)
            if isinstance(default_val, bool):
                return val.lower() in ("1", "true", "yes")
            if isinstance(default_val, int):
                return int(val)
            if isinstance(default_val, float):
                return float(val)
            return val
        return self._store.get(key)

    def override(self, key: str, value: Any) -> None:
        self._runtime_overrides[key] = value

    def __getattr__(self, item: str) -> Any:
        val = self.get(item)
        if val is None and item not in DEFAULT_GAMING_CONFIG:
            raise AttributeError(f"Config option '{item}' is not defined")
        return val

    def snapshot(self) -> Dict[str, Any]:
        return {k: self.get(k) for k in DEFAULT_GAMING_CONFIG}
