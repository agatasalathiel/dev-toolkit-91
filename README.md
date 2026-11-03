# dev-toolkit-91

`dev-toolkit-91` is a specialized Python library designed to streamline game asset processing and metadata management for independent developers. It automates tedious file conversions and API hooks to keep your project pipeline clean and efficient.

## Features
*   **Sprite Sheet Optimizer:** Automatically crops, trims whitespace, and generates JSON texture atlases from raw image assets.
*   **Discord Presence Sync:** Effortless integration with the Discord Rich Presence API to display real-time player stats and game states.
*   **Config Parser:** A lightweight handler for structured `.yaml` and `.toml` configuration files with built-in validation for game balance variables.
*   **Log Analytics:** An asynchronous logger that tracks engine performance metrics and crash reports directly to a local development dashboard.

## Installation

Ensure you have Python 3.9+ installed. Install the toolkit via pip:

```bash
pip install dev-toolkit-91
```

To install from source for development purposes:

```bash
git clone https://github.com/Developer/dev-toolkit-91.git
cd dev-toolkit-91
pip install -e .
```

## Usage

Quickly initialize the Discord Presence manager within your main game loop:

```python
from dev_toolkit import DiscordManager

# Initialize with your application client ID
presence = DiscordManager(client_id="1234567890")

# Update game state dynamically
presence.update(state="Exploring the Wasteland", details="Level 15")
```

For advanced configuration parsing:

```python
from dev_toolkit import ConfigLoader

# Automatically load and validate balance settings
config = ConfigLoader.load("settings/balance.yaml")
player_speed = config.get("player_speed", default=5.0)
```

## License
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.