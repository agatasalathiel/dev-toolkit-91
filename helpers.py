import random
import time
from typing import Any, Callable, TypeVar, List

T = TypeVar('T')

def jitter_delay(base_ms: int, variance: int = 50) -> None:
    """Simulates human-like latency for game engine inputs."""
    delay = (base_ms + random.randint(-variance, variance)) / 1000
    time.sleep(max(0, delay))

def chunk_game_state(data: List[T], size: int) -> List[List[T]]:
    """Partition heavy state packets for transmission."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def retry_operation(func: Callable[..., T], retries: int = 3) -> T:
    """Resilient execution wrapper for unstable game hooks."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if i == retries - 1:
                raise e
            time.sleep(0.1 * (2 ** i))

def sanitize_name(raw_name: str) -> str:
    """Cleans player usernames by stripping control characters."""
    return ''.join(c for c in raw_name if c.isalnum() or c in ' _-').strip()