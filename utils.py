import functools
import logging
import time
from typing import Callable, Any

logger = logging.getLogger('dev-toolkit-91')

class GameResourceCleaner:
    def __init__(self, resource_map: dict):
        self._resources = resource_map

    def purge_stale_assets(self, threshold_ms: int = 5000):
        now = time.time_ns() // 1_000_000
        keys_to_drop = [k for k, v in self._resources.items() if now - v.last_access > threshold_ms]
        for k in keys_to_drop:
            del self._resources[k]
        return len(keys_to_drop)

def memoize_game_state(func: Callable) -> Callable:
    cache = {}
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def sanitize_input(data: str) -> str:
    return ''.join(char for char in data if char.isalnum() or char in '_-')

def batch_process(items: list, chunk_size: int = 10):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def log_performance(func: Callable):
    @functools.wraps(func)
    def timed(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f'{func.__name__} executed in {duration:.4f}s')
        return result
    return timed