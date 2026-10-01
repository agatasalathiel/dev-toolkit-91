import time
import functools
import random

def retry_gaming_op(max_attempts=3, base_delay=1.0):
    def decorator(func):
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
                    # Exponential backoff with jitter for game server sync
                    delay = (base_delay * (2 ** (attempts - 1))) + (random.random() * 0.5)
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_gaming_op(max_attempts=4)
def fetch_server_payload(endpoint):
    # Simulated niche gaming network operation
    if random.random() < 0.7:
        raise ConnectionError("Game server heartbeat missed")
    return {"status": "ready", "tick": 128}

if __name__ == "__main__":
    data = fetch_server_payload("lobby/region-eu")
    print(f"Successfully synced: {data}")