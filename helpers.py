import time
import random
from typing import Callable, Any, Dict

def frame_rate_throttle(fps: int) -> Callable:
    interval = 1.0 / fps
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed < interval:
                time.sleep(interval - elapsed)
            return result
        return wrapper
    return decorator

def loot_generator(pool: Dict[str, float]) -> str:
    items = list(pool.keys())
    weights = list(pool.values())
    return random.choices(items, weights=weights, k=1)[0]

def hex_color_to_rgb(hex_val: str) -> tuple:
    hex_val = hex_val.lstrip('#')
    return tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))

def byte_size_formatter(bytes_count: int) -> str:
    units = ['B', 'KB', 'MB', 'GB']
    idx = 0
    while bytes_count >= 1024 and idx < len(units) - 1:
        bytes_count /= 1024
        idx += 1
    return f"{bytes_count:.2f} {units[idx]}"

class EntityClock:
    def __init__(self):
        self.ticks = 0
    def tick(self):
        self.ticks += 1
    def is_divisible(self, n: int) -> bool:
        return self.ticks % n == 0