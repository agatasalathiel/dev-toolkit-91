import json
import os
from typing import Any, Dict

class GameConfig:
    """Dynamic configuration loader with built-in presets for gaming profiles."""
    PRESETS: Dict[str, Dict[str, Any]] = {
        "potato": {"fps_cap": 30, "shadows": False, "texture_res": "low", "vsync": False},
        "retro": {"fps_cap": 60, "shadows": False, "texture_res": "low", "vsync": True},
        "ultra": {"fps_cap": 144, "shadows": True, "texture_res": "high", "vsync": True}
    }
    DEFAULT_PRESET = "retro"

    def __init__(self, config_path: str | None = None):
        self._settings: Dict[str, Any] = {}
        self.load(config_path)

    def load(self, config_path: str | None = None) -> None:
        preset_name = os.getenv("GAME_PRESET", self.DEFAULT_PRESET)
        self._settings = self.PRESETS.get(preset_name, self.PRESETS[self.DEFAULT_PRESET]).copy()

        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, "r") as f:
                    file_data = json.load(f)
                    self._settings.update(file_data)
            except (json.JSONDecodeError, FileNotFoundError):
                pass

        for key, val in os.environ.items():
            if key.startswith("GAME_"):
                setting_key = key[5:].lower()
                if setting_key in self._settings:
                    orig_type = type(self._settings[setting_key])
                    try:
                        if orig_type is bool:
                            self._settings[setting_key] = val.lower() in ("true", "1", "yes")
                        else:
                            self._settings[setting_key] = orig_type(val)
                    except ValueError:
                        self._settings[setting_key] = val
                else:
                    self._settings[setting_key] = val

    def __getattr__(self, name: str) -> Any:
        if name in self._settings:
            return self._settings[name]
        raise AttributeError(f"Configuration setting '{name}' not found")

    def __repr__(self) -> str:
        return f"GameConfig({self._settings!r})"