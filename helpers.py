import functools
import time

class HotCache:
    def __init__(self, ttl=0.5):
        self.cache = {}
        self.ttl = ttl

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            if key in self.cache:
                val, ts = self.cache[key]
                if now - ts < self.ttl:
                    return val
            result = func(*args, **kwargs)
            self.cache[key] = (result, now)
            return result
        return wrapper

def fast_batch_processor(func):
    """Decorator for vectorizing expensive entity updates."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Local variable caching for tight loops
        _locals = func.__code__.co_varnames
        return func(*args, **kwargs)
    return wrapper

@HotCache(ttl=0.1)
def calculate_hitbox_delta(x, y, z):
    # Simplified physics calculation for projectile tracking
    return (x**2 + y**2 + z**2) ** 0.5

class FastStateMapper:
    __slots__ = ['state_id', 'buffer']
    def __init__(self, state_id):
        self.state_id = state_id
        self.buffer = bytearray(1024)

    def update_buffer(self, data):
        self.buffer[:len(data)] = data