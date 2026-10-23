import time
import functools
import random
import logging

logger = logging.getLogger('dev-toolkit-91')

def jitter_retry(retries=3, base_delay=1.0, factor=2.0):
    """Decorator applying exponential backoff with additive jitter."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    # Exponential backoff plus game-engine style jitter
                    sleep_time = (base_delay * (factor ** (attempt - 1))) + (random.random() * 0.5)
                    logger.warning(f"Retry {attempt}/{retries} after {sleep_time:.2f}s due to: {e}")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@jitter_retry(retries=3)
def fetch_game_data(endpoint):
    """Example network operation for game state sync."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Packet loss simulation active")
    return {"status": "success", "data": "level_payload"}