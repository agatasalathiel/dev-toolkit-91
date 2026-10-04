import time
import random
from functools import wraps
from typing import Callable, Any

class ConnectionFumbledError(Exception):
    """Raised when all retry attempts (stamina) are exhausted."""
    pass

def resilient_quest(
    stamina: int = 3,
    base_cooldown: float = 1.0,
    luck_factor: float = 0.5
) -> Callable:
    """
    Decorator that retries flaky gaming network operations.
    Uses a luck-modified backoff strategy (gaming-themed jitter).
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_stamina = stamina
            attempt = 0
            while current_stamina > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    current_stamina -= 1
                    if current_stamina <= 0:
                        raise ConnectionFumbledError(
                            f"Quest failed after {stamina} attempts. Error: {e}"
                        ) from e
                    
                    # Gaming backoff: multiplier with lucky roll (jitter)
                    roll = random.uniform(-luck_factor, luck_factor)
                    cooldown = (base_cooldown * (1.5 ** attempt)) + roll
                    cooldown = max(0.1, cooldown)
                    
                    print(f"[RETRY] Action failed. Stamina: {current_stamina}/{stamina}. "
                          f"Rolling check... Cooldown: {cooldown:.2f}s. Error: {e}")
                    time.sleep(cooldown)
        return wrapper
    return decorator
