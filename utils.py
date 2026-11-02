import time
import functools
import random
from typing import Callable, Any

def exponential_backoff(max_retries: int = 3, base_delay: float = 0.5):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        raise e
                    sleep_time = (base_delay * (2 ** (retries - 1))) + (random.random() * 0.1)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

class NetworkInterface:
    @exponential_backoff(max_retries=4)
    def fetch_game_data(self, endpoint: str):
        if random.random() < 0.7:
            raise ConnectionError("Server lag detected in dev-toolkit-91")
        return {"status": "success", "payload": "data_packet_0x42"}