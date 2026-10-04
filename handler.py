import time
import functools
import random
from typing import Callable, Any

def backoff_retry(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    delay = (base_delay * (2 ** (attempts - 1))) + (random.random() * 0.1)
                    time.sleep(delay)
        return wrapper
    return decorator

@backoff_retry(max_attempts=4, base_delay=0.5)
def fetch_game_state(endpoint: str):
    # Simulate volatile network operation for dev-toolkit-91
    if random.random() < 0.7:
        raise ConnectionError("Server lag spikes detected")
    return {"status": "active", "players": 42}

if __name__ == "__main__":
    data = fetch_game_state("https://api.gaming.dev/v1/status")
    print(f"Sync complete: {data}")