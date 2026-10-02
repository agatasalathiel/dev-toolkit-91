import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('dev-toolkit-91')

class GameStateError(Exception):
    pass

def graceful_recovery(default_value: Any = None):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, TypeError, IndexError, KeyError) as e:
                logger.error(f'dev-toolkit-91 edge case caught in {func.__name__}: {e}')
                return default_value
            except Exception as e:
                logger.critical(f'unhandled chaos in {func.__name__}: {e}')
                raise GameStateError(f'critical game failure: {e}') from e
        return wrapper
    return decorator

@graceful_recovery(default_value={})
def safe_extract_game_data(data: dict, key_path: str):
    parts = key_path.split('.')
    current = data
    for part in parts:
        current = current[part]
    return current

def sanitize_input(value: Any) -> str:
    try:
        return str(value).encode('ascii', 'ignore').decode('utf-8')
    except Exception:
        return 'corrupted_packet'