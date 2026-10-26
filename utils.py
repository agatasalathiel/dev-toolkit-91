import time
import functools
import random
import logging

logger = logging.getLogger('dev-toolkit-91')

def retry_with_backoff(max_attempts=3, base_delay=1.0, jitter=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f'Critical failure after {max_attempts} attempts: {e}')
                        raise
                    
                    delay = base_delay * (2 ** (attempts - 1))
                    if jitter:
                        delay *= random.uniform(0.5, 1.5)
                    
                    logger.warning(f'Attempt {attempts} failed, retrying in {delay:.2f}s...')
                    time.sleep(delay)
        return wrapper
    return decorator

class NetworkInterface:
    @retry_with_backoff(max_attempts=4)
    def fetch_game_data(self, endpoint):
        # Simulated volatile network environment
        if random.random() < 0.7:
            raise ConnectionError('Packet loss encountered')
        return {'status': 'success', 'data': 'payload_0x91'}