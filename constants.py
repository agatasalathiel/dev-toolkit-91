import os

# Constants for game configuration

# Game states
INITIALIZING = 'initializing'
RUNNING = 'running'
PAUSED = 'paused'
GAME_OVER = 'game_over'

# Default settings
DEFAULT_SETTINGS = {
    'screen_width': 800,
    'screen_height': 600,
    'fps': 60,
    'background_color': (0, 0, 0),  # Black
}

# Error messages
ERROR_MESSAGES = {
    'file_not_found': 'The specified file was not found.',
    'invalid_game_state': 'The game is in an invalid state.',
    'settings_format': 'Settings format is incorrect.',
}

# A simple function to fetch a configuration value with error checking

def fetch_config_value(key):
    try:
        if key not in DEFAULT_SETTINGS:
            raise KeyError(ERROR_MESSAGES['settings_format'])
        return DEFAULT_SETTINGS[key]
    except KeyError as e:
        print(f'Error: {str(e)}')
        return None
    except Exception as e:
        print(f'Unexpected error: {str(e)}')
        return None
