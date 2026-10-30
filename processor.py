import time
import random
from functools import wraps

def gaming_retry(max_attempts=3, backoff=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    sleep_time = backoff * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, latency_sim=False):
        self.latency_sim = latency_sim

    @gaming_retry(max_attempts=3, backoff=0.2)
    def fetch_game_data(self, endpoint):
        if self.latency_sim and random.random() < 0.7:
            raise ConnectionError(f'Packet loss at {endpoint}')
        return {'status': 'success', 'data': 'pixel_art_blob'}

if __name__ == '__main__':
    proc = NetworkProcessor(latency_sim=True)
    result = proc.fetch_game_data('api/v1/assets')
    print(f'Retrieved: {result}')