# Dev Toolkit 91

Dev Toolkit 91 is a comprehensive Python-based toolkit designed for game developers to streamline their development process. This toolkit offers essential utilities and simplifies a variety of tasks, making game creation more efficient and enjoyable.

## Features

- **Sprite Management**: Easily load, manage, and animate 2D sprites with optimized performance.
- **Audio Integration**: Simplified audio playback with support for various formats, allowing seamless background music and sound effects.
- **Event System**: Robust event handling that enables the creation of responsive game mechanics without complex coding.
- **Config Management**: Load and edit game configurations via JSON files, facilitating easy adjustments during development and testing.

## Installation

To get started with Dev Toolkit 91, ensure you have Python installed on your machine. Then, clone the repository and install the required dependencies with the following commands:

```bash
git clone https://github.com/Developer/dev-toolkit-91.git
cd dev-toolkit-91
pip install -r requirements.txt
```

## Basic Usage Example

Here's a quick example to demonstrate how to use the toolkit for loading a sprite:

```python
from dev_toolkit import Sprite, Audio, EventManager

# Initialize the sprite
player_sprite = Sprite('assets/player.png')
player_sprite.set_position(100, 150)

# Load background music
background_music = Audio('assets/music/background.mp3')
background_music.play(loop=True)

# Create an event for handling player input
event_manager = EventManager()

def on_key_press(key):
    if key == 'space':
        player_sprite.jump()

event_manager.add_listener('key_press', on_key_press)

# Start your game loop
while True:
    event_manager.process_events()
    player_sprite.update()
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Dev Toolkit 91 is licensed under the MIT License. See the LICENSE file for details. This toolkit aims to empower game developers with better tools and experiences, fostering creativity and innovation in game design.