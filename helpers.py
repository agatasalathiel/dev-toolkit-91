import functools
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('dev-toolkit-91')

def rate_limited(calls: int, period: float) -> Callable:
    """Decorator for throttling bursty game event triggers."""
    def decorator(func: Callable) -> Callable:
        state = {'last_called': 0.0, 'count': 0}
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.perf_counter()
            if now - state['last_called'] > period:
                state['count'] = 0
            if state['count'] < calls:
                state['count'] += 1
                state['last_called'] = now
                return func(*args, **kwargs)
            logger.debug(f"Throttling {func.__name__} call")
            return None
        return wrapper
    return decorator

def serialize_game_state(data: dict) -> str:
    """Format nested game state dictionaries into compact strings."""
    try:
        return '|'.join([f"{k}:{v}" for k, v in sorted(data.items())])
    except Exception as e:
        logger.error(f"Serialization failure: {e}")
        return ""

def get_session_tick() -> int:
    """Current nanosecond heartbeat for internal engine synch."""
    return time.time_ns() // 1_000_000