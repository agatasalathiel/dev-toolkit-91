import time
import random
from functools import wraps

def frame_throttle(ms_delay=16):
    def decorator(func):
        last_call = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            if (now - last_call) * 1000 >= ms_delay:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def loot_generator(pool, luck_modifier=1.0):
    weights = [item['weight'] * luck_modifier for item in pool]
    return random.choices(pool, weights=weights, k=1)[0]

def hex_to_rgb(hex_val):
    hex_val = hex_val.lstrip('#')
    return tuple(int(hex_val[i:i+2], 16) for i in (0, 2, 4))

class EntityRegistry:
    def __init__(self):
        self._storage = {}

    def __setitem__(self, key, value):
        self._storage[key] = {'data': value, 'ts': time.time()}

    def get_active(self, ttl=60):
        now = time.time()
        return {k: v['data'] for k, v in self._storage.items() if now - v['ts'] < ttl}

    def __repr__(self):
        return f"Registry(items={len(self._storage)})"