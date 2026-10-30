import time
import random
from typing import Any, Callable, TypeVar

T = TypeVar('T')

def throttle(rate_limit: float) -> Callable:
    """Artificially slows down game events to match frame budget."""
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait = rate_limit - elapsed
            if wait > 0:
                time.sleep(wait)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def jitter(func: Callable) -> Callable:
    """Adds pseudo-random variation to combat outcomes."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result * random.uniform(0.95, 1.05)
        return result
    return wrapper

def batch_process(items: list[T], chunk_size: int = 10) -> list[list[T]]:
    """Chunks heavy assets for parallel loading routines."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def memoize_ttl(ttl: int = 300) -> Callable:
    """Temporary cache for game state queries."""
    cache = {}
    def decorator(func: Callable):
        def wrapper(*args):
            now = time.time()
            if args in cache and (now - cache[args][1]) < ttl:
                return cache[args][0]
            res = func(*args)
            cache[args] = (res, now)
            return res
        return wrapper
    return decorator