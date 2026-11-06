import time
import functools
from typing import Callable, Any, Type

def retry_gaming_op(max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (ConnectionError, TimeoutError)):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_ex = e
                    time.sleep(delay * (2 ** attempt))
            raise last_ex
        return wrapper
    return decorator

@retry_gaming_op(max_attempts=4, delay=0.5)
def fetch_leaderboard_data(url: str):
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server lag spikes detected")
    return {"status": "success", "payload": [100, 200, 300]}