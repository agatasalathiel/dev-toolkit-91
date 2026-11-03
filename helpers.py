import time
import functools
import random

def throttle(interval=1.0):
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                return None
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def jitter_delay(base=0.1, variance=0.05):
    time.sleep(base + (random.random() * variance))

def chunk_list(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def dict_deep_merge(base, update):
    for key, value in update.items():
        if isinstance(value, dict) and key in base:
            dict_deep_merge(base[key], value)
        else:
            base[key] = value
    return base

def format_ticks(ticks, tps=60):
    seconds = ticks / tps
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{s:05.2f}"

class GameStateContext:
    def __init__(self, data=None):
        self.data = data or {}
    def __enter__(self):
        return self.data
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.clear()